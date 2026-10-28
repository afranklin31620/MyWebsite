from flask import Flask , request , jsonify
from flask_cors import CORS

my_app = Flask(__name__)
CORS(app=my_app, origins=["http://127.0.0.1:5500"])

@my_app.route("/login",methods=["POST"])
def login():
    form_data = request.get_json()
    print(form_data)
    if form_data['username'].lower() != "afranklin31520":
        return jsonify(
            {'msg':'username/password incorrect'}
        )
    return {
        "msg":f"Hello {form_data["username"]}"
        }

@my_app.route("/create_account",methods=["POST"])
def create_account():
    form_data = request.get_json()
    email = form_data['email']
    return {"msg":f"Confirmation email sent to {email}"}

@my_app.route("/")
def home():
    return "Hello World"

#TODO add email sending function
if __name__ == "__main__":
    my_app.run(host='0.0.0.0',port=1234,debug=True)