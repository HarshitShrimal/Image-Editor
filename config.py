# By @TroJanzHEX


import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6033337410:AAFjc-t50kayZJzl_HoaNqNZXxc5-jI0Yyc")

    APP_ID = int(os.environ.get("APP_ID", 26351529))

    API_HASH = os.environ.get("API_HASH", "e2076ce1ff7824e6511838ca20213bed")

    # Get this api from https://www.remove.bg/b/background-removal-api
    RemoveBG_API = os.environ.get("RemoveBG_API", "Rt8XgF9Lw3hEeRuWSFF4D4EY")
