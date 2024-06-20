import requests

res =requests.po("http://127.0.0.1:8000/items/", json={"name":"I phone","des":"Smartphone",
  "price":59999
})
print("Text",res.text)
print("JSON",res.json())
print("Status Code",res.status_code)