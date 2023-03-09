from datetime import datetime
from marshmallow import Schema, fields


class Room(object):
    def __init__(self, user_id, room_name, date, start_time, end_time):
        self.user_id = user_id
        self.room_name = room_name
        self.timestamp = datetime.now()
        self.date = date
        self.start_time = start_time
        self.end_time = end_time


class RoomSchema(Schema):
    user_id = fields.Number()
    room_name = fields.Str()
    timestamp = fields.DateTime()
    date = fields.Date()
    start_time = fields.DateTime()
    end_time = fields.DateTime()


