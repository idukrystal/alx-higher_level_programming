#!/usr/bin/python3
"""apends args to avjdon list file"""

from sys import argv
from json import JSONDecodeError
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file = "add_item.json"
open(file, "w").close()

try:
    obj = load_from_json_file(file)
except (JSONDecodeError):
    obj = []

obj.extend(list(argv)[1:])
save_to_json_file(obj, file)
