my_list = [12, 34.3, True, "text", None, [1, 2], (0, 1), {2, 5}, 
			bytes([10, 20]), bytearray(b"some text")]

print(my_list)
for item in my_list:
	print(type(item))