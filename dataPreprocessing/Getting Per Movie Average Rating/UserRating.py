#UserRating.py
#author: Anand Karandikar

class UserRating:
	
	movieRating = 0
	
	def __init__(self, userId, movieRating):
		self.userId = userId
		self.movieRating = movieRating
		
	def __str__(self):
		return 'User rating (%d, %d)' %(self.userId, self.movieRating)
