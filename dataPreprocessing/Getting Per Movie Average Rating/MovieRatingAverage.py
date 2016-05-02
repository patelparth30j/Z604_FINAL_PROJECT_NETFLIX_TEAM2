#MovieRatingAverage.py
#author: Anand Karandikar

import jsonpickle
from MovieTitle import MovieTitle 
#from UserRating import UserRating
import os

outerDir = "C:/NetflixDataset/Netflix/Netflix/download"		
# the directory where movie_titles.txt lies.

#outerDir = "D:/Spring 2016/BigData/Data/download/download"
#outerDir = "D:/Spring 2016/BigData/ETL/ETL/Test"
outerFile = "movie_titles.txt"		# the file which tells the movie id,name and year.

innerDir = "C:/NetflixDataset/Netflix/Netflix/download/download/training_set/training_set"	# directory under which the user ratings are stored per movie in separate files.

#innerDir = "D:/Spring 2016/BigData/Data/download/download/training_set/training_set"

#outputJSON = "D:/Spring 2016/BigData/Data/download/download/movieSet.json"	# the output JSON. Would be used to load into MongoDB
outputJSON = "C:/NetflixDataset/Netflix/Netflix/download/movieSet.json"

endl = os.linesep

readF = open(outerDir+"/"+outerFile)#read from movie_titles
innerDirs = os.listdir(innerDir)
writeF = open(outputJSON,"a")	#write to JSON file. 

line = readF.readline()
i = 0
while line:
	line = line.strip(endl)
	val = line.split(",")
	
	innerF = open(innerDir+"/"+innerDirs[i])
	print('File ('+str(i)+') - '+innerDirs[i]+' : ')
	innerF.readline()		#skip the movie id
	lineI = innerF.readline()
	count = 1
	sumRating = 0
	while lineI:
		count += 1
		lineI = lineI.strip(endl)
		valI = lineI.split(",")
		sumRating = sumRating + int(valI[1])
		
		#userR = UserRating(int(val[0]), int(val[1]))
		#movie.userRating.append(userR)
		lineI = innerF.readline()
	innerF.close()
	# saving the average rating per movie
	average = (sumRating/count)

	movie = MovieTitle(int(val[0]), val[2], int(val[1]),average)
		
	jsonRep = jsonpickle.encode(movie,unpicklable=False)
	writeF.write(jsonRep+"\n")
	print(str(count)+" records processed.")
	
	line = readF.readline()
	i += 1
	
readF.close()
writeF.close()
