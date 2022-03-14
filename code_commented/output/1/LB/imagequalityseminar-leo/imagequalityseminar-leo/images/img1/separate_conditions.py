#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Step 4: Separate the conditons

The experiment was run with conditions intermixed randomly. Now we need to separate
the trials per condition, to later feed those files into R

Change the variables files, mappingA, B... conditions and condnames
as necessary (lines 24 - 48)

After running this script, you will have the CSV files ready to be analyzed with R

After separating, continues with the R script 
--> mlds_analysis.R


@author: 
"""

import pandas as pd

######################################################################
####### change the follwing variables as necessary
# list all the results files
files = ['design_LB_triads_0_results.csv', 'design_LB_triads_1_results.csv',  'design_LB_triads_2_results.csv', 'design_LB_triads_3_results.csv', 'design_LB_triads_4_results.csv']

# mapping: stimuli filenames --> stimulus vector, starting at one 
# (vectors in R start at one, not like in python)
# Here you should put the order of the stimuli you chose
mappingA = {'r_0_norain.jpeg': 1,
            'r_1_norain.jpeg': 2,
            'r_2_norain.jpeg': 3,
            'r_3_norain.jpeg': 4,
            'r_4_norain.jpeg': 5,
            'r_5_norain.jpeg': 6}

mappingB = {'r_0_rain.jpeg': 1,
            'r_1_rain.jpeg': 2,
            'r_2_rain.jpeg': 3,
            'r_3_rain.jpeg': 4,
            'r_4_rain.jpeg': 5,
            'r_5_rain.jpeg': 6}
            
mappingC = {'r_0_art_rain.jpeg': 1,
            'r_1_art_rain.jpeg': 2,
            'r_2_art_rain.jpeg': 3,
            'r_3_art_rain.jpeg': 4,
            'r_4_art_rain.jpeg': 5,
            'r_5_art_rain.jpeg': 6}

## extend if you have more conditions 
conditions = [mappingA, mappingB, mappingC] # extend this list if necessary
condnames = ['norain', 'rain', 'art_rain']       # names of the conditons. 
# the processed files will be saved using these suffixes

######################################################################
######################################################################

# iterate through files
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
        
        # ... to be read by R
        
    
# EOF
    
