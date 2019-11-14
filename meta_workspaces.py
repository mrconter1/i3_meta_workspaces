import os
import argparse
from subprocess import call

#Handle flags
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--meta", help="Meta flag")
parser.add_argument("-w", "--workspace", help="Workspace flag")
parser.add_argument("-mw", "--move_window", help="Move flag")
args = parser.parse_args()

#Name of stored meta variable
metaVarName = "meta_workspace"

#Correct path to stored variable
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'variables')

def readMeta():
    with open(filename) as fin:
        for line in fin:
            if line.startswith(metaVarName):
                return line.split(":")[-1].strip()

def writeMeta(value):
    if os.path.isfile(filename):
        os.remove(filename)
    with open(filename, 'a') as out:
        out.write(metaVarName + ":" + value + '\n')

#Create file if it does not exist
if not os.path.isfile(filename):
    writeMeta("0")

#Change meta workspace
if args.meta is not None:
    meta = args.meta
    writeMeta(meta)

#Change workspace within meta workspace
if args.workspace is not None:
    meta = readMeta()
    workspace = args.workspace
    print(meta)
    cmd = 'i3-msg "workspace ' + meta + workspace + ';"'
    os.system(cmd)

#Move window in between workspaces within meta workspace
if args.move_window is not None:
    meta = readMeta()
    workspace = args.move_window
    cmd = 'i3-msg "move container to workspace ' + meta + workspace + ';"'
    os.system(cmd)
