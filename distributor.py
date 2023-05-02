import os
from flask import Flask,jsonify,request,render_template,redirect,url_for
from fetch_item_list import fetch_item_list

app = Flask(__name__,template_folder='templates')

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('index.html')

@app.route('/create_so', methods = ['POST', 'GET'])
def create_so():
    list_user = fetch_item_list()
    #list_user = ["C++", "Python", "PHP", "Java", "C", "Ruby","R", "C#", "Dart", "Fortran", "Pascal", "Javascript"]
    return render_template('create_sale_order.html', languages=list_user)


app.config['DEBUG']= True
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True, port = 6262)