from hashlib import md5
from DataBase import models
import time
from FoodForAll.settings import DEFAULT_AVATAR

def gen_uid(seq=""):
    id = md5((str(time.time()) + seq).encode("utf-8")).hexdigest()
    if models.User.objects.filter(uid=id):
        id = gen_uid(seq=seq)
    return id

def create_user(mail, password, type, region, name="", avatar=DEFAULT_AVATAR):
    id = gen_uid(seq=mail)
    if name == "":
        name = mail
    user_info = {"uid": id,
    "mail": mail,
    "password": password,
    "name": name,
    "avatar": avatar,
    "type": type,
    "region": region,
    "project": "",
    "regis_time": int(time.time()),
    "last_login_time": int(time.time()),
    "donate_history": "",
    "share_mail_history": ""}
    models.User.objects.create(**user_info)
    return user_info