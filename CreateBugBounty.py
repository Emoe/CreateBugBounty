#!//usr/local/bin/python3
import os
import sys

basePath = "/Users/moe/BugBounty/"

banner = """
    _________                        __                          
    \_   ___ \_______   ____ _____ _/  |_  ____                  
    /    \  \/\_  __ \_/ __ \\__  \\   __\/ __ \                 
    \     \____|  | \/\  ___/ / __ \|  | \  ___/                 
     \______  /|__|    \___  >____  /__|  \___  >                
            \/             \/     \/          \/                 
__________            __________                     __          
\______   \__ __  ____\______   \ ____  __ __  _____/  |_ ___.__.
 |    |  _/  |  \/ ___\|    |  _//  _ \|  |  \/    \   __<   |  |
 |    |   \  |  / /_/  >    |   (  <_> )  |  /   |  \  |  \___  |
 |______  /____/\___  /|______  /\____/|____/|___|  /__|  / ____|
        \/     /_____/        \/                  \/      \/     
"""

print(banner)
create = {
    "folder": ["recon", "findings"],
    "file": ["notes.md", "scope.txt"]
} 

organistaion = sys.argv[1]
try:
    os.mkdir(basePath + organistaion)
except:
    print ("Creation of the directory %s failed" % path)
    sys.exit()

for key in create:
    for item in create[key]:
        print("Debug: Creating {} called {}".format(key,item))

        if key == "folder":
            try:
                os.mkdir(basePath + organistaion + "/" + item)
            except OSError:
                print ("Creation of the directory %s failed" % item)
        if  key == "file":
            try:
                open(basePath + organistaion + "/" + item, 'a').close()
            except OSError:
                print ("Creation of the file %s failed" % item)
