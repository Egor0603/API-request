import requests as req


arr_18reg = []
arr_of_types = []

# запрос к API  и его обработка, как json
r = req.get("https://api.kontur.ru/dc.contacts/v1/cus")
r = r.json()

# Фильтр значений с 18 регионом
for i in r["cus"]:
    if i["region"] == "18":
        arr_18reg.append(i)
        if i["type"] not in arr_of_types:
            arr_of_types.append(i["type"])


