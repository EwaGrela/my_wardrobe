from flask import Flask, jsonify, Blueprint, request

from wardrobe.model import WardrobeManager
from wardrobe.model import DataBaseConnector

connector = DataBaseConnector()
interface = WardrobeManager(connector)


blueprint = Blueprint("clothes", __name__)



@blueprint.route("/", methods = ["GET", "POST", "DELETE"])
def clothes():
    if request.method == "POST":
        return add_clothing()
    elif request.method == "GET":
        return show_clothes()
    elif request.method == "DELETE":
        return delete_clothing()


def add_clothing():
    data = request.get_json()
    model = data.get("model")
    name = data.get("name")
    info = data.get("info")
    interface.create_clothing(model, name, info)
    return "OK"

def show_clothes():
    clothes = interface.show_clothes()
    return jsonify(clothes)

def delete_clothing():
    cloth_id = request.args.get("id")
    to_delete = interface.delete_clothing(cloth_id)
    return jsonify(to_delete)


@blueprint.route("/garments", methods=["GET", "POST"])
def garments():
    if request.method == "GET":
        return get_garments()
    elif request.method == "POST":
        return post_garment()

def get_garments():
    garments = interface.show_garments()
    garments = [garment.to_json() for garment in garments]
    return jsonify(garments)

def post_garment():
    data = request.get_json()
    name = data.get("name")
    interface.create_garment(name)
    return "OK"



        

