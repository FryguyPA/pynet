#!/usr/bin/env python

import yaml
import json

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'whatever', 'hello there', {'attribs': [0, 1, 2, 3, 4], 'ip_addr': '10.11.12.13'}]

print(my_list)

file = open("my_file.yml", "w")
file.write(yaml.dump(my_list, default_flow_style=False))
file.close()

file = open("my_file.json", "w")
file.write(json.dumps(my_list))
file.close()

