# important note:
# this is not a proffesional tool
# it will not hold up in a court of law
# use at your own risk!
import webbrowser
from PIL import Image
import platform
import imagehash
import os
import urllib.parse
from pathlib import Path
import string
import sys
#basic file finder stolen from stack ovflw
def find(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
while True:
    targselect = input("type the name of your file.\n I will find all the files on the system that match it's name.\n Then select the first one:\n").strip('"\'')
    r, ext = os.path.splitext(targselect)
    pselect = input("where should I start looking: \n").strip('"\'')
    hashtarg = find(targselect, pselect)
    if hashtarg is not None: 
        hashval = imagehash.phash(Image.open(hashtarg))
        print(f"pHash: {hashval}")
        #web scrapey bit
        scrape = input("the following are your options: \n 1.search web \n 2.search drive \n 3.abort \n").strip('"\'')
        if scrape.lower() == '1':
                searchtype = input("press the number beside the scrape option to select that scrape option: \n 1. search for the hash\n  2. search for the name\n  3. use google lens \n").strip('"\'')

                if searchtype == "1":
                        query = urllib.parse.quote(str(hashval))
                        webbrowser.open(f"https://www.google.com/search?q={query}")
                        
                elif searchtype == "2":
                    query = urllib.parse.quote(targselect)
                    webbrowser.open(f"https://www.google.com/search?tbm=isch&q={query}")
                
                elif searchtype == "3":
                    webbrowser.open("https://lens.google.com")
                        
                searchagain = input("would you like me to search again with the same image name and hash? [y/n]: \n")
                if searchagain.lower() != 'y':
                        break
        #drive scraper
        elif scrape.lower() == '2':
                print("You have selected the file system scraper. \n I will scrape the filesystem for similiar hashes to your file.\n please wait while I find all drives on your computer.")
                system = platform.system()
                def detos():
                        if system == "Windows":
                                return "windows"
                        elif system == "Linux":
                                return "linux"
                        else:
                                sys.exit(f"Unsupported Operating System: {system} \n")
                print(f" this is the extension I will now search for on this: {ext}\n")
                #windows drive scraper. will get a more efficient file system scraper later. for now, do not trust it as it prolly gets caught up on file permisions and that typa stuff.
                crdr = os.path.dirname(os.path.realpath(__file__))
                jk = detos()
                if jk == "windows":
                        dtarg = input("type the drive letter/path that we will scan today:\n")
                        print("\nthis'll take a while. I will send the outputs to a txt in the folder you installed this program in,\n named {r}_report_matches, \n and other similiarly named images.\n")
                        b = Path(dtarg).rglob(f"*{ext}")
                        for path in b:
                                try:
                                        with Image.open(path) as img:
                                                cmhsh = imagehash.phash(img)
                                                #compare leur/les hashes
                                                ham_thresh = 10
                                                distcheck = cmhsh - hashval
                                                if distcheck <= ham_thresh:
                                                        #les matches de hashes ecri a un fichier
                                                        try:
                                                                report_path = os.path.join(crdr, f"{r}_report_hashes.txt")
                                                                with open(report_path, "a", encoding="utf-8") as f:
                                                                        f.write(f"found a match to {hashval}! hamming distance: {distcheck}, image is {path}, image hash is {cmhsh}\n\n")
                                                        except FileExistsError:
                                                                print(f"{r}_report_hashes.txt already exists bro")
                                                
                                                
                                except Exception as e:
                                        continue
                                
                elif jk == "linux":
                        print(f"\nyou have selected linux. as with the windows functionality, I will output to {r}_report_matches.txt. this will take a while tho.\n")
                        print("I will start searching from the root folder.\n")
                        b = Path("/").rglob(f"*{ext}")
                        for path in b:
                                pp = path.parts
                                if "proc" in pp or "sys" in pp:
                                        continue
                                try:
                                        with Image.open(path) as img:
                                                cmhsh = imagehash.phash(img)
                                                #compare leur/les hashes
                                                ham_thresh = 10
                                                distcheck = cmhsh - hashval
                                                if distcheck <= ham_thresh:
                                                        #les matches de hashes ecri a un fichier
                                                        try:
                                                                report_path = os.path.join(crdr, f"{r}_report_hashes.txt")
                                                                with open(report_path, "a", encoding="utf-8") as f:
                                                                        f.write(f"found a match to {hashval}! hamming distance: {distcheck}, image is {path}, image hash is {cmhsh}\n\n")
                                                        except FileExistsError:
                                                                print(f"{r}_report_matches.txt already exists bro")
                                except Exception as e:
                                        continue
                                                                
    #this is the thingy to select if you want to go again.
    else:
        print("file not found.")
    gogn = input("Do you have another image? [Y/N]: \n")
    if gogn.lower() == 'y':
       continue
    else:
        print("done")
        break
