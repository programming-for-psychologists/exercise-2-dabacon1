#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:26:55 2018

@author: DAB
"""
import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names] #0 represents first column in txt file
lastNames = [name.split(' ')[1] for name in names] #1 indicates second column in txt file
    #print gui.Dlg()
while True:
    userVar = {'Name':'Enter A First Name'}
    dlg = gui.DlgFromDict(userVar)
    userName = dlg.data[0].encode('ascii','ignore').strip()
    userName = userName.decode("utf-8")
    if userName in firstNames:
        break
    else:
        def popupError(text):
            errorDlg = gui.Dlg(title="Error", pos=(200,400))
            errorDlg.addText('Error: '+text, color='Red')
            errorDlg.show()
        popupError('Please enter a valid name.') 

    
#    """
#    the two line above are a more compact way of writing: 
#    names = open('names.txt', 'r').readlines()
#    firstNames=[]
#    for name in names:
#        firstNames.append(name.split(' ')[0])
#    """	
#    
win = visual.Window([800,600],color="black", units='pix')
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
stim = visual.TextStim(win, '+',color="white", colorSpace='rgb')
correctStim = visual.TextStim(win, 'O',color="green", colorSpace='rgb')
incorrectStim = visual.TextStim(win, 'X',color="red", colorSpace='rgb')

while True:
    stim.draw()
    win.flip()
    core.wait(.5)
    nameType = random.choice(["first","last"])
    
    if nameType == "first": #showing up 'b\Name'
        nameShown = userName
        correctKey='space'
    elif nameType == "first":
        nameShown = random.choice(firstNames)
        correctKey='f'
    elif nameType=="last": 
        nameShown = random.choice(lastNames)
        correctKey='l'  
    
    nameStim.setText(nameShown)   
    nameStim.draw()
#    if nameShown == userInput:
#        correctKey='space'
    core.wait(.3)
    win.flip()
    keypress=event.waitKeys(maxWait=1.0,keyList=['q',correctKey,'l','f','space'])
    #core.wait(.75)
    #event.waitKeys(keyList=[correctKey])
    if keypress == [correctKey]:
        correctStim.draw()
        win.flip()
        core.wait(.5)
    else:
        incorrectStim.draw()
        win.flip()
        core.wait(.5)
#    #    core.start(1.0)
#    # if keypress == ['']:
#    #        
#    #        incorrectStim.draw()
#    #        win.flip
#    #       core.wait(.5)
        if keypress==['q']: #a little bug-y, need to double tap q to close
            win.close()
            sys.exit()