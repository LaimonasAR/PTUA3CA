import requests


def get_servers(*args):
    for arg in args:
        r = requests.get(arg, timeout=3)
        response = r.headers
        # print(response)
        # for server in response.items():
        server_name = response["Server"]
        print(f"{arg}       {server_name}")


get_servers(
    "http://www.delfi.lt",
    "http://www.one.lt",
    "https://www.15min.lt/",
    "https://www.lrytas.lt/",
)
