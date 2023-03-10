import os
import requests
import re

count = 1
fontUrl = "https://openmoji.org"
url = "https://openmoji.org/library/"
response = requests.get(url)
text = response.text
srcList = re.findall(r'data\Wsrc="/.*?/.*?/.*?/.*?.svg" alt=".*?"', text)

for src in srcList:
    # get path of image
    srcClip = src.split("\"")[1]
    image = fontUrl + srcClip
    # get name of image
    nameClip = src.split("=")[2].split(";")[1]
    # get code of image
    codeClip = src.split(".")[0].split("/")[4]
    # print(codeClip)
    # print(os.path.join(os.path.expanduser("~"), "Desktop/image"))
    imageName = "{num}_{nme}_{cd}.svg".format(num=count, nme=nameClip, cd=codeClip)
    # print(imageName)ttt
    count += 1

    # go to Desktop directory
    os.chdir(os.path.join(os.path.expanduser("~"), "Desktop"))
    # check if folder exists, if not, make one. if exists, prompt a message
    if not os.path.isdir("image"):
        os.makedirs(os.getcwd() + "/image")  # make a folder called image
        print("folder created successfully!")
    else:
        print("folder existed!")
        pass

    # download images with svg format
    print("downloading {img}...".format(img=imageName))
    resImage = requests.get(image)
    with open(os.getcwd() + "/image" + "/" + imageName, 'wb') as file:  # open the path of image file
        file.write(resImage.content)
    file.close()
