from tinydb import TinyDB, Query
from telebot.types import Message

def find_user(msg: Message):
    id = msg.from_user.id
    db = TinyDB("db/users.json")
    user = Query()
    return db.search(user.id==id)

def add_user(msg: Message):
    if not find_user(msg):
        db = TinyDB("db/users.json")
        db.insert({"id":msg.from_user.id, "date":msg.date})
def get_all_users():
    db = TinyDB("db/users.json")
    return db.all()

def add_message(msg: Message, ok):
    db = TinyDB("db/messages.json")
    db.insert({"msg_id": msg.from_user.id, "msg": msg.text, "date": msg.date, "ok":ok})
