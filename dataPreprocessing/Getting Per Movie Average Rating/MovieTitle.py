#MovieTitle.py
#author: Anand Karandikar

import jsonpickle
from UserRating import UserRating

class MovieTitle:
	movieId = 0
	movieName = ""
	movieYear = 0
	avgRating = 0
	
	# Constructor in Python
	def __init__(self, movieId, movieName, movieYear, avgRating):
		self.movieId = movieId
		self.movieName = movieName
		self.movieYear = movieYear
		#self.userRating = []	# array of user ratings
		self.avgRating = avgRating
		
	def __str__(self):
		#return 'movie (%d, %d, %s, %s)' % (self.movieId, self.movieYear, self.movieName, self.userRating)
		return 'movie (%d, %d, %s, %f)' % (self.movieId, self.movieYear, self.movieName, self.avgRating)


