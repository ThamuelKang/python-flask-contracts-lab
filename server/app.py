#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {
        "id": 3,
        "contract_information": "This contract is to confirm ownership of this car",
    },
]
customers = ["bob", "bill", "john", "sarah"]
app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/contract/<id>")
def get_contract(id):

    contract_id = int(id)

    contract = None
    for c in contracts:
        if c["id"] == contract_id:
            contract = c
            break
    
    if contract is not None:
        body = contract["contract_information"]
        status = 200
    else:
        body = "Contract not found."
        status = 404
    return make_response(body, status)


@app.route("/customer/<customer_name>")
def get_customers(customer_name):
    if customer_name in customers:
        body = ""
        status = 204
    else:
        body = "Contract not found"
        status = 404
    return make_response(body, status)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
