this is a script I made to try using for OSINT
it is currently in development

***** BUGS AND STUFF *****

  * it doesn't support MacOS you will have to compile it yourself
  * if you have spaces in your linux file path to the actuall imagefind.py, it will break the thingy.
  * You need to have python3 installed on windows. ensure that you have added python to path
  * the .desktop shortcut(linux) sets Terminal=true. because of this, it will throw errors on minimalist desktop environments and standalone windows
  * to fix the above issue, execute 'python3 imagefind.py' directly from your terminal
  * if the installer fails, you will have to run: 'pip install pillow imagehash' for the imagefind.py to work.

***** REQUIREMENTS *****

  * python3
  * Pillow module
  * imagehash
  * Add python to path if running windows

***** USAGE *****

  * when running imagefind.py, you will be asked for the name of your image. make sure to include the extension
  * you will then be asked which folder/directory the script should look in.
  * after finding your image, it will give 3 options for web scraping.
  * we don't know if it works for non image files.

***** OTHER *****

  * this has not been fully tested. you are the guinea pigs. please put any bugs and stuff inside the comments.
  * this is not a proffesional tool. in future, it may be. but right now, don't use it for anything that you have to present in court.
