#download it and update website list as of ur choice and also timiing n thn add this to your 
#task schedulare to run it immediately on the start of the system save it with extension pyw

import time
from datetime import datetime as dt

hosts_temp=r"C:\website blocker\hosts"
hosts_path=r"C:\Windows\System32\Drivers\etc\hosts"
redirect="127.0.0.1"

#list of websites to block
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]

while True:
    # conditional to block websites in working hour from 8 AM to 4 PM
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path ,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
