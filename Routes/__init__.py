# from .UserRoutes import us_bp
# from .CarRoutes import car_bp
from .CarRoutes import car_bp


def load_routes(app):
    # app.register_blueprint(us_bp, url_prefix='/users')
    app.register_blueprint(car_bp, url_prefix='/cars')
    # app.register_blueprint(car_bp, url_prefix='/cars')



# http://120.0.0.0/cars/create
# http://120.0.0.0/user/create
# http://120.0.0.0/cars/edit
# http://120.0.0.0/user/edit
