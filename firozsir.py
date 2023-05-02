import requests
from flask import Flask, jsonify, request, render_template, redirect, url_for
from requests_ntlm import HttpNtlmAuth
import xmltodict, json

url = "http://49.249.232.210:10047/BCPLNAV01/WS/Bodycare%20Creations%20Ltd./Codeunit/DistibuterPortal"
def hitapi(username, password):
    payload = "<Envelope xmlns=\"http://schemas.xmlsoap.org/soap/envelope/\">\n    <Body>\n        <ValidateWeUser xmlns=\"urn:microsoft-dynamics-schemas/codeunit/DistibuterPortal\">\n            <userID>username</userID>\n            <pWS>password</pWS>\n            <errText></errText>\n            <userName></userName>\n        </ValidateWeUser>\n    </Body>\n</Envelope>"
    payload = payload.replace("username",username)
    payload = payload.replace("password",password)
    headers = {
        'SoapAction': 'ValidateWeUser',
        'Content-Type': 'application/xml'
    }
    response = requests.request("POST", url, headers=headers, data=payload, auth=HttpNtlmAuth('Administrator','bE$sAFE%D30a205_82'))
    #print(response.status_code)
    #print(response.request.body)
    #print(response.request.headers)
    xpars = xmltodict.parse(response.text)
    #print(json.dumps(xpars))
    return json.dumps(xpars)
    #return response.json()


app = Flask(__name__ )
@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        #return request.form
        username = request.form['username']
        password = request.form['password']
        a = hitapi(username,password)
        print(a)
        return a

    else:
        username = request.args.get('username')
        password = request.args.get('password')
        a = hitapi(username,password)
    return jsonify({a})
    #hitapi("C1114","1234")
if __name__ == '__main__':
    app.run(debug=True, port=2020)