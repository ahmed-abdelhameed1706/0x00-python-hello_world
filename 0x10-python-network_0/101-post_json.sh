#!/bin/bash
# getting the content of a respone with curl
curl -X POST $1 -H "Content-Type: application/json" -d "$(cat $2)"
