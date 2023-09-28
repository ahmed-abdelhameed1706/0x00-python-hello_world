#!/bin/bash
# getting only the status code of a respone with curl
curl -I -s -o /dev/null -w "%{http_code}" $1
