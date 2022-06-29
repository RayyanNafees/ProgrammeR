import sys # Imports are automatically detected (normally) in the script to freeze
import os 

base = None 

os.environ["TCL_LIBRARY"] = "<PathToPython>\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ["TK_LIBRARY"] = "<PathToPython>\\Python\\Python36-32\\tcl\\tk8.6"

if sys.platform=='win32':
    base = "Win32GUI"


executables = [cx_Freeze.Executable("Show_file.py")]    

cx_Freeze.setup(
        name = "Name",
        options = {"build_exe":{"packages":["tkinter","matplotlib"],"include_files":["test.ico", "<PathToPython>\\\\Python\\Python36-32\\DLLs\\tcl86t.dll", "<PathToPython>\\\\Python\\Python36-32\\DLLs\\tk86t.dll"]}},
        version="0.01",
        executables=executables) 
