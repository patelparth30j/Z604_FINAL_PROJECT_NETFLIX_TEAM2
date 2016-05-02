#UserRatingGroupByUser.py
#author: Anand Karandikar and Sameeksha Vaity

class UserRating:
	userId = 0
	movieRating = 0
	
	def __init__(self, userId, movieRating):
		self.userId = userId
		self.movieRating = movieRating
		
	def __str__(self):
		return 'User rating (%d, %d)' %(self.userId, self.movieRating)
