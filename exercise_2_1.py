#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:26:55 2018

@author: DAB
"""
import os
os.getcwd()

import time
import sys
import random
from psychopy import visual,event,core


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names] #0 represents first column in txt file

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
stim = visual.TextStim(win, '+',color="white", colorSpace='rgb')
while True:
    stim.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(firstNames)
    firstNameStim.setText(nameShown)   
    firstNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)
    
    if event.getKeys(['q']):
        win.close()
        sys.exit()