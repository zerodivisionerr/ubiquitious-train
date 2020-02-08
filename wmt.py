
# coding: utf-8

# In[1]:


import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from customplot import *


# In[2]:


wmt_dict = {'Exercise': {0: 'pushups',
    1: 'chest press',
    2: 'bicep curl',
    3: 'tricep extension',
    4: 'weighted_row',
    5: 'chest fly',
    6: 'treadmill',
    7: 'stair machine',
    8: 'elliptical',
    9: 'squat',
    10: 'leg curl',
    11: 'leg extension',
    12: 'deadlift',
    13: 'chinup',
    14: 'plank',
    15: 'lat pulldown'},
    'Push': {0: True,
    1: True,
    2: False,
    3: False,
    4: False,
    5: True,
    6: False,
    7: False,
    8: False,
    9: False,
    10: False,
    11: True,
    12: False,
    13: False,
    14: False,
    15: False},
    'Pull': {0: False,
    1: False,
    2: True,
    3: False,
    4: True,
    5: False,
    6: False,
    7: False,
    8: False,
    9: False,
    10: True,
    11: False,
    12: False,
    13: True,
    14: False,
    15: True},
    'Arms': {0: True,
    1: True,
    2: True,
    3: False,
    4: False,
    5: True,
    6: False,
    7: False,
    8: False,
    9: False,
    10: False,
    11: False,
    12: False,
    13: True,
    14: False,
    15: True},
    'Chest': {0: True,
    1: True,
    2: False,
    3: False,
    4: False,
    5: True,
    6: False,
    7: False,
    8: False,
    9: False,
    10: False,
    11: False,
    12: False,
    13: False,
    14: False,
    15: False},
    'Back': {0: False,
    1: False,
    2: False,
    3: False,
    4: True,
    5: False,
    6: False,
    7: False,
    8: False,
    9: False,
    10: False,
    11: False,
    12: False,
    13: True,
    14: False,
    15: True},
    'Legs': {0: False,
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    6: False,
    7: False,
    8: False,
    9: True,
    10: True,
    11: True,
    12: False,
    13: False,
    14: False,
    15: False},
    'Core': {0: True,
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    6: False,
    7: False,
    8: False,
    9: False,
    10: False,
    11: False,
    12: False,
    13: True,
    14: True,
    15: False},
    'Cardio': {0: False,
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    6: True,
    7: True,
    8: True,
    9: False,
    10: False,
    11: False,
    12: False,
    13: False,
    14: False,
    15: False},
    'Favorite': {0:False,
    1:False,
    2:False,
    3:False,
    4:False,
    5:False,
    6:False,
    7:False,
    8:True,
    9:False,
    10:False,
    11:False,
    12:False,
    13:False,
    14:False,
    15:False}
}


# In[3]:


#Print Push Exercises From Dictionary
for e in wmt_dict['Exercise']:
    if (wmt_dict['Push'][e] == True):
        print (wmt_dict['Exercise'][e])


# In[4]:


#Print Pull Exercises From Dictionary
for e in wmt_dict['Exercise']:
    if (wmt_dict['Pull'][e] == True):
        print (wmt_dict['Exercise'][e])


# In[5]:


#Print Cardio Exercises From Dictionary
for e in wmt_dict['Exercise']:
    if (wmt_dict['Cardio'][e] == True):
        print (wmt_dict['Exercise'][e])


# In[6]:


#Print Arm Exercises From Dictionary
for e in wmt_dict['Exercise']:
    if (wmt_dict['Arms'][e] == True):
        print (wmt_dict['Exercise'][e])


# In[7]:


#Print Leg Exercises From Dictionary
for e in wmt_dict['Exercise']:
    if (wmt_dict['Legs'][e] == True):
        print (wmt_dict['Exercise'][e])


# In[8]:


#Print Chest Exercises From Dictionary
for e in wmt_dict['Exercise']:
    if (wmt_dict['Chest'][e] == True):
        print (wmt_dict['Exercise'][e])


# In[9]:


#Print Back Exercises From Dictionary
for e in wmt_dict['Exercise']:
    if (wmt_dict['Back'][e] == True):
        print (wmt_dict['Exercise'][e])


# In[10]:


#Print Back Exercises From Dictionary
for e in wmt_dict['Exercise']:
    if (wmt_dict['Favorite'][e] == True):
        print (wmt_dict['Exercise'][e])


# In[11]:


#Add New Exercise and Set True/False per 
#wmt_dict['Exercise'][15] = 'lat_pulldown'
#wmt_dict['Back'][15] = True
#wmt_dict['Pull'][15] = True
#wmt_dict['Push'][15] = False
#wmt_dict['Arms'][15] = True
#wmt_dict['Legs'][15] = False
#wmt_dict['Cardio'][15] = False
#wmt_dict['Core'][15] = False
#wmt_dict['Chest'][15] = False


