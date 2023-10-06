import requests
import json
from requests_ntlm import HttpNtlmAuth
from flask import Flask, jsonify, request, render_template, redirect, url_for
import logging
from datetime import date, datetime


logging.basicConfig(filename="/Users/ayushmohanawasthi/IdeaProjects/Automation/automation/scm-automation-python/logs/" + str(date.today()) + ".log", format='%(asctime)s %(message)s', filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# setting up flask app
app = Flask(__name__, template_folder='template')



@app.route('/visiting/<name>/<designation>/<company_name>/<email>/<phone>/<website>', methods=['GET'])
def visiting_card_details(name,designation,company_name,email,phone,website):
    print(name,designation,company_name,email,phone,website)
    return render_template("index.html", name= name, designation=designation,company_name=company_name,email=email,phone=phone,website=website)

@app.route('/greet', methods=['GET'])
def greet():
    return jsonify("Hi there, please enter your name and details as per API")

app.config["DEBUG"] = True

# starting flask application
if __name__ == '__main__':
    # app.run(debug=True, port=6262)
    app.run(host='127.0.0.1', port=6262, debug=True)
