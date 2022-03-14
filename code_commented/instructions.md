# Triads Experiment with multiple Base Image

## Everything except the code
### Motivation
Our goal was to figure out, how rain affects the percieved Image Quality of a Picture if Compressed.

### Seach for images
For this we decided to use Weather Camera Pictures to get a wide rane of motives with and without rain. The weather Cameras have the big advantage of offering a vast selection of images with all sorts of weather conditions all taken from the exact same place.

#### Criteria For images
TBD

## Running The Code, Replicating our Experiments
Following this, you too can easily replicate our experiment or create your own with whatever images you want!

### Setting up
- checking variables
- checking refernce images
    - checking image names

### Instructions if you want to use your own images
- Replace the Values of the Varibles in variables.py if neccessary
- Replace the Pictures in resources/ but make sure to use the correct name
    - The Base image names have to start at 1 and count up, don't leave one out 
    - name sould be like this: r_<compressionNumber>_<conditionName>.jpeg . You can change the image type, but make sure to change the variable in variables.py
        - compressionNumber starts at 0 and counts up
        - conditionName can be anything, but has to be added in the variable in variable.py
        - you have to have an image for each compression for each condition you set in variables.py

### Runnig Code
1. run generate_design.py
    - Argument
        - Your Initials, make sure they are not alredy used. You can do this by going into output/1/ and check if there already is a folder with your initials. If there is one, just change it until there is no folder with this name.
2. run mlds_experiment_triads.py
    - Arguments:
        - same initials you used in 1
        - what image you are doing the experiment in (1,2,3,4)
        - in what repetition you are (0,1,2)
    - run this with each image and repetion combination, first iterating over all repetitions for one image and if you've done all repetitions for one image, move on to the next image.
3. run seperate_conditions.py
    - Arguments:
        - same initials you used in 1
        - what image you are seperating the conditions for (1,2,3,4)
    - Do this for each Imae you've done all trials for with mlds_experiment_triads.py
    - You have to run this code once for each image, so that you can do the experiment on just one image and still get the results. 
4. mlds_analysis.py
    - no Arguments
    - Run this once per Observer and Image
    - Copy this file into /output/<imageName>/<observerInitials>/
    - There replace the Path in the file to the path where the file is now
    - Replace the Observer in the File if neccessary
    - Now you can run the file