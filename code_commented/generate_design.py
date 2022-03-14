#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Original Script by
@author: G. Aguilar, June 2020
updated: Jan 2021

slightly updated
"""

# The Main Function should be called with 1  Argument, the Initials of the Observer.

# import packages
import itertools
import random
import numpy as np
import pandas as pd
import random
import sys
import os

# import local files
import variables as var

# set variables
nRep = var.nRep
conditionNames = var.conditionNames
numberConditions = var.numberConditions
numberCompressions = var.numberCompressions
imageEnding = var.imageEnding
numberImages = var.numberImages


#   Chooses random in what order element 0 and 2 will be returned
#   List[1] will aways stay the same
def shuffle_triad(t):
    # in    t       List        At least 3 items long, could be longer but all items above number 3 will get lost               ie. ["a", "b", "c"] or [1, 2, 3] or ...
    # out   t1      Any         List item 0 or 2 from t                                                                         ie.  "a"  or   "c"  or  1  or 3  or ...
    # out   t2      Any         List item 1 from t                                                                              ie.       "b"       or     2     or ...
    # out   t3      Any         List item 0 or 2 from t                                                                         ie.  "a"   or  "c"  or  1  or 3  or ...
    
    # randomly chooses if triad is increasing or decreasing
    if random.randint(0,1)==1:
        t1 = t[0]
        t2 = t[1]
        t3 = t[2]
    else:
        t1 = t[2]
        t2 = t[1]
        t3 = t[0]
        
    return (t1, t2, t3)


#   Iterates over List of x Lists, making combinations of 3 elements of the list and shuffling item 0 and 2
def create_design_triads(v):
    # in    conditions  List        List of a number of lists equal to the number of Conditions each containing Filepaths ..                    ie. [["resources/1/r_0_art_rain.jpeg", ...]["resources/1/r_0_rain.jpeg"..][..]]
    #                               .. of all compressions of one image of the condtion
    # out   data        Dict        Dict of 3 Lists. Each list is the place on the trial (top right, top left, bottom). ..
    #                               .. each List tells us at what point of the trial what image will be shown at that place
        
    trials = list(itertools.combinations(v, 3))
    
    s1 = []
    s2 = []
    s3 = []
    for t in trials:
        t1, t2, t3 = shuffle_triad(t)
        
        s1.append(t1)
        s2.append(t2)
        s3.append(t3)
        
    data = {'S1': s1, 'S2': s2, 'S3': s3}

    return data

#   returns List of the filepaths of all conditions and compressions of one base image
#   ie. if we have 3 conditions, "rain", "norain" and "art_rain" and 6 compression levels and we call this function for image 1 ...
#   a list with 3*6 = 18 images will be returned containing all combinations of conditions and compressions for image 1
def getConditions(imageName):
    # in    imageName   String      For what base image do we want the files? In the experiments all conditions of 1 image will be run ..       ie. "1" or "2" or ...
    #                               ... in the same trial, but diffrent images will be seperate trials and runs
    # out   conditions  List        List of a number of lists equal to the number of Conditions each containing Filepaths ..                    ie. [["resources/1/r_0_art_rain.jpeg", ...]["resources/1/r_0_rain.jpeg"..][..]]
    #                               .. of all compressions of one image of the condtion
    
    conditions = []
    for conditionNumber in range(numberConditions):
        conditionName = conditionNames[conditionNumber]
        conditions.append([])
        for compressionNumber in range(numberCompressions):
            fileName = "resources/%s/r_%s_%s%s" % (imageName, str(compressionNumber), conditionName, imageEnding)
            conditions[conditionNumber].append(fileName)
    return conditions


#   Main Function that creates trials for all images for all repetitions for 1 Observer
def doMain(observer):
    # in    observer    String      Name or Initials or other Identifyer of the Observer                ie. "LB" or "Leonie" or "TP01" or "Testperson1"
    # out   --

    for imageNumber in range(numberImages):
        imageName = str(imageNumber + 1)
        conditions = getConditions(imageName)
        outputPath = "output/%s/%s/" % (imageName, observer)
        if not os.path.exists(outputPath):
            os.makedirs(outputPath)
        for rep in range(nRep):
            
            # trials will be a List of strings, containting imagePaths for all compressions and conditions for the current base image
            trials = [create_design_triads(cond) for cond in conditions]

            # creates pandas Dataframe for all trials in each condition
            dd = []
            for i in range(len(conditions)):
                d = pd.DataFrame(trials[i])
                dd.append(d) 
            # joins the conditions
            df = pd.concat(dd)  
            # shuffles order
            df.reset_index(drop=True, inplace=True)
            df = df.reindex(np.random.permutation(df.index))
            df.reset_index(drop=True, inplace=True)
            df.index.name = 'Trial'
            
            # save in design folder, under block number
            df.to_csv('%sdesign_%s_%s_%d.csv' % (outputPath, observer, "triads", rep), index=False)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        observer = sys.argv[1]
        doMain(observer)
    else:
        print('Error, no argument given, please add observer Initials')

    