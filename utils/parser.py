import json
import requests
from typing import Dict


def parse_country_data(country_cco: str) -> Dict | None:
    """
    The function is intended for parsing data about a 
    country or about countries.
    Used as a reusable job with an interval of 2 hours

    Function signature:
        - countries — the target country whose data will be collected
    """

    # Main link to get data
    URL = "https://restcountries.com/v3.1/alpha?codes="

    # Obtaining data for the target country
    country_response = requests.get(URL + country_cco)
    if country_response.status_code != 200:
        # TODO: Setup logger
        return None

    # Try to turn the received data about the country
    #   into json format for easy work with data
    temp_country_data = json.loads(country_response.text)

    # Extracting useful information from the response.
    country_data = extract_country_data(temp_country_data[0])

    # Extract information about the surrounding neighbors
    #   of the target country from the json and form a link
    #   about obtaining these neighbors
    borders_response = requests.get(
        URL + ','.join(temp_country_data[0]['borders'])
    )

    # Using the built-in sort function, we sort the data by
    #   area in ascending order, which is in the json
    # The lambda construct helps reverse items in descending order
    #
    # Visual example:
    #   leaf initial state:           [1, 8, 4, 2]
    #   apply the lambda construct:   [0-1, 0-8, 0-4, 0-2] >> [-1, -8, -4, -2]
    #   apply sort():                 [-8, -4, -2, -1]
    #
    # Data only applies a negative value in the lambda construct,
    #  the underlying data is not affected in any way
    borders_data = json.loads(borders_response.text)
    borders_data.sort(key=lambda x: 0 - x["area"])

    temp_border_countries = list()

    # Iterate over all surrounding neighbours, get the data and add
    #   it to a temporary sheet that will be added to the final dict
    for i in borders_data:
        temp_border_countries.append(extract_country_data(i))

    country_data["borders"] = temp_border_countries

    return country_data

# Helper function `extract_country_data` allows you to extract
# certain data from the dict.
def extract_country_data(country_data: dict) -> Dict:
    temp_data = dict()

    temp_data["area"] = country_data["area"]
    temp_data["borders"] = country_data["borders"]
    temp_data["capital"] = country_data["capital"]
    temp_data["car"] = country_data["car"]
    temp_data["cca3"] = country_data["cca3"]
    temp_data["currencies"] = country_data["currencies"]
    temp_data["flags"] = country_data["flags"]
    temp_data["idd"] = country_data["idd"]
    temp_data["independent"] = country_data["independent"]
    temp_data["languages"] = country_data["languages"]
    temp_data["latlng"] = country_data["latlng"]
    temp_data["name"] = country_data["name"]
    temp_data["population"] = country_data["population"]
    temp_data["timezones"] = country_data["timezones"]
    temp_data["unMember"] = country_data["unMember"]

    return temp_data
