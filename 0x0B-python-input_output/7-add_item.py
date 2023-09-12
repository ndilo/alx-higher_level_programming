#!/usr/bin/python3
"""
file with function that adds all arguments to
a python list and saves to a file
"""


import json
from sys import argv


save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    new_item = load_json(filename)
except (ValueError, FileNotFoundError):
    new_item = []

new_item = new_item + argv[1:]
save_json(new_item, filename)
