# https://www.tutorialspoint.com/python/os_walk.htm
# https://lippincottlibrary.wordpress.com/2020/02/05/python-find-files-with-os-walk/

import os

for dirname, dirnames, filenames in os.walk('./CS97---WestWoodWalks/.git'):
    # os.walk returns a triple unit: dirname, dirnames, filenames
    print("## analyzing " + dirname)
    # print("print path to all subdirectories")
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))

    # print("print path to all filenames.")
    for filename in filenames:
        print(os.path.join(dirname, filename))

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from going there.
    #if '.git' in dirnames:
        # don't go into any .git directories.
        #dirnames.remove('.git')
    #The simpler way to ignore some directories is to not add them to dirnames 
    #    in the first place for subdirname in dirnames: if subdirname != '.git'