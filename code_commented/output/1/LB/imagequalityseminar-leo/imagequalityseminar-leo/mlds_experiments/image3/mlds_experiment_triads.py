# MLDS analysis script

# change to your working directory. Change it to wherever you 
# have your files in your system 
setwd("/home/leo/Uni/visuell/imagequalityseminar/mlds_experiments/image1")

# First, you need to install the package. 
# you only need to do this once, you can comment 
# this line after done it for the first time.
#install.packages('MLDS')


# load package 
library(MLDS)

########################################################
## Reading and preparing data
# read all the CSV files you generated

for (i in 0:2){

	if(i==0){# condition artificial rain 
		d1 <- read.csv('design_LB_triads_0_results_art_rain.csv')
		d2 <- read.csv('design_LB_triads_1_results_art_rain.csv')
		d3 <- read.csv('design_LB_triads_2_results_art_rain.csv')
		}



	# example data with triads
	if(i==1){# condition rain 
		d1 <- read.csv('design_LB_triads_0_results_rain.csv')
		d2 <- read.csv('design_LB_triads_1_results_rain.csv')
		d3 <- read.csv('design_LB_triads_2_results_rain.csv')
		}

	if(i==2){#  condition no rain
		d1 <- read.csv('design_LB_triads_0_results_norain.csv')
		d2 <- read.csv('design_LB_triads_1_results_norain.csv')
		d3 <- read.csv('design_LB_triads_2_results_norain.csv')
		}


	# puts together. If you have only one file,
	# then don't do this step, 
	d <- rbind(d1, d2, d3) #

	# instead you just call  #d <- read.csv('myfile.csv')

	# for quadruples, the data should have 5 columns
	#    resp (observer response, 0 for S1-S2, 1 for S3-S4)
	#    S1, S2, S3, S4: index of the stimulus values in each quadruple (integers).

	# for triads, the data should have the same columns except S4.
	#    the observer response resp is 0 for S1-S2, or 1 for S2-S3.

	# we also need to know the actual stimulus values (not the indices). 
	# In the case of the example of correlation in scatterplots,
	# the stimulus vector is..

	# I have just copied it from the generate_stim.py  script
	stim <- c(0.0, 0.25, 0.5, 0.75, 0.9, 0.98)



	# make a properly formatted dataframe. It adds an 'attribute' 
	# called 'stimulus' to the DataFrame, so later MLDS keeps
	# track of it and it can plot the x-axis properly.
	if(ncol(d)==4){
	  # for triads, use:
	  df <- as.mlbs.df(d, stim)
	}else{
	  
	  # bug correction / 14.12.2020
	  # MLDS for quadruples requiere that always column S1 < column S2
	  # and column S3 < column S4, even if order was reversed during the experiment.
	  # my python script saves the order wrong, so the following code swaps
	  # the indices when necessary
	  temp_min <- pmin(d$S3, d$S4)
	  d$S4 <- pmax(d$S3, d$S4)
	  d$S3 <- temp_min
	  
	  temp_min <- pmin(d$S1, d$S2)
	  d$S2 <- pmax(d$S1, d$S2)
	  d$S1 <- temp_min
	  ## end bug correction
	  
	  # for quadruples, use:
	  df <- as.mlds.df(d, stim)
	}



	########################################################
	## Analysis with MLDS 
	# calls MLDS routine to estimate scale
	scale <- mlds(df)


	# just prints the scale values in the console
	print(scale) 


	## we can plot the perceptual scale and save the figure as PDF
	# change the filename to your own name and include which method you used
	if(i==0){#  condition no rain
		pdf('scale_one_LB_art_rain.pdf')
		plot(scale, xlab="Correlation coefficient - r", ylab="Perceptual scale")
		}
		
	if(i==1){#  condition no rain
		pdf('scale_one_LB_rain.pdf')
		plot(scale, xlab="Correlation coefficient - r", ylab="Perceptual scale")
		}

	if(i==2){#  condition no rain
		pdf('scale_one_LB_norain.pdf')
		plot(scale, xlab="Correlation coefficient - r", ylab="Perceptual scale")
		}
}
dev.off()
# END
