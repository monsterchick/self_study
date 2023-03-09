import os

currentPath = os.getcwd()
print("current working path:", currentPath)

desktopPath = os.path.join(os.path.expanduser("~"), "Desktop")  # chagne working directory
print("get path of desktop:", desktopPath)

currentPath = desktopPath
os.chdir(currentPath)
print("working path after changed:", currentPath)


# to check if folder "image" not exists in Desktop
# if True, make a new folder called "image"
# if False, prompt a message
def mkdir(path):
    if not os.path.isdir("image"):
        # folder "image" not exists
        os.makedirs(path)
        print("new folder created successfully!")
    else:
        print("folder existed!")


pathOfFolder = currentPath + "/image"
# print(pathOfFolder)
mkdir(pathOfFolder)
