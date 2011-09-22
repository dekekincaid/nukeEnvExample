# menu.py example file for teaching people how to create their own
#
# Author: Deke Kincaid, The Foundry
# dekekincaid@gmail.com
# v1.0
# 10/22/11
#
# menu.py is automatically executed when you launch nuke but only in interactive(gui) sessions
# if you need something when you render on the farm then you should put it in the init.py
#
# this example shows setting default formats,adds custom menu gizmos, shortcuts, python/tcl scripts
#
#
# Install Instructions:
# 1. copy the file into your .nuke folder or anywhere in your NUKE_PATH 
#
#
# Any issues then email me
# dekekincaid@gmail.com
#
# credits:
# Diogo Girondi's branchout.py is used as and example of adding a python script to the menu
# Frank Reuter's SearchReplacePanel is an example of installing a python panel
# Ivan Busquets grad.gizmo is the example for adding gizmos with icons
# 

#this example defines format resolutions


nuke.addFormat ("1280 720 0 0 1280 720 1.0 720p")
nuke.addFormat ("2048 1108 0 0 2048 1108 1.0 2k_185")
nuke.addFormat ("2048 1157 0 0 2048 1157 1.0 2k_3perf")
nuke.addFormat ("2048 872 0 0 2048 872 1.0 2k_235")

#here we are importing python modules and scripts for use as menu items or panels inside nuke on startup

import os
import os.path
import sys
import nuke
import time

import branchout
import IconPanel
import nodeOps
import SearchReplacePanel

#this is where I add different buttons in your tools menus which call python scripts, gizmos, etc... 
nuke.menu("Nodes").addMenu("Filter").addCommand("aePremult", "nuke.createNode('aePremult.gizmo')", index=4)#add a gizmo to the Filter menu, index value is menu item number
nuke.menu("Nodes").addMenu("Image").addCommand("Grad", "nuke.createNode('grad')", icon='grad.png', index=8)#add gizmo to Image menu, assigns a specified icon
nuke.menu("Nodes").addMenu("Channels").addCommand("Branch Out Channels", "branchout.branchout()", 'alt+b')#add python script example below to channel menu #also adds alt+b hotkey

#alternative way to add many items to a single menu with a basic variable
menubar=nuke.menu("Nodes")
m=menubar.addMenu("Image")
m.addCommand("Grad", "nuke.createNode('grad')", icon='grad.png', index=8)
m.addCommand("aePremult", "nuke.createNode('aePremult.gizmo')", index=4)
m.addCommand("Branch Out Channels", "branchout.branchout()")

#This adds html links to help Menu
nuke.menu("Nuke").addMenu("Help").addCommand("Creative Crash Nuke Downloads", "nuke.tcl(\"start \\\"http://www.creativecrash.com/nuke/downloads/\\\"\")")
nuke.menu("Nuke").addMenu("Help").addCommand("Creative Crash Nuke Tutorials", "nuke.tcl(\"start \\\"http://www.creativecrash.com/nuke/tutorials/\\\"\")")
nuke.menu("Nuke").addMenu("Help").addCommand("Vfxtalk Nuke Forum", "nuke.tcl(\"start \\\"http://www.vfxtalk.com/forum/nuke-foundry-f60.html\\\"\")")
nuke.menu("Nuke").addMenu("Help").addCommand("Vfxtalk Nuke Downloads", "nuke.tcl(\"start \\\"http://www.vfxtalk.com/forum/nuke-plugins-scripts-f124.html\\\"\")")
nuke.menu("Nuke").addMenu("Help").addCommand("Nukepedia", "nuke.tcl(\"start \\\"http://www.nukepedia.com\\\"\")")



#this sets default node values on the grade node and write node
nuke.knobDefault('Grade.black_clamp','false')#turns off black clamp knob on Grade nodes when created
nuke.knobDefault("Write.channels", "rgba")#changes the default on write nodes from rgb to rgba


#example for spawining an external application or process from a nuke button
import subprocess
nuke.menu("Nuke").addMenu("Footage").addCommand('BrokenGlass rv', "subprocess.Popen('/usr/local/tweaks/rv/bin/rv /path/to/my/files/', shell = True)")#this spawns flipbook for specific render
nuke.menu("Nuke").addMenu("Utilities").addCommand('Vim', "subprocess.Popen('/usr/bin/gvim', shell = True)")#this creates a menu on the top bar called Utilities and adds a button to start up gvim 


#example for adding slog lut in root
nuke.root().knob('luts').addCurve("sLog", "{pow(10.0, ((t - 0.616596 - 0.03) /0.432699)) - 0.037584}")

#example for killing all viewers apon opening new script to speed up working with large scripts
def killViewers():
    for v in nuke.allNodes("Viewer"):
        nuke.delete(v)
nuke.addOnScriptLoad(killViewers)

#adds frank's search and replace python panel which is included
def addSRPanel():
	'''Run the panel script and add it as a tab into the pane it is called from'''
        myPanel = SearchReplacePanel.SearchReplacePanel()
        return myPanel.addToPane()
nuke.menu('Pane').addCommand('SearchReplace', addSRPanel)#THIS LINE WILL ADD THE NEW ENTRY TO THE PANE MENU
nukescripts.registerPanel('com.ohufx.SearchReplace', addSRPanel)#THIS LINE WILL REGISTER THE PANEL SO IT CAN BE RESTORED WITH LAYOUTS


