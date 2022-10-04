# commit to github repo with gitpython module

from git import repo
import random

# commit once to github repo

def main():
    # make a random file
    with open('random.txt', 'w') as f:
        f.write(str(random.randint(0, 1000)))
    # add file to git
    repo.index.add(['random.txt'])
    # commit file
    repo.index.commit('random commit')
    # push to github
    origin = repo.remote('origin')
    origin.push()


main()