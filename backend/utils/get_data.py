import pandas as pd
import re
from datetime import datetime

df = pd.read_excel("waters.xlsx", sheet_name=0)


def get_waters(text):
    text = str(text)
    if text == "nan":
        return []

    result = []
    temp = ""
    in_bracket = False

    for i in range(len(text)):
        if not in_bracket:
            if text[i] == "," or text[i] == "\n":
                result.append(temp)
                temp = ""
                continue

            temp += text[i]
            if text[i] == "(":
                in_bracket = True
                continue

        else:
            temp += text[i]
            if text[i] == ")":
                in_bracket = False
                continue
    result.append(temp)

    result = filter(lambda x: x != "-", result)
    result = map(lambda x: x.strip(), result)
    result = filter(lambda x: len(x) > 0, result)

    return list(result)


def get_address(txt):
    return txt.replace("\n", " ")


def get_name(txt):
    return txt.replace("\n", " ").replace("㈜", " ").replace("(주)", " ").strip()


def get_running(txt):
    if txt == "휴업":
        return False
    else:
        return True


suppliers = []
products = dict()
for row in df.itertuples():
    supplier = {
        "name": get_name(row[3]),
        "address": get_address(row[5]),
        "ceo_name": row[4],
        "intakes": row[11],
        "pipes": row[12],
        "first_permit_datetime": datetime.fromtimestamp(row[10].timestamp()),
        "last_permit_datetime": datetime.fromtimestamp(row[10].timestamp()),
        "is_running": get_running(row[13]),
    }
    suppliers.append(supplier)

    own_products = get_waters(row[7])
    oem_products = get_waters(row[8])

    for product_name in own_products + oem_products:
        if product_name not in products:
            product = {
                "name": product_name,
                "is_oem": False,
                "suppliers": [supplier["name"]],
                "vendor": "",
            }
            products[product_name] = product
        else:
            products[product_name]["suppliers"].append(supplier["name"])

df = pd.read_excel("waters.xlsx", sheet_name=1)
vendors = []
for row in df.itertuples():
    vendor = {
        "name": get_name(row[4]),
        "address": get_address(row[6]),
        "ceo_name": row[5],
        "declare_datetime": row[3],
        "is_running": True,
        "products": get_waters(row[9]),
    }
    vendors.append(vendor)
    for product_name in vendor["products"]:
        if product_name in products:
            products[product_name]["vendor"] = vendor["name"]

# print(suppliers)
# print(products)
# print(vendors)
