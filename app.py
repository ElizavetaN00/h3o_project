from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Team(Resource):  # Новый класс для корня
    def get(self):
        return 'H3O Project'

api.add_resource(Team, "/")

if __name__ == '__main__':
    app.run('0.0.0.0','5002')
