#!/bin/bash
# sends a JSON request to url passed
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"
