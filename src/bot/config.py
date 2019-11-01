import json
import typing


class Config:
    STREAM_URL: str
    TOKEN: str
    ADMIN: typing.List[int]
    TIMEOUT: int

    def __init__(self, config_path: str = "config.json"):
        config = json.load(open(config_path, "r"))

        self.ADMIN = config["admin_id"]
        self.TOKEN = config["token"]

        self.STREAM_URL = "http://" + \
                          config["server"]["listen_host"] + ":" + \
                          str(config["server"]["listen_port"]) + "/watch/?mid={}"

        self.TIMEOUT = config["bot"]["upnp_scan_timeout"]