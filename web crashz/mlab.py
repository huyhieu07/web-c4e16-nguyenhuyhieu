import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds129532.mlab.com:29532/muadongkhonglanh

host = "ds129532.mlab.com"
port = 29532
db_name = "muadongkhonglanh"
user_name = "admin007"
password = "12345678"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
