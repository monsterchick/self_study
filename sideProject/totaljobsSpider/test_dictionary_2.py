# dic = {
#     0:
#         {"a":"aaa", "a1":"aaa111"},
#     1:
#         {"b":"bbb", "b2":"bbb222"}
# }
# print(dic[0]["a1"])
import os

dict = {}
print(dict)
index = 0
date = '2022-2-2'
position = 'CEO'
address = 'bh88ng'
for i in range(10):
    dict[index] = {'release_date':date, 'company_address':address, 'job_position':position}
    print(dict[index]["company_address"])
    index += 1
print(dict)

# update subkey into a dictionary
dic1 = {0:{"a":"A","b":"B"},1:{"c":"C","d":"D"}}
dic1[0].update({"test":"TEST"})
print(dic1)
# reference:
# https://www.runoob.com/python/att-dictionary-update.html
# update subkey in dic
print(os.getcwd())