from flask import jsonify, request
from Services.UserService import user_service

class user_controller:
    def listUsers():
        data = user_service.listUser()
        return jsonify(data), 200


    def addUser():
        # data obtiene el cuerpo de la peticion 
        data = request.get_json(silent=True)
        # Se valida :
        # {} -> cuerpo json vacio -> 400
        # null -> 400
        # sin body ->400
        if not data:
            return jsonify({"mensaje":
                            "El cuerpo de la peticion no debe estar vacio o esta mal Formateado"}), 400

        campos_r = ["nombre","apellido","tipo_doc","documento","fecha_nac"]

        campos_f = [ x  for x in campos_r  if x not in data]
        if len(campos_f) > 0:
            return jsonify({"campos": f"campos faltantes {campos_f}"}), 400

        # validar que no esten vacios
    
        nombre      =data["nombre"]
        apellido    =data["apellido"]
        tipo_doc    =data["tipo_doc"]
        documento   =data["documento"]
        fecha_nac   =data["fecha_nac"]


        x = user_service.addUser(nombre, apellido, tipo_doc, documento, fecha_nac)
        return jsonify({"message": x}), 201

# blueprint en python
# httP://MISERVIDOR/USER/LISTAR
# httP://MISERVIDOR/USER/CREAR