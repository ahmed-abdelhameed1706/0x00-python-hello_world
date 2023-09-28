#!/bin/bash
# getting the methods of a respone with curl
curl -s -I $1 | grep -i "Allow" | cut -d " " -f2-
