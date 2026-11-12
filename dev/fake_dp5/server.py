import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

HERE = Path(__file__).parent
SCAN_OK = json.loads((HERE / "scan_200.json").read_text(encoding="utf-8"))

# Special container_uids that trigger DP5's error responses
ERRORS = {
    "notfound":  (453, "Container not found"),
    "noscanner": (461, "Scanner not connected"),
    "badread":   (477, "Failed to read barcode"),
}


class FakeDP5(BaseHTTPRequestHandler):
    def send_json(self, code, body):
        data = json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/dp5/remote/v1/system/status":
            return self.send_json(200, {"status": "IDLE"})
        if path == "/dp5/remote/v1/system/version":
            return self.send_json(200, {"version": "fake-dp5"})
        self.send_json(404, {"message": f"Fake DP5 doesn't implement GET {path}"})

    def do_POST(self):
        url = urlparse(self.path)
        if url.path != "/dp5/remote/v1/scan":
            return self.send_json(404, {"message": f"Fake DP5 doesn't implement POST {url.path}"})

        uid = parse_qs(url.query).get("container_uid", [""])[0]

        if uid == "slow":
            time.sleep(60)  # longer than DP5_TIMEOUT, to test your timeout handling

        if uid in ERRORS:
            code, msg = ERRORS[uid]
            return self.send_json(code, {
                "status": code, "message": msg, "userFriendlyMessage": msg, "path": url.path,
            })

        time.sleep(2)  # a real scan takes a moment; makes the UI feel realistic
        self.send_json(200, SCAN_OK)


if __name__ == "__main__":
    print("Fake DP5 listening on :8777", flush=True)
    ThreadingHTTPServer(("0.0.0.0", 8777), FakeDP5).serve_forever()