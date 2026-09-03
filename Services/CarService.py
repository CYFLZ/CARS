from flask import current_app
from Models.Car import Car
from Models.user import User

class car_service:

    def listCars():
        sql = """SELECT * FROM t_car 
        INNER JOIN t_user ON t_car.CAR_US_ID = T_USER.US_ID
        """
        # la siguiente linea es para ejecutar la consulta sql
        c   = current_app.mysql.connection.cursor() 
        c.execute(sql)
        # la siguiente linea es para obtener los resultados de la consulta sql
        data = c.fetchall()    
        cars_l = []
        for x in data:
            car_data = Car(x[0],x[1],x[2],x[3],x[4],x[5],x[6]).to_dic()
            user_data = User(x[7],x[8],x[9],x[10],x[11],x[12],x[13]).to_dic()  
            car_data["user"] = user_data
            cars_l.append(car_data)

        # cars_l = [ Car(c[0],c[1],c[2],c[3],c[4],c[5],c[6]).to_dic() for c in data ]
        # la siguiente linea es para cerrar la conexion a la base de datos
        c.close()
        return cars_l


   
