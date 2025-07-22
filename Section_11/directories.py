import os


def listDirectories(s):

    def dirList(d):
        nonlocal tabStop
        files = os.listdir(d)
        for f in files:
            currentDir = os.path.join(d, f) # joins both the directory and the file together
            if os.path.isdir(currentDir):
                print("\t" * tabStop + "Directory" + f)
                tabStop += 1
                dirList(currentDir)
                tabStop -= 1
            else:
                print("\t" * tabStop + f)


    tabStop = 0
    if (os.path.exists(s)):
        print("Directory listing of " + s)
        dirList(s)
    else:
        print(s + " does not exist")


listDirectories(".")

# listings = os.walk('.')
# for root, directories, files in listings:
#     print(root)
#     for d in directories:
#         print(d)
#     for f in files:
#         print(f)