
class Compiler:
	def __init__(self, memory_size=30000):
		self.memory_size = 30000
		self.memory = [0 for i in range(self.memory_size)]
		self.pointer_address = 0

	def _reset_memory(self):
		self.memory = [0 for i in range(self.memory_size)]
		self.pointer_address = 0

	def compile(self, compile_string):
		output_string = ""
		loop_buffer = {}
		for index, char in enumerate(compile_string):
			if char == ">":
				self.pointer_address += 1
				if self.pointer_address > self.memory_size - 1:
					self._raise_error("Pointer memory invalid, attempt to access address larger than allocated.",
						index, char)
					break
			elif char == ">":
				self.pointer_address -= 1
				if self.pointer_address < 0:
					self._raise_error("Pointer memory invalid, attempt to access address smaller than 0.", index, char)
					break
			elif char == "+":
				self.memory[self.pointer_address] += 1
			elif char == "-":
				self.memory[self.pointer_address] -= 1
				if self.memory[self.pointer_address] < 0:
					self._raise_error("Value at pointer smaller than 0.", index, char)
					break
			elif char == ".":
				output_string += self._ascii_value(self.memory[self.pointer_address])
			elif char == ",":
				print(output_string)
				user_input = input("INPUT: ")
				if not user_input.isnumeric():
					self._raise_error("Input is not an integer.", index, char)
					break
				self.memory[self.pointer_address] = int(user_input)

		self._reset_memory()

	def _ascii_value(self, number):
		if number < 128:
			return char(number)
		else:
			return ""

	def _raise_error(self, message, index, char):
		print("ERROR: " + message + "\nOccured at INSTRUCTION " + str(index) + ", \"" + char + "\".")
