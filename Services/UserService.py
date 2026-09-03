from flask import current_app
from Models.user import User

class user_service:

    def listUser():
        sql = "SELECT * FROM T_USER"
        # la siguiente linea es para ejecutar la consulta sql
        c   = current_app.mysql.connection.cursor() 
        c.execute(sql)
        # la siguiente linea es para obtener los resultados de la consulta sql
        data = c.fetchall()      

        users_l = [ User(u[0],u[1],u[2],u[3],u[4],u[5],u[6]).to_dic() for u in data ]
        # la siguiente linea es para cerrar la conexion a la base de datos
        c.close()
        return users_l

    def addUser(nombre, apellido, tipo_doc, documento, fecha_nac):
        c   = current_app.mysql.connection.cursor() 
        sql = f"""
                INSERT INTO T_USER (US_FIRST_NAME, US_LAST_NAME, US_TYPE_DOC, US_DOCUMENT, US_DATE_BIRTH)
                VALUES (%s, %s, %s, %s, %s)
            """
        c.execute(sql,(nombre, apellido, tipo_doc, documento, fecha_nac))
        current_app.mysql.connection.commit()
        c.close()
        return f"User {nombre} {apellido} added successfully."

    def upUser():
        pass

    def delUser():
        pass

    def searchByDoc(documento):
        pass
