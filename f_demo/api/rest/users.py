# import json
from flask import Blueprint, request, make_response, jsonify
import jwt
from datetime import datetime, timedelta
from conf.database import Config
# from functools import wraps

from api.helper.user_crud import (get_all_users, add_a_users, get_single_user,
                                  update_single_user)

USER_BLUEPRINT = Blueprint('user', __name__, url_prefix='/api/')


@USER_BLUEPRINT.route("/user", methods=["GET", "POST"])
def get_users():
    if request.method == "POST":
        data = request.get_json()
        return add_a_users(data)
    return get_all_users()


@USER_BLUEPRINT.route("/user/<int:id>", methods=["GET", "PUT", "PATCH"])
def update_user(id):
    if request.method == "PUT" or request.method == "PATCH":
        data = request.get_json()
        return update_single_user(id, data)
    if request.method == "DELETE":
        pass
    return get_single_user(id)


@USER_BLUEPRINT.route("/login")
def login():
    auth = request.authorization
    print(auth)

    if auth and auth.password == 'password':
        token = jwt.encode({"user": auth.username, "exp": datetime.utcnow() + timedelta(minutes=30)}, Config.SECRET_KEY)
        print(token)
        return jsonify({"token": token})

    return make_response("could not verify", 401, {"WWW-Authenticate": "Basic realm='Login Required'"})


# def token_required(f):
#     @wraps(f)
#     def decorator(*args, **kwargs):
