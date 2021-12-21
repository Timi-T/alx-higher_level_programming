#!/usr/bin/python3
"""
python script to add arguments to a python list
"""


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.exists('add_item.json') and os.stat('add_item.json').st_size == 0:
    with open('add_item.json', mode='w', encoding='utf-8') as a_file:
        a_file.write('[]')
elif os.path.exists('add_item.json') is False:
    with open('add_item.json', mode='w', encoding='utf-8') as a_file:
        a_file.write('[]')
list_content = load_from_json_file('add_item.json')
argc = len(sys.argv)
for i in range(1, argc):
    list_content.append(sys.argv[i])
save_to_json_file(list_content, 'add_item.json')
