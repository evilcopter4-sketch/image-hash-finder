#this is my trinidad. this is a developer thingy, that I made to figure out how some stuff works. you could use this, but I encourage the use of my real tool.
#like with most of my tools, the documentation is in the comments in the code. because I don't think anyone other than me will use these tools.

#note, you will want a bunch of ram especially for big websites


from io import BytesIO
import requests
from PIL import Image
import imagehash
import re
#commented out imports are things that will be used later, but don't need to be here right now.
#in general, my comments are for my mavigation, not your convenience

#url scanner
def urlscan(targurl):
    ris = requests.get(targurl)
    if ris.status_code == 200:
        r2 = ris.text
    return r2

#file opener. I prolly couldve left it out of a function, but I need to practice functions, so there.
def rf(ftarget):
    with open(ftarget, 'r') as file:
        lines = file.readlines()
        return lines


#downloader. this sends the image to memory for analysis. image.load() is used for debugging.

def dl(dltarget):
    res = requests.get(dltarget)
    print(res)
    if res.status_code == 200:
        img = Image.open(BytesIO(res.content))
        img.show()
        img.load()
        return img
            
    else:
        return "Error. idk what happened, bcuz my developer is a butt."

#here's the fun bit. basically asks where file is, duh, then converts the contents into a list. note for users, if you are reading this, your target file must have each
#target site on a newline, otherwise the code will try to scan a website that has https: in it twice.
htmlraw = []
htmlref1 = []
htmlref2 = []
test1 = input("Type the path to the txt file containing your target website list: \n").strip()
flistraw = rf(test1)
flistref = [lines.strip('\n') for lines in flistraw]

#this bit filters for only lines containing pngs.

for u in flistref:
    htmlraw.extend(urlscan(u).splitlines())
    htmlref1 = [line for line in htmlraw if ".png" in line]
    print(f"u equals:\n\n {u}")
#devcheck    
print(htmlref1)


#further refinement.
htmlref2 = []
for line in htmlref1:
    htp = line.split('"')
    for hp in htp:
        if ".png" in hp:
            htmlref2.append(hp)
            print(f"htp equals:\n\n {htp}")
            print(f"hp equals:\n\n {hp}")
#devcheck
print(htmlref2)
#downloading from htmlref2. should be simple. the reason it's lur is because url is too basic.
#this is where my script fucks up. due to the way the html code links are left inside these websites, there is no http://<target server> for lur
#plan for fixing: try adding an https:// thing on there. 
for lur in htmlref2:
    try:
        print(f"u = \n\n{u}")
        testtargffswork = u + lur
        print(f"testtargffswork = \n\n{testtargffswork}")
        test2 = dl(testtargffswork)
        p = imagehash.phash(test2)
        print(p)
        
    #error handling I stole off stack overflow
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print("API returned a 404 error: Not Found")
        else:
            print("API returned an error:", e)
    except Exception as e:
        print("An error occurred:", e)

#this should be done. it'll prolly brick mein computer. but oh well. 
