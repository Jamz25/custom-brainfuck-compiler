
class BrainF_Translator:

	CONVERT = {
		">": "++ptr;",
		"<": "--ptr;",
		"+": "++*ptr;",
		"-": "--*ptr;",
		".": "putchar(*ptr);",
		",": "*ptr = getchar();",
		"[": "while(*ptr){",
		"]": "}"
	}

	@staticmethod
	def translate_bf(convert_string):
		result_code = "#include <stdio.h>\nint main(){char array[30000] = {0}; char *ptr = array;"
		for char in convert_string:
			if char in BrainF_Translator.CONVERT:
				result_code += BrainF_Translator.CONVERT[char]
			else:
				print("Found invalid character " + char + ", will continue to compile.")
		return result_code + "}"

