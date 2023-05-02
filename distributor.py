import os
from flask import Flask,jsonify,request,render_template,redirect,url_for


app = Flask(__name__,template_folder='templates')

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('index.html')



app.config['DEBUG']= True
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True, port = 6262)