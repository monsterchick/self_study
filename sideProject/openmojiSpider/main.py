import os
import requests
import re


def mkdir(path):
    # go to Desktop directory
    os.chdir(os.path.join(os.path.expanduser("~"), "Desktop"))
    # check if folder exists, if not, make one. if exists, prompt a message
    if not os.path.isdir("image"):
        os.makedirs(path)  # make a folder called image
        print("folder created successfully!")
    else:
        print("folder existed!")
        pass


def download_image(image, image_name):
    # download images with svg format
    print("downloading {img}...".format(img=image_name))
    response_image = requests.get(image)
    with open(os.getcwd() + "/image" + "/" + image_name, 'wb') as file:  # open the path of image file
        file.write(response_image.content)
    file.close()


def work_on_sub_url(url):
    response = requests.get(url)
    text = response.text
    img_src_list = re.findall(r'id="downloadPNG" href=".*?" download', text)
    for imgSrc in img_src_list:
        img_link = "https://openmoji.org/" + imgSrc.split('href="/')[1].split('\"')[0].replace("amp;", "")
        img_name = re.findall(r'<h1 class="astro-3TWLDLUD">.*?</h1>', text)[0].split(">")[1].split("<")[0] + "_" + \
                   img_link.split("=")[3] + ".png"
        download_image(img_link, img_name)


url = "https://openmoji.org/library/"
response = requests.get(url)
text = response.text
src_list = re.findall(r'<a class="emojiDetailsLink astro-JSGNIHCK" href=".*?">', text)

mkdir("/Users/monstermac/Desktop/image")
for src in src_list:
    # get path of image
    src_clip = src.split("\"")[3].split("/")[2]
    # get main url
    main_url = url + src_clip
    work_on_sub_url(main_url)

print("all done. Congratulations!")

