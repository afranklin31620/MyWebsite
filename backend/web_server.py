from flask import Flask , request , jsonify
from flask_cors import CORS
from mail_server import generate_verification_code , send_verification_code
vcode = 0
my_app = Flask(__name__)
CORS(app=my_app, 
     resources={
         r"/*": {
             "origins": ["http://127.0.0.1:5500",
                         "http://localhost:5500"
                         ]
                }
               }
    )
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
    global vcode
    vcode = generate_verification_code()
    send_verification_code(vcode,email)
    return {"msg":f"Confirmation email sent to {email}"}

@my_app.route("/verify_code",methods=["POST"])
def verify():
    form_data = request.get_json()
    print(form_data)
    auth_code = form_data['validation_code']
    if auth_code.isdigit():
        if int(auth_code) == vcode:
            return {"msg":"Codes match"}
        return {"msg":f"Codes don't match current code {vcode} attempted code : {auth_code}"}
    return {"msg":"Invalid Code"}
@my_app.route("/")
def home():
    return f"Verification Code {vcode}"

#TODO add email sending function
if __name__ == "__main__":
    my_app.run(host='0.0.0.0',port=1234,debug=True)