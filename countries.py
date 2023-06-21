# this returns list of all countries and area (a dictionary with 299 items).

import requests
import json
import csv

url = 'http://api.worldbank.org/v2/country?format=json&per_page=299'
response = requests.get(url)
json_response = response.json()
# pprint(json_response) ... to get all contents in json_response like indicator names, ...

countries = []
for item in json_response[1]:
    countries.append([item["id"], item["name"]])

with open("countries.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id", "name"])
    for row in countries:
        writer.writerow(row)