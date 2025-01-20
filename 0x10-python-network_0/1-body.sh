#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response only if the status code is 200.

# Send GET request and store the response code and body
response=$(curl -sL -w "%{http_code}" -o /tmp/body "$1")

# If the response code is 200, display the body
if [ "$response" -eq 200 ]; then
  cat /tmp/body
fi