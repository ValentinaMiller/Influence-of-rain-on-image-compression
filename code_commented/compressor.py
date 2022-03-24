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