# In[12]:


#Add Exercise to wmt_dict
def addExer(name, push, pull, arms, chest, back, legs, core, cardio, favorite):
    if (name not in wmt_dict['Exercise'].values()):
        wmt_dict['Exercise'][len(wmt_dict['Exercise'])] = name
        wmt_dict['Push'][len(wmt_dict['Exercise'])] = push
        wmt_dict['Pull'][len(wmt_dict['Exercise'])] = pull
        wmt_dict['Arms'][len(wmt_dict['Exercise'])] = arms
        wmt_dict['Chest'][len(wmt_dict['Exercise'])] = chest
        wmt_dict['Back'][len(wmt_dict['Exercise'])] = back
        wmt_dict['Legs'][len(wmt_dict['Exercise'])] = legs
        wmt_dict['Core'][len(wmt_dict['Exercise'])] = core
        wmt_dict['Cardio'][len(wmt_dict['Exercise'])] = cardio
        wmt_dict['Favorite'][len(wmt_dict['Exercise'])] = favorite


# In[13]:


addExer('kick_backs', True, False, False, False, False, True, False, False, False)
wmt_dict


# In[14]:


my_prog = {'Date':
               {0: '02/08/2020'},
           'Exercise' : 
               {0: 'pushups'},
           'Sets':
               {0: 3},
           'Reps':
               {0: 15},
           'Weight':
               {0: None},
           'Speed':
               {0: None},
           'Distance':
               {0: None},
            'Duration':
               {0: None},
           'Difficulty':
               {0: 3},
           'Enjoyability':
               {0: 7}
          }


# In[15]:


my_prog


# In[16]:


#Add Progress Entry to my_prog Dict
def addProg(date, name, sets, reps, weight, speed, distance, duration, difficulty, enjoyability):
    my_prog['Date'][len(my_prog['Enjoyability'])] = date 
    my_prog['Exercise'][len(my_prog['Enjoyability'])] = name
    my_prog['Sets'][len(my_prog['Enjoyability'])] = sets
    my_prog['Reps'][len(my_prog['Enjoyability'])] = reps
    my_prog['Weight'][len(my_prog['Enjoyability'])] = weight
    my_prog['Speed'][len(my_prog['Enjoyability'])] = speed
    my_prog['Distance'][len(my_prog['Enjoyability'])] = distance
    my_prog['Duration'][len(my_prog['Enjoyability'])] = duration
    my_prog['Difficulty'][len(my_prog['Enjoyability'])] = difficulty
    my_prog['Enjoyability'][len(my_prog['Enjoyability'])] = enjoyability


# In[17]:


addProg('02/08/2020', 'treadmill', None,None,None,0,3, 1, 3, 7)
my_prog


# In[31]:


# function to return key for any value 
def get_key(val): 
    for key, value in my_prog['Exercise'].items(): 
        if val == value:
            return (key) 
  
    print ("key doesn't exist")


# In[32]:


get_key('pushups')


# In[33]:


def diffIncr(exercise):
    if (exercise != Cardio):
        reps = reps * .20
        #count number of entries or weeks of doing exercise
        #increase count times 20% to
        #count number of increments to sets, reps, and weight
        #increase reps first, then increase weight and lower reps back to base
        reps = reps_base
        reps_count += 1
        weight = weight * .20
        weight_count += 1
        
    else:
        distance = my_prog[Distance][1]
        distance = distance * .20
        speed = speed * .20
        #increase distance by increment times 20% first 
        #then maintain speed but increase time/distance
        #alternate
        print (distance)


# In[50]:


def suggestedIncr(exercise):
    if (exercise in my_prog['Exercise']):
        #grab date of most recent entry of that exercise
        #use that index to find the difficulty of that entry
        if (difficulty < 3 & wmt_dict['Cardio'][key==exercise]):
            diffIncr(exercise)
    
    difficulty = my_prog['Difficulty'][get_key(exercise)]
    distance = my_prog['Distance'][get_key(exercise)]
    print("Suggested Distance for next time: " + str(distance * 1.2))
    #difficulty = my_prog[wm]
        


# In[51]:


suggestedIncr('treadmill')


# In[25]:


my_prog['Exercise'][1] = 'treadmill'
my_prog['Exercise'][1]


# In[46]:


my_prog['Difficulty'][1]


# In[47]:


my_prog['Reps'][1]


# In[28]:


my_prog


# In[29]:


#Print Entry in my_prog
def printEntry(locationInteger):
    for item in my_prog:
        print (my_prog[item][locationInteger])


# In[30]:


printEntry(0)

