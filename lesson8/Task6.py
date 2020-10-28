import traceback

class OwnError(Exception):
	def __init__(self, txt):
		self.txt = txt
