import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()

        time.sleep(random.random() * 0.3)

mengetik('Terimakasih Telah,Memakai\nScript Arimengen\nDan\nJangan Lupa Subscribe')

time.sleep(0.9)
import os
os.system("clear")