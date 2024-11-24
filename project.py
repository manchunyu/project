#!/usr/bin/env python3

import os
import shutil
import sys
import sqlite3
import pyfiglet
import inquirer

def main():
    foldername = sys.argv[1]
    if check_foldername(foldername):
        shutil.rmtree(foldername)

    requirements = get_user_requirements()
    scaffold(foldername, requirements)
    
    
def check_foldername(fname):
    if os.path.exists(f"./{fname}"):
        answer = input("Folder already exists, would you like to replace it? [Y]es/[N]o ")
        return True if answer == "Y" else sys.exit("Exited program.")


def get_user_requirements():
    questions = [
    inquirer.Checkbox(
        "requirements",
        message="Select the features required",
        choices=["Database", "User Authentication"],
    ),
    ]
    return inquirer.prompt(questions)["requirements"]

    
def scaffold(fname, requirements):
    path = f"./{fname}"

    shutil.copytree("./template/apptemplate", path)
    

    if "Database" in requirements:
        sqlite3.connect(f"{path}/{fname}.db")

        lines = []
        with open(f"{path}/app.py", "r") as file:
            lines = file.readlines()
                   
        lines.insert(0, "from cs50 import SQL\n")

        with open(f"{path}/app.py", "w") as file:
            file.writelines(lines)
            
        

if __name__ == "__main__":
    main()


