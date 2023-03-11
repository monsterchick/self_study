def people(key1, key2):
    people = {
        "John": {"address": "bh8112", "mobile": "12342", "gender": "male"},
        "Kitty": {"address": "bh7s6d", "mobile": "372463", "gender": "female"},
        "Leo": {"address": "j3b4k4", "mobile": "5678637", "gender": "male"},
        "Jim": {"address": "ggf8ff", "mobile": "252525423", "gender": "female"},
        "Cat": {"address": "ng876d", "mobile": "111111", "gender": "female"},
        "Marry": {"address": "sbb767", "mobile": "123123", "gender": "male"},
    }
    name_list = people.keys()
    value = people[key1][key2]  # value from input
    # print(name_list)    # this is a list
    info_dic = people[key1]    # dictionary of information in person
    print(info_dic)
    print(type(info_dic))   # dict
    # if people.keys() in key1 :
    #     print('true')
    # else:
    #     print('false')

    try:
        if key1 in name_list:
            print("{k1}'s {k2} is {v}.".format(k1=key1, k2=key2, v=value))
        else:
            print("Could not find information")
    except KeyError:
        print("Could not find information")