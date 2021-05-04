import pyrebase

config = {
    "apiKey": "AIzaSyD4n6xa9qO3BMDvU_-BckiUh0WoxbcPm1w",
    "authDomain": "societydetails-d0e31.firebaseapp.com",
    "databaseURL": "https://societydetails-d0e31-default-rtdb.firebaseio.com",
    "projectId": "societydetails-d0e31",
    "storageBucket": "societydetails-d0e31.appspot.com",
    "messagingSenderId": "763436702669",
    "appId": "1:763436702669:web:0c9f42d4f936544d078284",
    "measurementId": "G-LLHLJ7CRDB"

}

firebase = pyrebase.initialize_app(config)

auth=firebase.auth()
db = firebase.database()

'''
db.child("names").push({"name":"Manasvini"}) #to create and push value
db.child("names").child("names").update({"name":"Manasvini"}) #to update the previous value with a new one
users = db.child("names").child("names").get() #to get child in child
print(users.key())

db.child("names").remove() #to remove root if we use child("names").child("names").remove() it removes child of child
'''

from flask import *

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def basic():
	if request.method=='POST':
		if request.form['submit'] == 'add':
			name=request.form['name']
			phone=request.form['phone']
			email=request.form['email']
			block=request.form['block']
			area=request.form['area']
			db.child("details").push("user").child("name").set(name)
			db.child("details").child("phone").set(phone)
			db.child("details").child("email").set(email)
			db.child("details").child("block").set(block)
			db.child("details").child("area").set(area)
			detail = db.child("details").get()
			to = detail.val()
			return render_template('main.html',t=to.values())
		elif request.form['submit'] == 'delete':
			db.child("details").remove()
		return render_template('main.html')
	return render_template('main.html')

if __name__=='__main__':
	app.run(debug=True)

