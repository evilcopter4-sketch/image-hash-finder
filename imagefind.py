#important note:
# this is not a proffesional tool
# it will not hold up in a court of law
# use at your own risk!
import webbrowser
from PIL import Image
import imagehash
import os
import urllib.parse

def find(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
while True:
    targselect = input("type the name of your file.\n I will find all the files on the system that match it's name.\n Then select the first one:\n").strip('"\'')
    pselect = input("where should I start looking: \n").strip('"\'')
    hashtarg = find(targselect, pselect)
    if hashtarg is not None: 
        hashval = imagehash.phash(Image.open(hashtarg))
        print(f"pHash: {hashval}")
        scrape = input("I can scrape the web if you'd like[y/n]: \n").strip('"\'')
        while scrape.lower() == 'y':
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
                
    #this is the funtion to select if you want to go again.
    else:
        print("file not found.")
    gogn = input("Do you have another image? [Y/N]: \n")
    if gogn.lower() == 'y':
       continue
    else:
        print("done")
        break
