import os
from datetime import date, datetime
from flask import Flask, jsonify, request, render_template

from room.model.room import Room, RoomSchema
from room.model.room_type import RoomType


app = Flask(__name__, template_folder=os.path.abspath("templates"))

ROOM = [
    Room(2, RoomType.ABERDEEN.value,
         date(2023, 3, 9),
         datetime(2023, 3, 9, hour=10, minute=30, second=0),
         datetime(2023, 3, 9, hour=11, minute=30, second=0)),
    Room(5, RoomType.STANLEY.value,
         date(2023, 3, 9),
         datetime(2023, 3, 9, hour=12, minute=30, second=0),
         datetime(2023, 3, 9, hour=14, minute=30, second=0)),
    Room(5, RoomType.ABERDEEN.value,
         date(2023, 3, 9),
         datetime(2023, 3, 9, hour=14, minute=30, second=0),
         datetime(2023, 3, 9, hour=16, minute=00, second=0))
]


@app.route("/")
def home():
    return render_template("index.html", data=ROOM)


@app.route("/rooms")
def get_rooms():
    schema = RoomSchema(many=True)
    room_name = request.args.get("room_name")
    date = request.args.get("date")
    data = [room for room in ROOM if room.room_name == room_name.upper()] if room_name else ROOM
    data = [room for room in data if room.date.isoformat() == date] if date else data
    rooms = schema.dump(data)
    return jsonify(rooms)


@app.route("/rooms", methods=["POST"])
def post_room():
    room = RoomSchema().load(request.get_json())
    ROOM.append(room)
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
