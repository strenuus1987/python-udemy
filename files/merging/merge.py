import glob2
import datetime

files = glob2.glob("*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", 'w') as file_res:
    for file in files:
        with open(file, 'r') as f:
            file_res.write(f.read() + "\n")
