import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema, UserUpdateSchema
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from models import UserModel
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Users", "users", description="Operations on users")


@blp.route("/users/<int:id>")
class Users(MethodView):

    @blp.response(200, UserSchema)
    def get(self, id):
        user = UserModel.query.get_or_404(id)
        return user

    def delete(self, id):
        user = UserModel.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}

    @blp.arguments(UserUpdateSchema)
    @blp.response(200, UserSchema)
    def put(self, updated_user, user_id):
        user = UserModel.query.get(user_id)
        if user:
            user.name = updated_user["name"]
            user.username = updated_user["username"]
            user.password = updated_user["password"]
            user.age = updated_user["age"]
            user.type = updated_user["type"]
            user.gender = updated_user["gender"]
            user.contact = updated_user["contact"]
        # else:
        #     user = UserModel(id=id, **updated_user)    
        
        db.session.add(user)
        db.session.commit()

@blp.route("/users")
class UsersList(MethodView):

    @blp.response(200, UserSchema(many=True)) 
    def get(self):
      return UserModel.query.all()
    
    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, new_user):
        user = UserModel(
            name = new_user["name"],
            username= new_user["username"],
            password= pbkdf2_sha256.hash(new_user["password"]), 
            age = new_user["age"],
            gender=new_user["gender"],
            type=new_user["type"],
            contact=new_user["contact"]
            )
        print(user)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message= "A user with same name exists")    
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting user")

        return {"message", "User created successfully"} 
