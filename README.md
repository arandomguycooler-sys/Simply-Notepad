# SimplyNotepad

**SimplyNotepad** is a lightweight, simplified text editor for Windows, created by **Vsy**.
It’s inspired by classic Notepad but for Low-End PCs that hardly can run Notepad.

---

## Features

- Open, edit, and save text files (`.txt`)  
- Undo/redo support  
- Line numbers display  
- Copy, cut, and paste functionality  
- File type association with `.txt`  
- Modern installer support (via Inno Setup)  

---

## Installation

### Windows (Executable)

1. Download the latest installer from the Releases page
2. Run the installer and follow the instructions
3. SimplyNotepad will be available from your Start Menu and desktop (optional)


## Python Source
1. Get Git from here if you havent yet: https://git-scm.com/install/
2. Install Python 3.x from python.org(if you havent yet)
3. Get the source using the command below
```bash
git clone https://github.com/arandomguycooler-sys/Simply-Notepad
```
4. Run the .py script using the command below
```bash
python SimplyNotepad.py
```

### Building
You can build Simply Notepad in TWO ways:

Manual: 
  1. First get the source using the Tutorial above until step 4.
  2. If you havent, get Pyinstaller using the command below(you can use auto-py-to-exe!)
  ```bash
  pip install pyinstaller
  ```
  3. Use any command you would like, but i use this:
  ```bash
  pyinstaller --noconfirm --onefile --windowed --icon "SimplyNotepad.ico" --name "SimplyNotepad" --add-data "SimplyNotepad.ico;." "SimplyNotepad.py"
  ```
Automated:
  1. Get the source using the "Python Source" tutorial
  2. Run the build.py file in ANY way.
  3. Your done, if something errors, use Manual instead.

### Porting it over to a USB so you can install it
1. Get the installer(if your pc cant run the installer, Build it from source.)
2. Run the installer/Run the .exe that comes when you build it.

### Contributing
Contributions are welcome!
How to contribute:
1. Fork this Repository
2. Modify YOUR fork in ANY way.
3. Submit a pull request.
4. Wait until i review it
5. if i accept, your fork will be merged!
6. if i deny, your fork will not be merged and you will get why. Common reasons include but dont extend to: Trolling(e.g. Deleting the GUI.) and Merge Problems.

### Contact
You can contact me on Discord(my Discord is randomsyofficial) but if you wanna get info about your Pull Request getting closed, see above.
