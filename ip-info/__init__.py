import requests

class IPDataError(Exception):
        errno: int
        strerror: str

class ip():
    ip = "1"
    def __init__(self,ip:str):
        self.ip = ip

    def get_data(self):
        r = requests.get(f"http://ip-api.com/json/{self.ip}").json()
        if r["status"] == "fail":
            raise IPDataError("fail,try again!")
        else:
            self.res = r 
            return r
