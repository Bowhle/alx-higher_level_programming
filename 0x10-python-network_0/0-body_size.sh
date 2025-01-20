#!/bin/bash
# Takes in a URL, sends a request, and displays the body size in bytes.
curl -s -w '%{size_download}\n' -o /dev/null "$1"
