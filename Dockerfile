# Dockerfile reference guide at https://docs.docker.com/go/dockerfile-reference/

# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.2
FROM python:${PYTHON_VERSION}-slim@sha256:ac212230555ffb7ec17c214fb4cf036ced11b30b5b460994376b0725c7f6c151 as base


# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN mkdir -p /app/staticfiles

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# create the appropriate directories
# ENV HOME=/home/app
# ENV APP_HOME=/home/app/web
# RUN mkdir $APP_HOME
# RUN mkdir $APP_HOME/staticfiles
# WORKDIR $APP_HOME

# Install required system packages and ODBC driver for SQL Server
RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    gnupg \
    unixodbc-dev \
    && curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /etc/apt/trusted.gpg.d/microsoft.gpg \
    && echo "deb [arch=amd64] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
# Install Python dependencies

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Copy the source code into the container.
COPY . .

RUN chown -R appuser:appuser /app

# Switch to the non-privileged user to run the application.
USER appuser


# This will collect all static files into the directory specified by STATIC_ROOT in your settings.py
RUN SECRET_KEY=dummy \
    DEFAULT_URL=sqlite:////tmp/db.sqlite3 \
    SHIRE_URL=sqlite:////tmp/db.sqlite3 \
    ALLOWED_HOSTS="localhost" \
    CSRF_TRUSTED_ORIGINS="http://localhost:8000" \
    python manage.py collectstatic --noinput
# # Expose the port that the application listens on.
# EXPOSE 8000
#
# # Run the application.
# CMD python manage.py runserver

# entrypoint shell scripts to be executed
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
