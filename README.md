# Cloud Computing - Activity 4

Object storage and caching for HTTP services using Redis and S3 (MinIO).

Author: José Ignacio Piedra Rascón (Nacho)

## Delivery links

- GitHub repository: https://github.com/Nachopiedra/activity-4
- DockerHub image: https://hub.docker.com/r/nachopiedra/activity-4

## Overview

A file-storage HTTP API built with FastAPI, following a hexagonal architecture
with dependency injection so that persistence backends are fully interchangeable.

- Redis is used as a cache for session tokens (with automatic expiration).
- MinIO (S3-compatible) is used as object storage for file contents.
- File metadata and file content are stored separately.

## Architecture

Each module (authentication, files) follows the same layered layout:

- api/ : routers (HTTP layer only).
- domain/controllers/ : use-case logic.
- domain/bo/ : business objects.
- domain/persistences/ : abstract interfaces (ports).
- persistence/ : concrete adapters (redis, minio, memory, postgres).
- dependency_injection/ : singletons wiring the API to the domain.

## How to run

Build and start the services:

    docker compose build carlemany-backend
    docker compose up -d postgres redis minio-server minio carlemany-backend

Check that the API is up:

    curl http://localhost:8000/healthcheck

The API is exposed on port 8000 (mapped to port 80 inside the container).

## Endpoints

Authentication:

- POST /register : create a new user.
- POST /login : authenticate and receive a session token.
- POST /logout : close the session (token in the Auth header).
- GET /introspect : validate a token and return the user (token in Auth).

Files (token always sent in the Auth header):

- GET /files : list the files owned by the user.
- POST /files : create file metadata (returns the new file id).
- GET /files/{id} : get a file's metadata.
- DELETE /files/{id} : delete a file (metadata and content).
- POST /files/{id} : upload the file content (stored in MinIO).
- POST /files/merge : merge several PDF files into a new one.

## Continuous integration

A GitHub Actions workflow (.github/workflows/ci.yml) runs ruff and black
format checks on every push and pull request.

## Formatting

    ruff check .
    black --config .black .

## Notes

The minio client service image in docker-compose.yml was updated from the
deprecated minio/mc to quay.io/minio/mc, since the former is no longer
available on Docker Hub.
