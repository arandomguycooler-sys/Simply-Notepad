import os

app_name = "SimplyNotepad"
source_file = "SimplyNotepad.py"
icon_file = "SimplyNotepad.ico"

os.system(f'pyinstaller --noconfirm --onefile --windowed --icon "{icon_file}" --name "{app_name}" --add-data "{icon_file};." "{source_file}"')
