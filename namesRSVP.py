# Display some text, take in responses, read from a file

# 1: Make the fixation cross appear before each name and disappears right before the name comes up

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
    
    
#2 Make the script show last names instead of first names
import time
import sys
import random
from psychopy import visual,event,core


names = open('names.txt', 'r').readlines()
lastNames = [name.split(' ')[1] for name in names] #1 indicates second column in txt file

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
lastNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
stim = visual.TextStim(win, '+',color="white", colorSpace='rgb')
while True:
    stim.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(lastNames)
    lastNameStim.setText(nameShown)   
    lastNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)
    
    if event.getKeys(['q']):
        win.close()
        sys.exit()

#3 Make the program randomly alternate between first names and last names.
import time
import sys
import random
from psychopy import visual,event,core


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names] #0 represents first column in txt file
lastNames = [name.split(' ')[1] for name in names] #1 indicates second column in txt file

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
#firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
#lastNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])

stim = visual.TextStim(win, '+',color="white", colorSpace='rgb')
while True:
    stim.draw()
    win.flip()
    core.wait(.5)
    i = random.choice([0,1])
#    if i == 0:
#        nameShown = random.choice(firstNames)
#        firstNameStim.setText(nameShown)   
#        firstNameStim.draw()
#    else: 
#        nameShown = random.choice(lastNames)
#        lastNameStim.setText(nameShown)   
#        lastNameStim.draw()
        
    if i == 0:
        nameShown = random.choice(firstNames)
    else: 
        nameShown = random.choice(lastNames)
    
    nameStim.setText(nameShown)   
    nameStim.draw()

    core.wait(.5)
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)
    
    if event.getKeys(['q']):
        win.close()
        sys.exit()

# 4: wait for a response and only proceed to the next name if the response is correct
import time
import sys
import random
from psychopy import visual,event,core


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names] #0 represents first column in txt file
lastNames = [name.split(' ')[1] for name in names] #1 indicates second column in txt file

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
stim = visual.TextStim(win, '+',color="white", colorSpace='rgb')
while True:
    stim.draw()
    win.flip()
    core.wait(.5)
    nameType = random.choice(["first","last"])
    if nameType == "first":
        nameShown = random.choice(firstNames)
        correctKey='f'
    else: 
        nameShown = random.choice(lastNames)
        correctKey='l'
        
    nameStim.setText(nameShown)   
    nameStim.draw()
    core.wait(.5)
    win.flip()
    #core.wait(.75)
    #event.waitKeys(keyList=[correctKey])
    keypress=event.waitKeys(keyList=[correctKey,'q'])

    if keypress==['q']:
        win.close()
        sys.exit()
        
    win.flip()
    core.wait(.15)  


#    if event.getKeys(['q']):
#        win.close()
#        sys.exit()


# 5: Now let's implement some feedback. Show the feedback for 500 ms.
import time
import sys
import random
from psychopy import visual,event,core


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names] #0 represents first column in txt file
lastNames = [name.split(' ')[1] for name in names] #1 indicates second column in txt file

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

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
    if nameType == "first":
        nameShown = random.choice(firstNames)
        correctKey='f'
    else: 
        nameShown = random.choice(lastNames)
        correctKey='l'
        
    nameStim.setText(nameShown)   
    nameStim.draw()
    core.wait(.3)
    win.flip()
    keypress=event.waitKeys(keyList=['q',correctKey,'l','f'])
 
    if keypress == [correctKey]:
        correctStim.draw()
        win.flip()
        core.wait(.5)
    else:
        incorrectStim.draw()
        win.flip()
        core.wait(.5)
    if keypress==['q']: #a little bug-y, need to double tap q to close
        win.close()
        sys.exit()

#6: Now, instead of waiting for a response forever, let's implement a timeout.
# unknowingly have been importing psychopy clock via core, now I know what core does

import time
import sys
import random
from psychopy import visual,event,core


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names] #0 represents first column in txt file
lastNames = [name.split(' ')[1] for name in names] #1 indicates second column in txt file

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

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
    if nameType == "first":
        nameShown = random.choice(firstNames)
        correctKey='f'
    else: 
        nameShown = random.choice(lastNames)
        correctKey='l'
        
    nameStim.setText(nameShown)   
    nameStim.draw()
    core.wait(.3)
    win.flip()
    keypress=event.waitKeys(maxWait=1.0,keyList=['q',correctKey,'l','f'])
  
    if keypress == [correctKey]:
        correctStim.draw()
        win.flip()
        core.wait(.5)
    else:
        incorrectStim.draw()
        win.flip()
        core.wait(.5)

    if keypress==['q']: #a little bug-y, need to double tap q to close
        win.close()
        sys.exit()

# 7: Pop up a box that accepts a first name ... pop-up a 'Name does not exist'error box
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
    userInput = dlg.data[0].encode('ascii','ignore').strip()
    if userInput in firstNames:
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
    if nameType == "first":
        nameShown = random.choice(firstNames)
        correctKey='f'
    else: 
        nameShown = random.choice(lastNames)
        correctKey='l'
        
    nameStim.setText(nameShown)   
    nameStim.draw()
    core.wait(.3)
    win.flip()
    keypress=event.waitKeys(maxWait=1.0,keyList=['q',correctKey,'l','f'])
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
            
# 8: Extend the task by requiring the subject to respond by pressing a spacebar 
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
# 9: compute the response times on trials
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
    win.flip()
    timer = core.Clock()
    timer.reset(newT=0.0)
#    if nameShown == userInput:
#        correctKey='space'
#    core.wait(.3)
#    win.flip()
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
        timer.getTime()*1000
        print timer.getTime()* 1000
#    #    core.start(1.0)
#    # if keypress == ['']:
#    #        
#    #        incorrectStim.draw()
#    #        win.flip
#    #       core.wait(.5)
        if keypress==['q']: #a little bug-y, need to double tap q to close
            win.close()
            sys.exit()   
# 10: 
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
    f = open('output.txt', 'w')
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
    win.flip()
    timer = core.Clock()
    timer.reset(newT=0.0)
#    if nameShown == userInput:
#        correctKey='space'
#    core.wait(.3)
#    win.flip()
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
        timer.getTime()*1000
        print timer.getTime()* 1000
    React = timer.getTime()*1000
    f.write(str(int(keypress==correctKey))+'\t'+ str(keypress) + '\t' + str(React)+'\n') 
    f.flush()
#    #    core.start(1.0)
#    # if keypress == ['']:
#    #        
#    #        incorrectStim.draw()
#    #        win.flip
#    #       core.wait(.5)
    if keypress==['q']: #a little bug-y, need to double tap q to close
            win.close()
            sys.exit()

# 11: Do something new
        