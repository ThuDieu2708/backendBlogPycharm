
from flask import Flask , request
import DB.Controllers as Controlers
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

controllers = Controlers.SQL()
controllers.connectDB()

@app.route('/' ,methods=['GET', 'POST'])
def get_accountAdmin():
	listAcount = {}
	lists = controllers.getListAcount()
	print(lists)
	for item in lists:
		listAcount[item[0]] = item[1]
	res = json.dumps(listAcount)
	return res

@app.route('/adduser' , methods=['GET', 'POST'])
def save_accountUser():
	try:
		item = {}
		if request.method  == 'POST':
			print(request.get_json())
			item["tk"] = request.get_json()["email"]
			item["mk"] = request.get_json()["password"]
			controllers.saveRegister(item , "accountuser")
			return request.get_json()
		else:
			return "404"
	except :
		return "404"

if __name__ == '__main__':
	app.run();