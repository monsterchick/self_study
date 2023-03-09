import requests
import re
a = "https://openmoji.org/"
url = "https://openmoji.org/library/"
response = requests.get(url)
text = response.text
# print(text)
image = re.findall('<img class="emoji-variant-color lazyload astro-JSGNIHCK loaded".*? alt=',text)
print(image)
for i in text:
    print(i)

# '<img class="emoji-variant-color \
# lazyload astro-JSGNIHCK loaded __web-inspector-hide-shortcut__" \
# data-src="/data/color/svg/1F4A2.svg" alt="&quot;anger symbol&quot;-emoji" \
# data-ll-status="loaded" src="/data/color/svg/1F4A2.svg">')