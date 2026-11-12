import requests
from django.conf import settings


class DP5Error(Exception):
    """Anything that went wrong talking to DP5, with a message safe to show users."""


def _url(path):
    return f"{settings.DP5_URL.rstrip('/')}/dp5/remote/v1{path}"


def get_status():
    try:
        r = requests.get(_url("/system/status"), timeout=5)
        r.raise_for_status()
        return r.json()["status"]          # e.g. "IDLE"
    except requests.RequestException as e:
        raise DP5Error("The scanner service is not reachable.") from e


def scan(container_uid=None):
    uid = container_uid or settings.DP5_CONTAINER_UID
    try:
        r = requests.post(_url("/scan"), params={"container_uid": uid},
                          timeout=settings.DP5_TIMEOUT)
    except requests.Timeout as e:
        raise DP5Error("The scanner took too long to respond.") from e
    except requests.ConnectionError as e:
        raise DP5Error("The scanner service is not running.") from e

    if r.status_code != 200:
        # DP5 returns ErrorInfo JSON with a userFriendlyMessage for its custom 4xx codes
        try:
            msg = r.json().get("userFriendlyMessage") or r.json().get("message")
        except ValueError:
            msg = None
        raise DP5Error(msg or f"Scan failed (HTTP {r.status_code}).")

    return r.json()