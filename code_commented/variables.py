# Number of repetitions. At least 3, 5 recommended.
# Type: Integer
# Default: 3
nRep = 3

# Names of the Condtitions. These will be part of your image name. For more specifics about your ..
# .. image Names, look in instructions.md
# Type: List of Stings
# Default: ["norain", "rain", "art_rain"]
conditionNames = ["norain", "rain", "art_rain"]
# How many conditions there are. This will calculate itself.
numberConditions = len(conditionNames)

# How many compressions you created. These will be part of your image name. For more specifics about your ..
# .. image Names, look in instructions.md
# Type: Integer
# Default: 6
numberCompressions = 6

# What type of image your images are. Change this if you use other kind of types.
# Type: String
# Default: ".jpeg"
imageEnding = ".jpeg"
# How many Base Images are in your Experiment
# Type: Integer
# Default: 4
numberImages = 4