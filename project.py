#!/usr/bin/env python3

import os
import shutil
import sys
import sqlite3
import pyfiglet
import inquirer



def main():
    welcome_text = pyfiglet.figlet_format("Welcome to your Flask app", font="doom")
    print(welcome_text)

    requirements = get_user_requirements()
    if check_foldername(requirements["project_name"]):
        shutil.rmtree(requirements["project_name"])

    print(f"Setting up {requirements['project_name']} for you...")
    scaffold(requirements["project_name"], requirements["database"])
    print(f"{requirements['project_name']} is ready for you, happy coding!")
    
    
    
def check_foldername(fname):
    if os.path.exists(f"./{fname}"):
        questions = [
            inquirer.List("to_delete", 
                            message=
                            f"You have an existing folder named {fname}, would you like to delete it?",
                            choices=["Yes", "No"])
                    ]
        return True if inquirer.prompt(questions)["to_delete"] == "Yes"\
                    else sys.exit("Exited program.")


def get_user_requirements():
    questions = [
    inquirer.Text("project_name", message="Name of project"),
    inquirer.List(
        "database",
        message="Do you need a database",
        choices=["Yes", "No"],
    ),
    ]
    return inquirer.prompt(questions)

    
def scaffold(fname, database):
    path = f"./{fname}"

    shutil.copytree("./template", path)
    

    if database == "Yes":
        sqlite3.connect(f"{path}/{fname}.db")

        lines = []
        with open(f"{path}/app.py", "r") as file:
            lines = file.readlines()
                   
        lines.insert(0, "from cs50 import SQL\n")

        with open(f"{path}/app.py", "w") as file:
            file.writelines(lines)
            
        

if __name__ == "__main__":
    main()



