#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
	def __init__(self, size, x=0, y=0, id=None):
		super().__init__(size, size, x, y, id)
		

	def __str__(self):
		return f"[Square] ({self.id}) {self.x} / {self.y} - {self.height}"


	@property
	def size(self):
		return self.width

	@size.setter
	def size(self, value):
		self.width = value
		self.height = value

	def update(self, *args, **kwargs):
		"""
		assigns attributes using args or kwargs.
		*args (positional argument):
			1st argument : id
			2nd argument : size
			3rd argument : x
			4th argument : y

		**kwargs: non positional arguments.
		"""


		if args and len(args) > 0:
			attributes = ["id", "size", "x", "y"]
			for i, value in enumerate(args):
				if i < len(attributes):
					setattr(self, attributes[i], value)
		elif kwargs:
			for key, value in kwargs.items():
				if hasattr(self, key):
					setattr(self, key, value)