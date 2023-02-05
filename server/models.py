from database import db

import json

class MessageModel(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    user_name = db.Column(db.String(80))
    message = db.Column(db.String(500))

    def __init__(self, name, message):
        self.user_name = name
        self.message = message

    def json(self):
        return json.dumps(
            {
                "id": self.id,
                "created_at": self.created_at,
                "user_name": self.user_name,
                "message": self.message,
            },
            default=str
        )
