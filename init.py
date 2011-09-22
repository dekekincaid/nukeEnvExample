# init.py example file for teaching people how to create their own for use with Nuke
#
# Author: Deke Kincaid, The Foundry
# dekekincaid@gmail.com
# v1.0
# 10/22/11
# dekekincaid@gmail.com
#
# This file is automatically executed when you launch nuke in both command line and interactive(gui) sessions
#
# Install Instructions:
# 1. copy the file into your .nuke folder or anywhere in your NUKE_PATH 
#
#
# Any issues then email me or post a reply in the comments on nukepedia
# dekekincaid@gmail.com
#
#
import os
#
# this example is for directly pointing to other directories you want nuke to look at for loading scripts, gizmos and plugins
nuke.pluginAddPath("/blah/blah/blah/blah")
#nuke.pluginAddPath(os.path.exanduser("~/nukescripts"))# this exampe is if you want to use a folder relative to your user's home directory

#so lets say you want to really organize scripts on your home machine
#I would first set an environment variable for NUKE_PATH pointing to for example $HOME/nukescripts or /SERVERNAME/SERVERSHARE/PATH/TO/NUKE/ENVIRONMENT/ON/SERVER
#then I will then in my init.py setup the following to organize my scripts:
#
#this will use my home directory
nuke.pluginAddPath(os.path.expanduser("~/nukescripts"))
nuke.pluginAddPath(os.path.expanduser("~/nukescripts/gizmos"))
nuke.pluginAddPath(os.path.expanduser("~/nukescripts/icons"))
nuke.pluginAddPath(os.path.expanduser("~/nukescripts/lut"))
nuke.pluginAddPath(os.path.expanduser("~/nukescripts/plugins"))
nuke.pluginAddPath(os.path.expanduser("~/nukescripts/python"))
nuke.pluginAddPath(os.path.expanduser("~/nukescripts/tcl"))
#
#this example will use a location on the server
#
nuke.pluginAddPath("/path/to/server/nukescripts/gizmos")
nuke.pluginAddPath("/path/to/server/nukescripts/icons")
nuke.pluginAddPath("/path/to/server/nukescripts/lut")
nuke.pluginAddPath("/path/to/server/nukescripts/plugins")
nuke.pluginAddPath("/path/to/server/nukescripts/python")
nuke.pluginAddPath("/path/to/server/nukescripts/tcl")
