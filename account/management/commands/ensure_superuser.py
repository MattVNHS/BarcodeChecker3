import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create the local admin account from environment variables if it doesn't exist."

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "")

        # (A) Opt-in: if the variables aren't set, do nothing rather than fail.
        if not username or not password:
            self.stdout.write("Superuser env vars not set; skipping.")
            return

        # (B) Idempotent: safe to run on every container start.
        if User.objects.filter(username=username).exists():
            self.stdout.write(f"Superuser '{username}' already exists; skipping.")
            return

        # (C) create_superuser hashes the password and sets is_staff + is_superuser.
        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f"Created superuser '{username}'."))