class Cell:

	def __init__(self, cell):
		self.cell = cell

	def __str__(self):
		return f"клетка с {self.cell} ячейками"

	def __add__(self, other):
		return Cell(self.cell + other.cell)

	def __sub__(self, other):
		return Cell(abs(self.cell - other.cell))

	def __mul__(self, other):
		return Cell(self.cell * other.cell)

	def __floordiv__(self, other):
		return Cell(self.cell // other.cell)

	def make_order(self, rows):
		self.rows = rows
		all_cells = ['*'] * self.cell
		new_list = []
		new_line = ''
		new_list = [all_cells[i:i + rows] for i in range(0, len(all_cells), rows)]
		for el in new_list:
			new_line = ''.join(el)
			print(new_line)

cell_1 = Cell(7)
cell_2 = Cell(13)
print(cell_1 + cell_2)
print(cell_1 * cell_2)
print(cell_1 - cell_2)
print(cell_1 // cell_2)
cell_2.make_order(4)
print()
(cell_1 + cell_2).make_order(5)
print()
(cell_1 * cell_2).make_order(9)
