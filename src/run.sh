#!/bin/sh
cd "$(dirname "$0")"
python3 server.py&
TO_KILL=$!
python3 app.py
kill $TO_KILL