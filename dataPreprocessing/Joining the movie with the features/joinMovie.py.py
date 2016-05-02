# joinMovie.py
# Join the movie features with the movies from the training_set.
# Code to get the comma separated values in the format
# UserId, MovieId, MovieRating

import os
import csv
import jsonpickle

endl = os.linesep

writeF = open("D:/CD/Sp16/BD/ETL/Prod/Final_UserMovieRating_Filtered.csv","a")
inputFileName = "D:/CD/Sp16/BD/ETL/Prod/movie_features_df.csv"
with open(inputFileName,"r") as readF:
	reader = csv.reader(readF,delimiter="\t")
	count = 0
	records = 0
	str_zeros = ""
	for row in reader:
		count += 1
		# this get the movie name under the directory training_set
		zeros = 7 - len(row[0])
		for i in range(0, zeros):
			str_zeros += "0"
		
		# the output file name
		filename = "D:/CD/Sp16/BD/download/training_set/mv_"+str_zeros+str(row[0])+".txt"

		str_zeros = ""

		# open the movie file		
		with open(filename, "r") as readMovieF:
			readMovieF.readline()
			movieId = row[0]
			print "File no. "+str(count)+", movie id: " + str(movieId)
			line = readMovieF.readline().strip(endl)
			records += 1
			while line:
				records += 1
				val = line.split(",")
				userId = val[0]
				rating = val[1]
				writeF.write(userId+","+movieId+","+rating+"\n")
				line = readMovieF.readline().strip(endl)

	print "Total files operated: " + str(count)
	print "Total records processed: " + str(records)

readF.close()
readMovieF.close()		
writeF.close()
		
	


