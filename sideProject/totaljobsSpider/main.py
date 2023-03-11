import json
import os
import re
import requests

index = 0
dictionary = {}
key_rd = "release_date"
key_ca = "company_address"
key_jp = "job_position"


# get url with searching keywords
def get_page(job, location):
    fir_key = "/" + job.replace(" ", "") + "/"
    sec_key = location
    url = "https://www.totaljobs.com/jobs{fir_key}in-{sec_key}?radius=10&searchOrigin=Resultlist_top-search".format(
        fir_key=fir_key, sec_key=sec_key)
    # print(url)
    return url


def headers():
    # pretending to access as a browser
    headers = {"content-type": "text/html; charset=utf-8",
               "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    return headers


def add_index():
    global index
    index += 1


def save_to_json_file():
    json_object = json.dumps(dictionary, indent=4)    # convert type dict to str
    path = os.getcwd() + "/download.json"
    with open(path, "w") as fp:
        fp.write(json_object)
    print("save successfully")


def make_keys_into_dictionary(key, value):
    global index
    global dictionary
    dictionary[index] = {key: value}
    add_index()  # index +1 each call


def dictionary_update(key, value):
    global index
    dictionary[index].update({key: value})
    add_index()
    # print(dictionary)


def clip_release_date(clip_list):
    for i in clip_list:
        release_date = i.split('</path></svg></span>')[1].split('<')[0]
        # print(release_date)
        make_keys_into_dictionary(key_rd, release_date)
    global index
    index = 0


def clip_company_address(clip_list):
    # global key_ca
    for i in clip_list:
        company_address = i
        # print("company address: {company_address}".format(company_address=company_address))
        dictionary_update(key_ca, company_address)
    global index
    index = 0


def clip_job_position(clip_list):
    for i in clip_list:
        position = i.split('>')[1].split('<')[0]
        # print(f"job position: {position}".format(position=position))
        dictionary_update(key_jp, position)
    global index
    index = 0


job_search = input("Please enter a Job title/skill/company: ")
location_search = input("Please enter a location(Town/city/postcode): ")

url = get_page(job=job_search, location=location_search)
response = requests.get(url, headers=headers())
text = response.text

position_list = re.findall('<h2 class="sc-fzqMAW krdChg">.*?</h2>', text)  # job title list
company_address_list = re.findall('<li data-at="job-item-location" class="sc-fznXWL jExrPv">.*?</span>(.*?)</li>', text)  # address list
release_date_list = re.findall('<li data-at="job-item-timeago" class="sc-fznXWL jwFffy">.*?</li>', text)  # position list
clip_release_date(release_date_list)
clip_company_address(company_address_list)
clip_job_position(position_list)
save_to_json_file()
