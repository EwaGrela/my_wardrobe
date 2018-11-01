from flask import Flask, jsonify, Blueprint, request

from wardrobe.model import ClothesManager

interface = ClothesManager()


blueprint = Blueprint("clothes", __name__)

@blueprint.route("/test")
def test():
    return "just a test"

@blueprint.route("/", methods = ["GET", "POST"])
def add_clothing():
    data = request.get_json()
    model = data.get("model")
    info = data.get("info")
    print("info", info)
    interface.add_clothing()
    return "OK"




def clothes():
    if request.method == "POST":
        return add_clothing()
