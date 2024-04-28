from flask import Flask
from db import *
from flask_smorest import Api
# import models
from resources.user import blp as UserBlueprint
from resources.patient import blp as PatientBlueprint
from resources.doctor import blp as DoctorBlueprint
from resources.department import blp as DepartmentBlueprint


def create_app():
    app = Flask(__name__)
    
    URL = "mysql://root:Iloverahul24@localhost"
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Hospital REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{URL}/hospital'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # db.init_app(app)

    api = Api(app)

    app.app_context().push()
    db.init_app(app)
    db.create_all()
    db.session.commit()
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(PatientBlueprint)
    api.register_blueprint(DoctorBlueprint)
    api.register_blueprint(DepartmentBlueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8080, host='0.0.0.0')