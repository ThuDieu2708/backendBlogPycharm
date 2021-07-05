
from flask import Flask , request, jsonify,abort
import  dbapidemo.venv.DB.Controllers as Controlers
from flask_cors import CORS
import json
from werkzeug.utils import secure_filename
import simplejson as json
import os
app = Flask(__name__)
cors = CORS(app)

controllers = Controlers.SQL()
controllers.connectDB()

UPLOAD_PATH = 'C:\\Users\\Thu Dieu\\CongNgheWeb\\reactjs\\Blog\\frontend\\public\\images'
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.jpeg','.jfif']
app.config['UPLOAD_PATH'] = UPLOAD_PATH


@app.route('/homepage' , methods=["GET"])
def get_homepage():
    lists = controllers.getHomePage()
    res = json.dumps(lists)
    return res,200

@app.route('/detail-home/<id>')
def get_detail_home(id):
    lists = controllers.getDetailHome(id)
    res = json.dumps(lists)
    return res,200

@app.route('/products-cook')
def get_products_cook():
    listCook = {}
    lists = controllers.getProduts()
    res = json.dumps(lists)
    return res,200

@app.route('/detail-cook/<id>')
def get_detail_cook(id):
    listCook = {}
    lists = controllers.getDetail(id)
    res = json.dumps(lists)
    return res,200

@app.route('/products-cultural')
def get_products_cultural():
    lists = controllers.getProdutsVanHoa()
    res = json.dumps(lists)
    return res,200

@app.route('/detail-cultural/<id>')
def get_detail_cultural(id):
    lists = controllers.getDetailCultural(id)
    res = json.dumps(lists)
    return res,200

@app.route('/login' ,methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(username)
    print(password)
    lists = controllers.getListAcount(username, password)
    res = json.dumps(lists)

    if lists:
        return res,200
    return 'fail', 500

@app.route('/checkinfo' ,methods=['GET', 'POST'])
def get_account():
    if request.method == 'POST':
        print("->" , json.dumps(controllers.getListAcount(request.get_json())))
        return json.dumps(controllers.getListAcount(request.get_json()))
    return "fail check info"

@app.route('/checkID' ,methods=['POST'])
def get_ID():
    username = request.form['username']
    id = controllers.getID(username)
    if id != -1:
        return {
            'id': id
        }, 200
    return'fail', 500

@app.route('/adduser' , methods=['GET', 'POST'])
def save_accountUser():
    try:
        item = {}
        if request.method  == 'POST':
            print(request.get_json())
            item["tk"] = request.get_json()["email"]
            item["mk"] = request.get_json()["password"]
            controllers.saveRegister(item)
            return "ok"
        else:
            return "fail"
    except :
        return "fail2"

@app.route('/addAmThuc' , methods=['GET', 'POST'])
def save_AmThuc():
    id = request.form['id']
    tenmon = request.form['tenmon']
    nguyenlieu = request.form['nguyenlieu']
    soche = request.form['soche']
    author = request.form['author']

    try:
        state = request.form['state']
    except:
        state = 0

    try:
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    except:
        filename = request.form['file']
    controllers.saveAmThuc2(id, nguyenlieu, tenmon, soche, filename, author, state)
    return "ok"


@app.route('/addVanHoa' , methods=['POST'])
def save_VanHoa():
    id = request.form['id']
    tenbai = request.form['tenbai']
    noidung = request.form['noidung']
    author = request.form['author']
    try:
        state = request.form['state']
    except:
        state = 0
    try:
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    except:
        filename = request.form['file']
    controllers.saveVanHoa(id, tenbai, noidung, filename, author, state)
    return "ok"

@app.route('/listByName' , methods=['POST'])
def getListByName():
    try:
        if request.method  == 'POST':

            return json.dumps(controllers.getListByAuthor(request.get_json()))
        else:
            return "fail getListByName"
    except :
        return "fail2 getListByName"


@app.route('/deleteId' , methods=['POST'])
def deleteId():
    try:
        if request.method  == 'POST':
            controllers.deleteId(request.get_json())
            return "ok"
        else:
            return "fail deleteId"
    except :
        return "fail2 deleteId"

# -------------bài đăng user---------------
@app.route('/userCook' , methods=['GET'])
def userCoook():
    lists = controllers.getUser_Cook()
    res = json.dumps(lists)
    return res, 200

@app.route('/userCultural' , methods=['GET'])
def userCultural():
    lists = controllers.getUser_Cultural()
    res = json.dumps(lists)
    return res, 200


if __name__ == '__main__':
    app.run(debug=True)

