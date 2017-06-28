import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = r'C:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python36\tcl\tk8.6'

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup (
    name="Bug and Insect",
    options={"build_exe":{"packages":["pygame"],
                          "include_files": ["classes.py","process.py","images"]}},
    executables = executables

    )
