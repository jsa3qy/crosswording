#!/bin/sh
set -e
pip3 install -r requirements.txt || pip install -r requirements.txt
python3 main.py "$1" "$2"