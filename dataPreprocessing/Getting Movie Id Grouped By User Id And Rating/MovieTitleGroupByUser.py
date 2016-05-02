#MovieTitleGroupByUser.py
#author: Anand Karandikar and Sameeksha Vaity

import jsonpickle
from UserRating import UserRating

class MovieTitle:
	movieId = 0
	movieName = ""
	movieYear = 0
	
	# Constructor in Python
	def __init__(self, movieId, movieName, movieYear):
		self.movieId = movieId
		self.movieName = movieName
		self.movieYear = movieYear
		self.userRating = []	# array of user ratings
		
	def __str__(self):
		return 'movie (%d, %d, %s, %s)' % (self.movieId, self.movieYear, self.movieName, self.userRating)


