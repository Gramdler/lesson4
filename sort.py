###This script sorts files in the folder which user give in an argument when open script in console. And print result in console###

import sys
from pathlib import Path

# Start to work with functions
#enclosure = False


def print_vocabluary(vocabluary={}, p=str):
    print("_______________________________________")
    print(
        f"Congragulation!\nYour files in folder: {p}\n\thad been sorted:")
    for key, values in vocabluary.items():
        if vocabluary[key] != []:
            print(f"{key.title()} :", end="")
            for value in set(values):
                print(f" {value}", end='')
            print()
    print()
    print("Thank you for take our service!")


def sort(folder_path=Path()):

    # function sort files in formats in folder.
    # Folder_path is folder path in string, formats is vocabluary
    # where keys are the name of kind format and values are files extension
    # Give result in vocaluary like formats variant with addition keys know_extension and unknow_extension###
    list_formatted = {
        "image": [],
        "video": [],
        "doc": [],
        "music": [],
        "archive": [],
        "unidentified": [],
        "exists_formats": [],
        "unexists_formats": []
    }  # vocabluary for result function

    formats = {
        "image": ["JPEG", "PNG", "JPG", "SVG"],
        "video": ["AVI", "MP4", "MOV", "MKV"],
        "doc": ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"],
        "music": ["MP3", "OGG", "WAV", "AMR", "M4A"],
        "archive": ["ZIP", "GZ", "TAR", "RAR"]
    }
    name_list = []
    suffix_list = []
    tmp = []
    p = Path(folder_path)
    for i in p.iterdir():
        if i.is_file():
            if i.suffix:
                for key, values in formats.items():
                    if i.suffix[1:].upper() in values:
                        list_formatted[key].append(i.name)
                        list_formatted["exists_formats"].append(
                            f"{i.suffix[1:].upper()}")
                name_list.append(i.name)
                suffix_list.append(i.suffix[1:].upper())
        # I need add list to find name of files in dir wich unidentified.
        # Because anoter method didn't work.
        for value in list_formatted.values():
            if value != []:
                tmp = tmp[:] + value[:]
        while name_list:
            name = name_list.pop()
            if name not in tmp:
                list_formatted["unidentified"].append(name)
        for value in suffix_list:
            if value not in list_formatted["exists_formats"]:
                list_formatted["unexists_formats"].append(value)
    print_vocabluary(list_formatted, p)
    for i in p.iterdir():
        if i.is_dir() and not i.name.startswith('.'):
            #print(f"files from enclosure folder {i.name}: ")
            # enclosure
            sort(f"{Path.cwd()}\{p.name}\{i.name}")
        elif i.is_file():
            continue
        else:
            print("If you see this message, that something went wrong")


# Take first argument from conslone after name of script, and check variant if user didn't give way.
try:
    folder_path = sys.argv[1]
except IndexError:
    folder_path = "Error path"

# Check condition if script take wrong way.

if folder_path == "Error path":
    print("You didn't enter in console folder path.\nIf you want to sort files in the current folder, enter Y\n to finish program enter N or anything: ")
    tmpb = input("Y/N: ")
    folder_path = Path() if tmpb.lower() == "y" else exit()

sort(folder_path)
