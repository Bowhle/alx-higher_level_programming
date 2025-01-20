#!/bin/bash
# Takes in a URL, sends a request, and displays the body size in bytes.
# The -s option silences the output,
# and -w is used to print the size of the response body
curl -s "$1" | wc -c
