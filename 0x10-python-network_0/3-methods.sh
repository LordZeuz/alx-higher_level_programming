#!/bin/bash
curl -s -I -X OPTIONS "$1" | grep "Allow" | tr -d '\r'
