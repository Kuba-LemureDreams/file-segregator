import shutil
import typer
import os
from typing_extensions import Annotated

app = typer.Typer(help="A script to segregate files on your desktop or in other folders")

@app.command("defpath")
def default_path(auto_assign: Annotated[str, typer.Argument()]):
    """
    Automatically load in path:
    if option is win, then load desktop folder
    if option is here, then load in script executable location
    otherwise input is path
    """
    if auto_assign == "win":
        op_user = typer.prompt("What is the name of your user folder?")
        seg_path = f"C:\\Users\\{op_user}\\Desktop"
    elif auto_assign == "here":
        seg_path = os.getcwd()
    else:
        seg_path = auto_assign
    if not os.path.exists("./tmp"):
        os.mkdir("./tmp")
    f = open("./tmp/env.txt", "w")
    f.write(seg_path)
    f.close()

@app.command()
def clean_tmp():
    """
    Cleans temporary files.
    """
    cleaning = typer.confirm("Are you sure you want to remove temporary files of the script?")
    if os.path.exists("./tmp") and cleaning:
        shutil.rmtree("./tmp")
        print("Cleaning!")
    elif not os.path.exists("./tmp"):
        print("Directory not found!")
        raise typer.Abort()
    elif not cleaning:
        print("Aborting!")
        raise typer.Abort()
    else:
        print("Unknown error, contact administrator")
        raise typer.Abort()

@app.command("list")
def list_items():
    """
    If is True, then prints out items in a current folder
    """
    f = open("./tmp/env.txt", "r")
    seg_path = f.read()
    f.close()
    file_tree = os.scandir(seg_path)
    for entry in file_tree:
        if entry.is_file():
            print(entry.name)

@app.command()
def segregate():
    """
    Main function to segregate your files, just run and let magic happen
    """
    f = open("./tmp/env.txt", "r")
    seg_path = f.read()
    f.close()
    file_tree = os.listdir(seg_path)
    for entry in file_tree:

        if entry.endswith(".jpg") or entry.endswith(".png") or entry.endswith(".jpeg") or entry.endswith(".webp") or entry.endswith(".gif"):
            if not os.path.exists(seg_path+"\\seg\\images"):
                os.mkdir(seg_path+"\\seg")
                os.mkdir(seg_path+"\\seg\\images")
            shutil.move(seg_path+"\\"+entry, seg_path+"\\seg\\images\\"+entry)
        if entry.endswith(".mp3") or entry.endswith(".wav") or entry.endswith(".flac"):
            if not os.path.exists(seg_path + "\\seg\\soundfiles"):
                if not os.path.exists(seg_path + "\\seg"):
                    os.mkdir(seg_path + "\\seg")
                os.mkdir(seg_path + "\\seg\\soundfiles")
            shutil.move(seg_path+"\\"+entry, seg_path+"\\seg\\soundfiles\\"+entry)
        if entry.endswith(".docx") or entry.endswith(".odt") or entry.endswith(".txt") or entry.endswith(".json"):
            if not os.path.exists(seg_path + "\\seg\\txtfiles"):
                if not os.path.exists(seg_path + "\\seg"):
                    os.mkdir(seg_path + "\\seg")
                os.mkdir(seg_path + "\\seg\\txtfiles")
            shutil.move(seg_path+"\\"+entry, seg_path+"\\seg\\txtfiles\\"+entry)
        if entry.endswith(".pdf"):
            if not os.path.exists(seg_path + "\\seg\\pdf"):
                if not os.path.exists(seg_path + "\\seg"):
                    os.mkdir(seg_path + "\\seg")
                os.mkdir(seg_path + "\\seg\\pdf")
            shutil.move(seg_path+"\\"+entry, seg_path+"\\seg\\pdf\\"+entry)
        if entry.endswith(".zip") or entry.endswith(".7z") or entry.endswith(".tar.xz") or entry.endswith(".tar.gz"):
            if not os.path.exists(seg_path + "\\seg\\archives"):
                if not os.path.exists(seg_path + "\\seg"):
                    os.mkdir(seg_path + "\\seg")
                os.mkdir(seg_path + "\\seg\\archives")
            shutil.move(seg_path+"\\"+entry, seg_path+"\\seg\\archives\\"+entry)
        if entry.endswith(".exe") or entry.endswith(".iso"):
            if not os.path.exists(seg_path + "\\seg\\executables"):
                if not os.path.exists(seg_path + "\\seg"):
                    os.mkdir(seg_path + "\\seg")
                os.mkdir(seg_path + "\\seg\\executables")
            shutil.move(seg_path+"\\"+entry, seg_path+"\\seg\\executables\\"+entry)

    clean_tmp()



if __name__ == '__main__':
    app()

