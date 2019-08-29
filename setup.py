import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Deepak\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6"
os.environ['Tk_LIBRARY'] = r"C:\Users\Deepak\AppData\Local\Programs\Python\Python37-32\tcl\tk8.6"

executables = [cx_Freeze.Executable('struct_text_editor.py',base =base , icon='icon.ico')]

cx_Freeze.setup(
    name = "Struct Text Editor",
    options = {"build_exe":{"packages":["tkinter","os"],"include_files":["icon.ico",'tcl86t.dll','tk86t.dll','icons']}},
    version = "0.01",
    description = "Tkinter Application",
    executables =  executables
)