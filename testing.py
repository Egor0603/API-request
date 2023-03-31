import requests as req


arr_18reg = []
arr_of_types = []
arr_for_table = []

# запрос к API  и его обработка, как json
r = req.get("https://api.kontur.ru/dc.contacts/v1/cus")
r = r.json()

# Фильтр значений с 18 регионом
for i in r["cus"]:
    if i["region"] == "18":
        arr_18reg.append(i)
        if i["type"] not in arr_of_types:
            arr_of_types.append(i["type"])

# Создание списка списков с необходимыми для таблицы значениями
for i in arr_of_types:
    for j in range(len(arr_18reg)):
        inner_list = []
        if arr_18reg[j]["type"] == i:
            inner_list.append(arr_18reg[j]["type"])
            inner_list.append(arr_18reg[j]["code"])
            inner_list.append(arr_18reg[j]["name"])
            if arr_18reg[j]["soun"]:
                inner_list.append(arr_18reg[j]["soun"]["inn"])
            else:
                inner_list.append(" ")

            arr_for_table.append(inner_list)

