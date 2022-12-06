#!/bin/bash
set -xe

exec uvicorn app.main:app --workers 3 --host 0.0.0.0 --http h11 --port 8002
