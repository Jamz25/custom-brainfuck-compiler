from brainfuck_to_c import BrainF_Translator
from custom_errors import ArgumentError, FileError, FileTypeError
import os
import time
import sys

sys.tracebacklimit = 0

if len(sys.argv) == 1:
	raise ArgumentError("NO FILE ARGUMENT FOUND!")

if not os.path.isfile(sys.argv[1]):
	raise FileError("FILE \"" + sys.argv[1] + "\" CANNOT BE FOUND OR DOES NOT EXIST!")

if sys.argv[1].split(".")[-1] != "bf":
	raise FileTypeError("INVALID FILE EXTENSION, SHOULD BE \".bf\".")

with open(sys.argv[1], "r") as file:
	brainf_string = file.read()

c_code = BrainF_Translator.translate_bf(brainf_string)
c_filename = str(hash(time.time)) + ".c"
with open(c_filename, "w") as c_file:
	c_file.write(c_code)
if os.system("g++ -w  -o output " + c_filename) == 0:
	print("Successfully compiled Brainfuck code into .exe format.")
else:
	print("Could not compile. You may not have g++ installed.")
os.remove(c_filename)