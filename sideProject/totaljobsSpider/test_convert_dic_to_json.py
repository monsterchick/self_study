import json

dic = {0:{"a":"A","b":"B"},1:{"c":"C","d":"D"}}
print("original:",dic,"data type:",type(dic))
new_dumps_dic = json.dumps(dic)
print("json dumps:",new_dumps_dic,"data type:",type(new_dumps_dic))
back_to_dic = json.loads(new_dumps_dic)
print("json loads:",back_to_dic,"data type:",type(back_to_dic))


# reference:
# https://blog.csdn.net/sinat_36899414/article/details/77817195
