#!/usr/bin/python3
"""A module for 7-add_item"""

import os
import sys
import json

save_to_json_file = __import__("5-save_to_json_file").\
        save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").\
        load_from_json_file

f = "add_item.json"

if os.path.exists(f):
    save_to_json_file(load_from_json_file(f), f)
else:
    save_to_json_file([arg for arg in sys.argv[1:]], f)
