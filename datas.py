# this returns all valid indicator for all countreis

import requests
import json
import time
from datetime import datetime
import psycopg2
import sentry_sdk


sentry_sdk.init(
    dsn="http://aafa1f815c234017b4db553810bef7be@94.182.88.211:9000/9",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


def save_datas_to_json(data, fileName=''):
    if fileName.endswith('.json'):
        # Saving data to JSON file
        with open(f"exported_data/{fileName}", 'w') as outfile:
            json.dump(data, outfile)
    else:
        # Saving data to plain text file
        with open(f"exported_data/{fileName}", 'w') as outfile:
            outfile.write(str(data))


def get_data(indicator, page = 1, per_page = 1000):
    url = f'http://api.worldbank.org/v2/countries/all/indicators/{indicator}?date=1960%3A2022&format=json&per_page={per_page}&page={page}'
    response = requests.get(url)
    return response.json()


def log(message):
    print(message)


def collect_data():

    # Set up the database connection
    conn = psycopg2.connect(
        host = "localhost",
        database = "worldbank",
        user = "postgres",
        password = "654321"
    )
    # Create a cursor object from the connection
    cur = conn.cursor()

    with open('exported_data/indicators_copy.json') as file:
        indicators = json.load(file)

    with open('exported_data/failed_indicators.json') as file:
        failed_indicators = json.load(file)

    counter = 0

    for indicator in indicators[:]:
        indicators.remove(indicator)
        log(f"getting {indicator} data ...")
        page = 1
        per_page = 2000
        # errors = []

        while True:
            try:
                # make API request with current page and per_page values
                response = get_data(indicator, page, per_page)
                for item in range(len(response[1])):
                    data = (response[1][item]["indicator"]["id"], 
                            response[1][item]["country"]["id"],
                            response[1][item]["date"],
                            response[1][item]["value"])

                    query = "INSERT INTO datas (indicator, country, date, amount) VALUES (%s, %s, %s, %s)"
                    cur.execute(query, data)

                # increment the page value to fetch the next page of data
                page += 1
                time.sleep(1)

                # check if there are more pages to fetch
                if page > response[0]['pages']:
                    # save_datas_to_json(indicator_datas, f"{datetime.now().strftime('%d-%m-%Y,%H-%M-%S')}-{indicator}.json" )
                    log('saved')
                    break
            except:
                # # check if the indicator was not found or returns bad response. It may have been deleted or archived.
                # errors.extend(response)
                # save_datas_to_json(errors, f'ERROR_{indicator}.log')
                failed_indicators.append(indicator)
                log('failed')
                break
        
        conn.commit()
        time.sleep(1)

        # this is for API request limitation. I want to fetch just 2000 indicator datas for each time
        counter += 1
        if counter >= 30:
            break

    # Commit the changes to the database and close the cursor and connection
    cur.close()
    conn.close()

    # save a copy of indicators that does not checked and fetched its data yet.(deleted indicators that executed)                
    save_datas_to_json(indicators, "indicators_copy.json" )

    save_datas_to_json(failed_indicators, 'failed_indicators.json')

for i in range(50):
    collect_data()
    log(f"-------------------> loop {i+1} complited")
    time.sleep(3)
