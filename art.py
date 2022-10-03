# make 10 random commits to github to a repo

import os
import random
import time

def main():
    
    # make 10 random commits
    for i in range(10):
        # make a random file
        with open('random.txt', 'w') as f:
            f.write(str(random.randint(0, 1000)))
        # add file to git
        os.system('git add random.txt')
        # commit file
        os.system('git commit -m "random commit" ' + str(time.time()))
        # push to github
        os.system('git push')
        # wait 1 second
        time.sleep(1)

main()