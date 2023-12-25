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
    if len(parts) >= 5:
        id = extract_id(parts[0]) # id of city
        countryId = extract_id(parts[3]) #id of country
        name = parts[1] #city name
        country = parts[4] #country name
        print(f'{city_id}\t{country_id}\t{city_name}\t{country_name}')