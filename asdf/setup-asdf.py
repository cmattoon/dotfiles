#!/usr/bin/env python3
import os, sys
import yaml

import subprocess
import shlex

def exec(command: str):
    print(f"[exec] \033[36m{command}\033[0m")
    command = shlex.split(command)
    ps = subprocess.Popen(command,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    out, err = ps.communicate()
    return out.decode('utf-8'), err.decode('utf-8')

datafile = os.path.join(os.path.dirname(__file__), 'asdf.yaml')
with open(datafile) as fd:
    data = yaml.load(fd, Loader=yaml.SafeLoader)
try:
    query = sys.argv[1]
except IndexError:
    query = None
    
for app in data:
    name = app.get('name')
    if query is None or query == name:
        plugin_url = app.get('plugin', {}).get('url')
        current = app.get('current')
        exec(f"asdf plugin add {name} {plugin_url}")
        for version in app.get('versions'):
            exec(f"asdf install {name} {version}")
        exec(f"asdf set -p {name} {current}")
        print("")
