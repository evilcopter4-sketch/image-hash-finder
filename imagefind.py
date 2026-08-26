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
                        matches = 0
                        output_filename = "search_results.txt"
                
                        # Open log file for saving results
                        with open(output_filename, "a", encoding="utf-8") as out_file:
                            out_file.write(f"\n--- Search results for: {targselect} (pHash: {hashval}) ---\n")
                    
                            for root, dirs, files in os.walk(pselect):
                                for f in files:
                                    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp')) and f != targselect:
                                        img_path = os.path.join(root, f)
                                        try:
                                            other_hash = imagehash.phash(Image.open(img_path))
                                            distance = hashval - other_hash  # Hamming distance
                                            if distance <= 10:
                                                result_line = f"  [Match found! Distance: {distance}] -> {img_path}"
                                                print(result_line)
                                                out_file.write(result_line + "\n")
                                                matches += 1
                                        except Exception:
                                            continue
                                    
                    out_file.write(f"Total matches found: {matches}\n")
                print(f"Finished. Found {matches} matching image(s).\n")
                        
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
