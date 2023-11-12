from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

import os

buildBranch = "main"
buildPath = "/home/ubuntu/chat"
buildCommand = "cd " + buildPath + \
    " && git stash && git pull && git pull origin " + buildBranch

app = Flask(__name__)
api = Api(app)


class Webhook(Resource):
    def post(self):
        os.system(buildCommand)
        return jsonify({"message": "Build Complete"})


api.add_resource(Webhook, '/deploy')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, debug=True)
