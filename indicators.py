# this returns list of all indicator ids and names (with 20941 items)

import requests
import json
import csv

url = 'http://api.worldbank.org/v2/indicator?format=json&per_page=20941'
response = requests.get(url)
json_response = response.json()
# pprint(json_response) ... to get all contents in json_response like indicator names, ...

indicators = []
for item in json_response[1]:
    indicators.append([item["id"], item["name"]])

with open("indicators.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id", "name"])
    for row in indicators:
        writer.writerow(row)
