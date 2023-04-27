import requests


def download_cats(count):
    for i in range(0, count):
        r = requests.get("https://cataas.com/cat")
        with open(f"cat_pic{i}.jpg", "wb") as f:
            f.write(r.content)


download_cats(3)
