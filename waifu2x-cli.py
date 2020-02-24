import os
import sys
import shutil
import requests
import cv2
import glob
import json
import wget

input_dir   = sys.argv[1]
output_dir  = "output"

img_list = os.listdir(input_dir)
img_list.sort()

os.chdir(input_dir)
if os.path.isdir(output_dir):
    shutil.rmtree(output_dir, ignore_errors=True)

os.mkdir(output_dir)

i = 0
while i < len(img_list):

    print("\nWorking... "+img_list[i]+"\n")

    r = requests.post(
        "https://api.deepai.org/api/waifu2x",
        files={
            'image': open(img_list[i], 'rb'),
        },
        headers={'api-key': 'api-key:quickstart-QUdJIGlzIGNvbWluZy4uLi4K'} #Replace with your own DeepAI API. 
    )
    data        = json.loads(r.text)    

    if data.get("status"):
        print(data["status"])
        break
    else:
        img_link    = data["output_url"]
        wget.download(img_link, out=output_dir+"/upscaled_"+img_list[i])

    i += 1
