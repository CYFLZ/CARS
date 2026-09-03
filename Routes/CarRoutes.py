from flask import Blueprint,jsonify
# from Controllers.CarsController import cntListCars
from Services.CarService import car_service

car_bp = Blueprint('cars_bp', __name__)

@car_bp.route('/', methods=['GET'])
def listCars():
    x = car_service.listCars()
    return jsonify(x), 200  
 

@car_bp.route('/create', methods=['POST'])
def createCar():
    return ""

@car_bp.route('/edit', methods=['PUT'])
def updateCar():
    return ""

@car_bp.route('/delete', methods=['DELETE'])
def deleteCar():
    return ""


 