import requests

url = "https://raw.githubusercontent.com/susanli2016/NLP-with-Python/master/data/amazon_alexa.tsv"
r = requests.get(url)
if r.status_code == 200:
    with open("amazon_alexa.tsv", "wb") as f:
        f.write(r.content)
    print("Descarga exitosa")
else:
    print(f"Error {r.status_code}")
