import sys
import os
import os.path
import re

import dat1lib
import dat1lib.utils
import info_printer

class ModelHeader(object):
	def __init__(self, f):
		self.magic, = dat1lib.utils.read_struct(f, "<I")
		self.data = dat1lib.utils.read_struct(f, "<" + "I"*8)

###

def handle_args():
	if len(sys.argv) < 2:
		print "Usage:"
		print "{} <filename> [directory to extract to]".format(sys.argv[0])
		sys.exit()

	fn = sys.argv[1]
	f = None
	try:
		f = open(fn, "rb")
	except:
		print "Couldn't open '{}'!".format(fn)
		sys.exit()

	is_model = (".model" in fn)

	extraction_dir = os.path.basename(fn).replace(".model", "") + "_extracted"
	if len(sys.argv) > 2:
		extraction_dir = sys.argv[2]

	return (f, is_model, extraction_dir)

def main():
	f, is_model, extraction_dir = handle_args()

	model_header = None
	offset = 0
	if is_model:
		model_header = ModelHeader(f)
		offset = 36
	
	dat1 = dat1lib.DAT1(f, offset)
	f.close()

	info_printer.print_info(model_header, dat1)
	info_printer.extract_secion(dat1, extraction_dir)

main()
