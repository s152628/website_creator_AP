import os
import shutil


def constructor(choice):
    if os.path.exists("Running_Website\website.html"):
        os.remove("Running_Website\website.html")
    if choice == "1":
        shutil.copyfile("html/template_1.html", "Running_Website/website.html")
    elif choice == "2":
        shutil.copyfile("html/template_2.html", "Running_Website/website.html")
    elif choice == "3":
        shutil.copyfile("html/template_3.html", "Running_Website/website.html")
