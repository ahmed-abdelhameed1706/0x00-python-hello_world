#!/bin/bash
# sending a post request with params and getting the content of a respone with curl
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
