import time
from datetime import datetime as dt

hosts_temp= r"C:\Python\Website Blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com", 'www.youtube.com', 'youtube.com']

while True:
    if dt(dt.now().year, dt.now().month,dt.now().day,4) < dt.now() < dt(dt.now().year, dt.now().month,dt.now().day,5):
        print('Working Hours')
        with open(hosts_path,'r+') as file:
            content=file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+ "\n")

    else:
        with open(hosts_path, "r+") as file:
            content =file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Chill Hours...")
    time.sleep(5)
