dic = {}

val_a = "aaa"
val_b = "bbb"
val_c = "ccc"
num1 = 1
num2 = 2
num3 = 3

dic[val_a] = val_c
print(dic)

# add key
dic["key_a"] = val_a
dic["key_b"] = val_b
dic["key_c"] = val_c
print(dic)

# remove key
del dic["aaa"]
print(dic)

# add a key which already exists
dic["key_a"] = "add key again"
print(dic)  # the value will be updated




# https://stackabuse.com/python-how-to-add-keys-to-dictionary/
#how to make a new key