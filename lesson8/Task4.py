class Orgtechnic:
	def __init__(self, name, price, number, units):
		self.name = name
		self.price = price
		self.number = number
		self.units = units

class Printer(Orgtechnic):
	def __init__(self, name, price, number, units, toner):
		super().__init__(name, price, number, units)
		self.toner = toner
		self.product = [self.name, self.price, self.number, self.units, self.toner]

class Scanner(Orgtechnic):
	def __init__(self, name, price, number, units, mpi):
		super().__init__(name, price, number, units)
		self.mpi = mpi
		self.product = [self.name, self.price, self.number, self.units, self.mpi]

class Xerox(Orgtechnic):
	def __init__(self, name, price, number, units, ltype):
		super().__init__(name, price, number, units)
		self.ltype = ltype
		self.product = [self.name, self.price, self.number, self.units, self.ltype]
