from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello (Resource):
    def get(self):
        return 'H3O'

api.add_resource(Hello, '/')

if __name__ == '__main__':
    app.run('0.0.0.0','5001')
