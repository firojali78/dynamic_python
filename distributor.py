import os
from flask import Flask,jsonify,request,render_template,redirect,url_for
from fetch_item_list import fetch_item_list, fetch_catagory

app = Flask(__name__,template_folder='templates')

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('index.html')

@app.route('/create_so', methods = ['POST', 'GET'])
def create_so():
    list_user = fetch_catagory()
    return render_template('create_sale_order.html', languages=list_user)

@app.route('/category',methods=['POST'])
def submitcateg():
    if request.method == 'POST':
        input_json = request.form.get("category")
        input_json = input_json.split("~")[0]
        print(input_json)
        list_user = fetch_item_list(input_json)
        print(list_user)
        return render_template('create_sale_order.html', languages=list_user)



app.config['DEBUG']= True
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True, port = 6262)