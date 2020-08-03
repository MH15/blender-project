from os.path import expanduser
home = expanduser("~")


STATE = {
    "root_path": home,
    "active_project": None,
    "project": None
}
