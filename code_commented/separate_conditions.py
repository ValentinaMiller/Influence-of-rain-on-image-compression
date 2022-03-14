#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Original Script by
@author: G. Aguilar

slightly updated
"""

# The Main Function should be called with 1  Argument, the Initials of the Observer.

# importing Packages
import pandas as pd
import sys

# importing local Files
import variables as var

# setting Variables
nRep = var.nRep
condnames = var.conditionNames
numberCondtions = var.numberConditions
numberCompressions = var.numberCompressions


#   returns the trial result files for all repetitions
def getFiles(observer, imageName):
    # in    observer    String      Name or initial of the observer                         ie. "LB" or "Leonie" or ...
    # in    imageName   String      Name of the Base image we seperate the condtions for    ie. "1" or "2" or ...
    # out   files       List        List of all trial result files of one image             ie. ["output/1/LB/design_LB_triads_0_results.csv", "output/1/LB/design_LB_triads_1_results.csv", "output/1/LB/design_LB_triads_2_results.csv"]
    
    files = []
    for rep in range(nRep):
        fileName = "output/%s/%s/design_%s_triads_%s_results.csv" % (imageName, observer, observer, str(rep))
        files.append(fileName)
    return files


#   Maps the Images to the compressions
#   Compressions count up from 1 to however many compressions you have. We start at 1, because vectors in R start at one
def getConditions(imageName):
    # in    imageName       String      Name of the Base image we seperate the condtions for                                ie. "1" or "2" or ...
    # out   conditions      List        List of Dictionarys, with the image Name as key and the compression as value        ie. [{"resources/1/r_0_norain.jpeg": 1, "resources/1/r_1_norain.jpeg": 2,...}, {"resources/1/r_0_rain.jpeg": 1, "resources/1/r_1_rain.jpeg": 2,...}, {...}]
    
    conditions = []
    for i in range(numberCondtions):
        conditions.append({})
        condname = condnames[i]
        for j in range(numberCompressions):
            key = "resources/%s/r_%s_%s.jpeg" % (imageName, str(j), condname)
            var = j + 1
            conditions[i][key] = var
            print(key)
            print(var)

    return conditions


#   Main Function. Seperates the results of the trials into each conditions to analyse them seperatly later.
def doMain(observer, imageName):
    # in    observer    String      Name or initial of the observer                         ie. "LB" or "Leonie" or ...
    # in    imageName   String      Name of the Base image we seperate the condtions for    ie. "1" or "2" or ...
    files = getFiles(observer, imageName)
    conditions = getConditions(imageName)

    # iterate through csv result files
    for f in files:
        print('** processing file: %s' % f)
        # opens file
        df = pd.read_csv(f)
        
        # iterate through conditions
        for c, mapping in enumerate(conditions):
            condname = condnames[c]
            
            # selects only the rows for the condition
            idx = (df['S3'].isin(list(mapping.keys()))) | (df['S1'].isin(list(mapping.keys())))
            slicedf = df[idx].copy()
            
            print('condition %s has %d trials' % (condname, len(slicedf)))
            
            # applies the mapping
            slicedf['S1'] = slicedf['S1'].map(mapping)
            slicedf['S2'] = slicedf['S2'].map(mapping)
            slicedf['S3'] = slicedf['S3'].map(mapping)
            try:
                slicedf['S4'] = slicedf['S4'].map(mapping)
                
            except:
                print('this is a triad experiment')
                
            # finally we save the newly coded file,
            fname = '%s_%s.csv' % (f.split('.')[0], condname)
            print('saving as: %s' % fname)
            print('')

            slicedf.to_csv(fname, index=False)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("Error, Just one Argument give, neccesary is observer initials AND Image Number!")
    elif len(sys.argv) > 2:
        observer = sys.argv[1]
        imageName = sys.argv[2]
        doMain(observer)
    else:
        print('Error, no argument given, please add observer Initials and image Number!')