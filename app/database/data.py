import json


class Users:
    with open("app/database/fake_users_db.json") as f:
        data = json.load(f)
