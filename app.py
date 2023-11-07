from flask import Flask, request
import db
import query

conn = db.connect()
app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register_user():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    dob = request.form.get("dob")
    phone = request.form.get("phone")
    print([name, email, password, dob, phone])
    response = query.register_user(conn, name, email, password, dob, phone)
    return response

@app.route("/users", methods=["GET"])
def get_users():
    return query.get_users(conn)

@app.route("/change-password/<id>", methods=["PATCH"])
def change_password(id):
    new_password = request.form.get("new_password")
    if (new_password == None):
        return {"Please input new password"}
    return query.change_password(conn, id, new_password)

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    return query.login(conn, email, password)


