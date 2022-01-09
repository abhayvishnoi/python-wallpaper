#change desktop background using python
def change_windows_background(image_path):
    import ctypes
    #absolute path to image
    import os
    # print(os.path.abspath(image_path))
    print(ctypes.windll.user32.SystemParametersInfoW(20, 0,os.path.abspath(image_path) , 0))
    # SPI_SETDESKWALLPAPER = 20 
    # ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path , 0)

#get random wallpaper from reddit
def get_random_wallpaper_from_reddit():
    import requests
    import json
    import random
    reddit_url = "https://www.reddit.com/r/wallpapers/top/.json?sort=top&t=day"
    response = requests.get(reddit_url)
    if response.status_code == 200:
        data = response.json()
        data = data['data']['children']
        data = [x['data']['url'] for x in data]
        return random.choice(data)
    else:
        return "https://www.bing.com/th?id=OHR.RiceBangladesh_EN-US1519717699_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp"
# get_random_wallpaper_from_reddit()
def save_wallpaper():
    import requests
    url = get_random_wallpaper_from_reddit()
    print(url)
    #save wallpaper
    response = requests.get(url)
    with open('wallpaper.jpg', 'wb') as f:
        f.write(response.content)
        f.close()
    return

def save_and_change_wallpaper():
    save_wallpaper()
    change_windows_background('wallpaper.jpg')

#save and change wallpaper every 20 seconds
import time
tts=int(input("Enter time in seconds to change wallpaper: "))
while True:
    save_and_change_wallpaper()
    print('changed wallpaper')
    print(f'sleeping for {tts} seconds')
    time.sleep(tts)

#due to ip restricts we have to use bing default wallpaper reddit will work fine if you 
# increase sleeping time have fun i will give link in description , dont forget to subscribe