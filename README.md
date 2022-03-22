# Rain and Image Compression 

## 1. Introduction
Our project aims to examine the effect induced by rain on the perceived quality of images when compressed. In order to study such an effect, we make use of comparable images that illustrate sceneries reflecting *clear* and *rainy* states. We hypothesize that rain causes a difference in the perceived quality of a compressed image and conduct an MLDS experiment with the method of triads to test our hypothesis. 

## 2. Experimental design
In each trial of the MLDS experiment, the observer is presented with three compressed versions of a picture depicting a single state (rainy or clear weather). Six compression levels are used: $`50\%, 58\%, 66\%, 74\%, 82\%`$ and $`90\%`$. For each of our $`4`$ pictures, an observer has to complete $`3`$ runs, in each of which they are presented with $`60`$ comparisons, totalling $`720`$ trials per observer. Overall, $`9`$ observers have taken the experiment. 

### 2.1 Stimuli 
The stimuli consist primarily of four different pairs of pictures with each pair comprising a clear and a rainy weather photograph. We also added an extra layer to our experiment by artificially simulating raindrops and consequently enabling a perfect comparison to the original clear weather picture. 

<div align="center">
![stimuli](https://i.imgur.com/2pMtrij.png)
</div>

#### 2.1.1 Search for pictures  
In order to lay the groundwork for a sensible experiment, the stimuli had to fulfil certain criteria, that is, any pair of pictures of rainy and clear weather had to be... 

 1. taken at the same location (to reflect the same scenery) 
 2. taken within small time intervals (to account for dynamically changing landscapes) 
 3. taken by the same camera (to avoid inconsistencies in image quality)
 4. ideally of the same brightness level (to minimize the effects of perceived brightness)

The stimuli were therefore obtained from weather cameras ([foto-webcam.eu](https://www.foto-webcam.eu/webcam)) as they presented the most viable choice. However, the decision to use such cameras also posed its own challenges. The pictures of rainy weather had to captured at the perfect moment in time such that  raindrops are visible but not falling on the camera lens and obscuring the scenery or causing an out-of-focus image. Naturally, finding such pictures has proven to be difficult and time consuming. To ease this task and narrow our scope of search, we collected weather data of different regions to determine the points in time in which rainfall was especially high and used them as reference points while searching for pictures. For example, "Image 1" was taken on 16.08.2021 in Fürstenfeldbruck where the region's weather data showed a peak in precipitation: 
<div align="center">
![weather_fuerstenfeldbruck](https://i.imgur.com/sqdB4wb.png)
</div>

In the following we demonstrate examples of violated criteria: 

<div align="center">
![violations](https://i.imgur.com/1QEHfzE.png)
</div>

#### 2.1.2 Cropping  
Each pair of stimuli pictures (rain/no rain) had to be manually cropped for two main reasons: 
 1. Reducing differences: Raindrops should ideally be the only factor differentiating the pair. Any other visible dissimilarities or moving objects had to be cut out.
 2. Setting a practical uniform size of $`350`$x$`350`$ pixels which allows the MLDS experiment to be executed on smaller monitors. 

The cropping process had to be pixel-perfect to guarantee that the resulting pictures in each pair reflected the same scenery. To achieve this, every two pictures comprising a pair were layered on top of one another and cropped together simultaneously. 

<div align="center">
![image 1 cropping](https://i.imgur.com/ZpN7cND.png)![image 2 cropping](https://i.imgur.com/IJWOmfK.png)![image 3 cropping](https://i.imgur.com/aOOq57j.png)![image 4 cropping](https://i.imgur.com/BeozHT1.png)
</div>

#### 2.1.3 Artificial rain
Rain effects were simulated by adding gaussian monochromatic noise to clear weather pictures and applying blending techniques. For the purposes of our experiment, we use a consistent amount of noise at $`35\%`$ and do not consider other variables like the fall angle or the size of raindrops. 

#### 2.1.4 Compression
The stimuli images were compressed into JPEG format using Python's PIL (Python Imaging Library). Since PIL's quality parameter runs from $`95`$ (best possible quality) to $`1`$ (worst possible quality), the following function was used to translate compression percentages into their corresponding quality values: 
```math 
f: \mathbb{N} \to \mathbb{N}, f(x) = \lceil\mid95 -(\frac{x}{100} \cdot 95)\mid\rceil
```
where $`x`$ is the desired compression percentage. The compression was then implemented using the script `compressor.py`: 

```python # Usage: Run the script from a directory that includes .bmp, .jpg or .jpeg images.
 # Usage: Run the script from a directory that includes .bmp, .jpg or .jpeg images.

from PIL import Image
import os 

images = [file for file in os.listdir() if file.endswith(('bmp','jpg', 'jpeg'))]

for i in images:
    curr = Image.open(i)
    # The "quality" parameter: A scale from 0 (worst) to 95 (best). See Pillow's documentation (https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html?#jpeg)
    compression_levels = [47.5, 39.9, 32.3, 24.7, 17.1, 9.5]
    percent = 0 
    for x in compression_levels:
    	# Output file name: [image name]_compressed_[compression level]
    	if (x == 47.5): percent = 50
    	elif (x == 39.9): percent = 58
    	elif (x == 32.3): percent = 66
    	elif (x == 24.7): percent = 74
    	elif (x == 17.1): percent = 82
    	elif (x == 9.5): percent = 90
    	curr.save(i + "_compressed_" + str(percent) + ".jpeg", format='JPEG', quality=round(x))
 ```
The complete set of compressed images is shown below.  

|Compression level|Clear|Rain| Rain (artificial)|
|:-:|:-:|:-:|:-:|
|0.5|![pic](https://i.imgur.com/QovOgxm.jpg)|![pic](https://i.imgur.com/PBfJiUm.jpg)|![pic](https://i.imgur.com/wIEBtga.jpg)|
|0.58|![pic](https://i.imgur.com/UwVfrIN.jpg)|![pic](https://i.imgur.com/iX1Vjdm.jpg)|![pic](https://i.imgur.com/tZWtYbS.jpg) |
|0.66|![pic](https://i.imgur.com/svLeNr0.jpg)|![pic](https://i.imgur.com/rovsEax.jpg)| ![pic](https://i.imgur.com/IvkEjKu.jpg)|
|0.74|![pic](https://i.imgur.com/ABvgvJf.jpg)|![pic](https://i.imgur.com/Z3XM5Bp.jpg)| ![pic](https://i.imgur.com/77qopKs.jpg)|
|0.82|![pic](https://i.imgur.com/cDiWVzq.jpg)|![pic](https://i.imgur.com/P3XTE3D.jpg)| ![pic](https://i.imgur.com/mXVgAeJ.jpg)|
|0.9|![pic](https://i.imgur.com/G13YGWQ.jpg)|![pic](https://i.imgur.com/wr0UDDD.jpg)| ![pic](https://i.imgur.com/F0KOq09.jpg)|

|Compression level|Clear|Rain| Rain (artificial)|
|:-:|:-:|:-:|:-:|
|0.5|![pic](https://i.imgur.com/S6s8r71.jpg)|![pic](https://i.imgur.com/MVlldQc.jpg)|![pic](https://i.imgur.com/pxsaedL.jpg)|
|0.58|![pic](https://i.imgur.com/s9LJX6B.jpg)|![pic](https://i.imgur.com/YVOIMZt.jpg)|![pic](https://i.imgur.com/znlpfRw.jpg) |
|0.66|![pic](https://i.imgur.com/BYYOQD7.jpg)|![pic](https://i.imgur.com/5jVvwLx.jpg)| ![pic](https://i.imgur.com/5VteQLu.jpg)|
|0.74|![pic](https://i.imgur.com/C1lGRqY.jpg)|![pic](https://i.imgur.com/w6RFl10.jpg)| ![pic](https://i.imgur.com/tWpOPaV.jpg)|
|0.82|![pic](https://i.imgur.com/UDLmONs.jpg)|![pic](https://i.imgur.com/g7vMp5x.jpg)| ![pic](https://i.imgur.com/U7fzXix.jpg)|
|0.9|![pic](https://i.imgur.com/SFshFM9.jpg)|![pic](https://i.imgur.com/ghWRPCG.jpg)| ![pic](https://i.imgur.com/oX2YCl3.jpg)|

|Compression level|Clear|Rain| Rain (artificial)|
|:-:|:-:|:-:|:-:|
|0.5|![pic](https://i.imgur.com/QUcIMyk.jpg)|![pic](https://i.imgur.com/78u9AG5.jpg)|![pic](https://i.imgur.com/CagcHGc.jpg)|
|0.58|![pic](https://i.imgur.com/Gl6w8IV.jpg)|![pic](https://i.imgur.com/4mTimSb.jpg)|![pic](https://i.imgur.com/8MUIBqY.jpg) |
|0.66|![pic](https://i.imgur.com/zcykkeA.jpg)|![pic](https://i.imgur.com/xG6Zs5n.jpg)| ![pic](https://i.imgur.com/ofrb9ew.jpg)|
|0.74|![pic](https://i.imgur.com/e22Ae9J.jpg)|![pic](https://i.imgur.com/WqE1Hjv.jpg)| ![pic](https://i.imgur.com/KLONJOI.jpg)|
|0.82|![pic](https://i.imgur.com/NIgSaCW.jpg)|![pic](https://i.imgur.com/0pQCL6W.jpg)| ![pic](https://i.imgur.com/7pkHY4j.jpg)|
|0.9|![pic](https://i.imgur.com/Dqqa7HN.jpg)|![pic](https://i.imgur.com/81prexJ.jpg)| ![pic](https://i.imgur.com/HfwCra2.jpg)|

|Compression level|Clear|Rain| Rain (artificial)|
|:-:|:-:|:-:|:-:|
|0.5|![pic](https://i.imgur.com/4HwZnRn.jpg)|![pic](https://i.imgur.com/edesODO.jpg)|![pic](https://i.imgur.com/7h7iTiR.jpg)|
|0.58|![pic](https://i.imgur.com/u5n4eC3.jpg)|![pic](https://i.imgur.com/vdqoeW7.jpg)|![pic](https://i.imgur.com/MAh5E5E.jpg) |
|0.66|![pic](https://i.imgur.com/lmTf2Ti.jpg)|![pic](https://i.imgur.com/Fz0Hy6G.jpg)| ![pic](https://i.imgur.com/eWR0V9B.jpg)|
|0.74|![pic](https://i.imgur.com/zjZyXsM.jpg)|![pic](https://i.imgur.com/hRe7tDv.jpg)| ![pic](https://i.imgur.com/li3cYaq.jpg)|
|0.82|![pic](https://i.imgur.com/UAARg7r.jpg)|![pic](https://i.imgur.com/q967cF8.jpg)| ![pic](https://i.imgur.com/kr1WFSJ.jpg)|
|0.9|![pic](https://i.imgur.com/aMw1hOC.jpg)|![pic](https://i.imgur.com/hPrsqx6.jpg)| ![pic](https://i.imgur.com/STJ101i.jpg)|

### 2.2 Implementation  

## 3. Results

## 4. Discussion

## 5. Instructions to recreate the experiment
Following this, you too can easily replicate our experiment or create your own with whatever images you want!

### Setting up
- checking variables
- checking reference images
    - checking image names

### Instructions if you want to use your own images
- Replace the values of the variables in `variables.py` if necessary
- Replace the pictures in `resources/` but make sure to use the correct name
    - The base image names have to start at 1 and count up, don't leave one out
    - name should be like this: `r_<compressionNumber>_<conditionName>.jpeg`. You can change the image type, but make sure to change the variable in `variables.py`
        - compressionNumber starts at 0 and counts up
        - conditionName can be anything, but has to be added in the variable in `variable.py`
        - you have to have an image for each compression for each condition you set in `variables.py`

### Running the code
1. run `generate_design.py`
    - Argument:
        - Your initials, make sure they are not already used. You can do this by going into `output/1/` and checking if there already is a folder with your initials. If there is one, just change it until there is no folder with this name.
2. run `mlds_experiment_triads.py`
    - Arguments:
        - same initials you used in 1
        - what image you are doing the experiment in (1,2,3,4)
        - in what repetition you are (0,1,2)
    - run this with each image and repetition combination, first iterating over all repetitions for one image and if you've done all repetitions for one image, move on to the next image.
3. run `seperate_conditions.py`
    - Arguments:
        - same initials you used in 1
        - what image you are separating the conditions for (1,2,3,4)
    - Do this for each image you've done all trials for with `mlds_experiment_triads.py`
    - You have to run this code once for each image, so that you can do the experiment on just one image and still get the results. 
4. run `mlds_analysis.R`
    - No Arguments
    - Run this once per observer and image
    - Copy this file into `/output/<imageName>/<observerInitials>/`
    - There replace the path in the file with the path where the file is now
    - Replace the observer in the file if necessary
    - Now you can run the file
