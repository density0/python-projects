import os





def filepath():
    path = ''
    path = os.getcwd().format()

    pos_slash = path.index("U")

    path = f"{path[0:pos_slash]}" + "\\" + f"{path[pos_slash:]}"
    return path






print(filepath())