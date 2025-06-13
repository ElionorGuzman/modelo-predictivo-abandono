#!/usr/bin/env bash
uvicorn api_abandono:app --host 0.0.0.0 --port $PORT
