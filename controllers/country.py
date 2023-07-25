from flask import request
from flask import jsonify
from services.country import get_country_info

# 
def get():
    country = request.args.get("code", "tjk")

    country_data = get_country_info(country)

    print(country_data)

    return jsonify(country_data[1]), country_data[0]
