# REST - representational State Transfer
# API - application programming interface
# status 200 - all is ok, nothing crash

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"augustine": ["hello augustine"],
         "no name": [" hello stranger"]}


# names = ["augustine", "firdaus"]

class HelloWorld(Resource):
    def get(self, name):
        return names[name]


# class HelloWorld(Resource):
#     def get(self, name):
#         for i in names:
#             if name == "augustine":
#             print("Hello augustine")
#         else:
#             print("Hello stranger")

api.add_resource(HelloWorld, "/helloworld/<string:name>")

# to change port number
if __name__ == "__main__":
    app.run(port=8087)
    app.run(debug=True)
