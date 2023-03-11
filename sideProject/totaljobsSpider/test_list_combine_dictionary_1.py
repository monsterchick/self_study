list = [
    {"a1":"aaa111", "a2":"aaa222", "a3":"aaa333"},
    {"b1":"bbb333", "b2":"bbb333", "b3":"bbb333"},
    {"c1":"ccc111", "c2":"ccc222", "c3":"ccc333"}]

print(list[0])
print(list[1])
print(list[2])
print("====================")
print(list[0]["a2"])
print(list[1]["b3"])
print(list[2]["c1"])
print("====================")
print(list[0]["a1"])
print(list[0]["a2"])
print(list[0]["a3"])
print(list[1]["b1"])
print(list[1]["b2"])
print(list[1]["b3"])
print(list[2]["c1"])
print(list[2]["c2"])
print(list[2]["c3"])
print("====================")
print(list[0].keys())