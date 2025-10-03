#!/bin/bash
curl http://127.0.0.1:8000/health
# -> {"status":"ok"}

curl -X POST http://127.0.0.1:8000/send -H "content-type: application/json" -d '{"message":"hi","meta":{"k":1}}'
# -> {"ok": true, "echo": {"message":"hi","meta":{"k":1}}}

curl -X POST http://127.0.0.1:8000/send -H "content-type: text/plain" --data-raw "hello"
# -> {"ok": true, "echo": {"message":"hello"}}
