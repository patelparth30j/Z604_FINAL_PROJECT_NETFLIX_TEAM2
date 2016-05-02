#GroupByUser.py

#Objective - Group the user_id and user_rating based on the movie_id in the netflix dataset.

#author: Anand Karandikar and Sameeksha Vaity

import jsonpickle
from MovieTitle import MovieTitle 
from UserRating import UserRating
import os

#outerDir = "C:/NetflixDataset/Netflix/Netflix/download"		
# the directory where movie_titles.txt lies.

outerDir = "D:/Spring 2016/BigData/Data/download/download"
#outerDir = "D:/Spring 2016/BigData/ETL/ETL/Test2"

outerFile = "movie_titles.txt"		# the file which tells the movie id,name and year.
#outerFile = "_movie.txt"

#innerDir = "C:/NetflixDataset/Netflix/Netflix/download/download/training_set/training_set"	# directory under which the user ratings are stored per movie in separate files.

innerDir = "D:/Spring 2016/BigData/Data/download/download/training_set/training_set"
#innerDir = "D:/Spring 2016/BigData/ETL/ETL/Test2"

outputJSON = "F:/BigData/movieSet.json"	# the output JSON. Would be used to load into MongoDB

endl = os.linesep

readF = open(outerDir+"/"+outerFile)#read from movie_titles
innerDirs = os.listdir(innerDir)
writeF = open(outputJSON,"a")	#write to JSON file. 

line = readF.readline()
i = 0
while line:
	line = line.strip(endl)
	val = line.split(",")

	if(val[1] == 'NULL'):
		movie = MovieTitle(int(val[0]),val[2],val[1])
	else:
		movie = MovieTitle(int(val[0]),val[2],int( val[1]))
	
	innerF = open(innerDir+"/"+innerDirs[i])
	#print(innerDir+"/"+innerDirs[i])
	#print('File ('+str(i)+') - '+innerDirs[i]+' : ')
	innerF.readline()		#skip the movie id
	lineI = innerF.readline()
	#print(lineI)
	count = 0
	while lineI:
		count += 1
		lineI = lineI.strip(endl)
		valI = lineI.split(",")
		
		userR = UserRating(int(valI[0]), int(valI[1]))
		#print(userR)
		movie.userRating.append(userR)
		lineI = innerF.readline()
		
	innerF.close()
	
	print(str(count)+" records processed.")
	jsonRep = jsonpickle.encode(movie,unpicklable=False)
	writeF.write(jsonRep+"\n")
	
	line = readF.readline()
	i += 1
	
readF.close()
writeF.close()
