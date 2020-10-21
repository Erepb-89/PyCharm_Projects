class Matrix:

	def __init__(self, matrix):
		self.matrix = matrix

	def __str__(self):
		new_line = ''
		for i in self.matrix:
			new_line += ''.join(f"\t{str(i[0])}\t\t{str(i[1])}\n")
		return f"{new_line}"

	def __add__(self, other):
		new_line = ''
		self.add_matrix = [[0, 0], [0, 0], [0, 0]]
		for i in range((len(self.matrix))):
			for j in range(len(self.matrix[0])):
				self.add_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

		print(new_line)
		for i in self.add_matrix:
			new_line += ''.join(f"\t{str(i[0])}\t\t{str(i[1])}\n")
		return f"{new_line}"

matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
