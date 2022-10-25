#!/usr/bin/python3
"""apends args to avjdon list file"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file = "add_item.json"
try:
    obj = load_from_json_file(file)
except (TypeError):
    obj = []
obj.append(list(argv))
save_to_json_file(obj, file)
