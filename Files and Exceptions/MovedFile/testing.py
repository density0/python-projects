import os
import shutil
import sys





def filepath():
    path = ''
    path = os.getcwd().format()

    pos_slash = path.index("U")

    path = f"{path[0:pos_slash]}" + "\\" + f"{path[pos_slash:]}"
    return path


shutil.move("testing.py", filepath() + "\\MovedFile")
