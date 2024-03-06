import os
import time
import sys
import string
import random

running = True

def main():
        global running

        while running:
                try:
                        N = random.randrange(21,36)
                        oo = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=N))
                        os.system("clear")
                        print("PadLock v1.0 | Developed by bananasniper")
                        print("+=========================================+")
                        print()
                        print(str(oo))
                        print()
                        input("Press ENTER/RETURN to generate another password...")
                except KeyboardInterrupt:
                        sys.exit()

main()