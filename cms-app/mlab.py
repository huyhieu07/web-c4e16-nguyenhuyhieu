import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds249798.mlab.com:49798/muadongkhonglanh
# mongodb://<dbuser>:<dbpassword>@ds237979.mlab.com:37979/cms_app

host = "ds237979.mlab.com"
port = 37979
db_name = "cms_app"
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
