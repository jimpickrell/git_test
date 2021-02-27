# we want to find if git is in this folder, or upstream
# https://www.tutorialspoint.com/python/os_walk.htm
# https://lippincottlibrary.wordpress.com/2020/02/05/python-find-files-with-os-walk/

import os
path=os.getcwd();
#path = os.path.normpath(path)
pathos = path.split(os.sep)
print(pathos)

mypath = "/"
my_git_location = ""
for p in pathos:
    print(p)
    mypath = os.path.join(mypath,p)
    print(mypath)

    with os.scandir(mypath) as entries:
        for entry in entries:
            if(entry.name == "traverse.p"):    #  change this to .git
                print("traverse.py Found");
                my_git_location = mypath

if(my_git_location == ""):
    print("Git folder not found.")
    exit(1)
print("Git found at " + my_git_location)

exit();

#root="./"
#
#with os.scandir(root) as entries:
#    for entry in entries:
#        print(entry.name)

#root= "CS97---WestwoodWalks"
root= "../../../../../../../../"

with os.scandir(root) as entries:
    for entry in entries:
        if(entry.name == ".git"):
            print("Found");
        #print(entry.name)



#for dirname, dirnames, filenames in os.walk('.'):
    # os.walk returns a triple unit: dirname, dirnames, filenames
    # print("## analyzing " + dirname)
 
#    if '.git' == dirname:
        #result.append(os.path.join(root, dirname))
#        result=os.path.join(root, dirname)
#        print(".git found at " + result);
 
 
 
 
    # print("print path to all subdirectories")
#    for subdirname in dirnames:
#        print(os.path.join(dirname, subdirname))

    # print("print path to all filenames.")
 #   for filename in filenames:
 #       print(os.path.join(dirname, filename))

    #The simpler way to ignore some directories is to not add them to dirnames 
    #    in the first place for subdirname in dirnames: if subdirname != '.git'