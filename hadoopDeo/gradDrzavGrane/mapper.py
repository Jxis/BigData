#!/usr/bin/env python3
"""mapper.py"""
import sys

def extract_id(url):
    parts = url.split('/')
    if '/' in url and len(parts) > 1:
        last_part = parts[-1]
        if last_part.startswith("Q"):
            return last_part[1:]
    return url

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    if len(parts) >= 7:
        city_id = extract_id(parts[0])
        country_id = extract_id(parts[3])
        print(f'{city_id}\t{sister_id}')