from brainfuck_to_c import BrainF_Translator
import os
import time

brainf_string = input("Code: ")
c_code = BrainF_Translator.translate_bf(brainf_string)
c_filename = str(hash(time.time)) + ".c"
with open(c_filename, "w") as c_file:
	c_file.write(c_code)
if os.system("g++ -w  -o output " + c_filename) == 0:
	print("Successfully compiled Brainfuck code into .exe format.")
else:
	print("Could not compile. You may not have g++ installed.")
os.remove(c_filename)