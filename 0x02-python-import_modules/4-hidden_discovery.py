#!/usr/bin/python3

import importlib.util, sys

module_name = "hidden_4"
path_to_module = "./hidden_4.pyc"
spec = importlib.util.spec_from_file_location(module_name)
module = importlib.util.module_from_spec(spec)

spec.loader.exec_module(module)

for name in dir(module):
    if not name.startwith("__"):
        print(name)
