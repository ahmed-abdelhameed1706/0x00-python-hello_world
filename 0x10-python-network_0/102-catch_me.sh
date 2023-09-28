#!/bin/bash
# getting the content of a respone with curl
curl -s 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -L --max-redirs 100 -H "Origin: School"
