from flask import Flask
from flask_restful import reqparse, Resource, Api
from flask_cors import CORS, cross_origin
from database import db, connection_string
from models import MessageModel

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

api = Api(app)
cors = CORS(app)
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()
    db.session.commit()

class MessageList(Resource):
    def get(self):
        messages = MessageModel.query.all()
        return {'messages': list(message.json() for message in messages)}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('message')

        args = parser.parse_args()
        new_message = MessageModel(args['name'], args['message'])

        db.session.add(new_message)
        db.session.commit()

        return new_message.json(), 201

api.add_resource(MessageList, '/messages')

if __name__ == '__main__':
    app.run(debug=True)
