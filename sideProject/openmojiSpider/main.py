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


def downloadImage(image, imageName):
    # download images with svg format
    print("downloading {img}...".format(img=imageName))
    resImage = requests.get(image)
    with open(os.getcwd() + "/image" + "/" + imageName, 'wb') as file:  # open the path of image file
        file.write(resImage.content)
    file.close()


def workOnSubUrl(mainUrl):
    response = requests.get(mainUrl)
    text = response.text
    imgSrcList = re.findall(r'id="downloadPNG" href=".*?" download', text)
    for imgSrc in imgSrcList:
        imgLink = "https://openmoji.org/" + imgSrc.split('href="/')[1].split('\"')[0].replace("amp;", "")
        imgName = re.findall(r'<h1 class="astro-3TWLDLUD">.*?</h1>', text)[0].split(">")[1].split("<")[0] + "_" + \
                  imgLink.split("=")[3] + ".png"
        downloadImage(imgLink, imgName)


url = "https://openmoji.org/library/"
response = requests.get(url)
text = response.text
srcList = re.findall(r'<a class="emojiDetailsLink astro-JSGNIHCK" href=".*?">', text)

mkdir("/Users/monstermac/Desktop/image")
for src in srcList:
    # get path of image
    srcClip = src.split("\"")[3].split("/")[2]
    # get main url
    mainUrl = url + srcClip
    workOnSubUrl(mainUrl)

print("all done. Congratulations!")
