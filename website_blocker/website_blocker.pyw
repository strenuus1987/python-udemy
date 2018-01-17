from datetime import datetime as dt
import time

hosts_path_temp=r"Hosts\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts" #r is for row string without any break lines. Another solution use \\
redirect="127.0.0.1"
websites_list=["www.youtube.com", "youtube.com", "www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        with open(hosts_path_temp, 'r+') as file:
            data = file.read()
            for website in websites_list:
                if website not in data:
                    file.write("\n" + redirect + " " + website)
    else:
        with open(hosts_path_temp, 'r+') as file: #move the carriage to the end of the file
            data = file.readlines()
            file.seek(0) # seek the carriage to the beggining of the file
            for line in data:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate() # removes everything after the pointer
    time.sleep(10)
