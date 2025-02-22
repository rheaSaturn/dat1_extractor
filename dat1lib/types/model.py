import dat1lib.types.dat1
import dat1lib.utils as utils
import io
import struct

class Model(object):
	MAGIC = 0x98906B9F

	def __init__(self, f, version=None):
		# MSMR
		# 38298 occurrences
		# size = 2260..42645436 (avg = 108149.2)
		# from 8 to 31 sections (avg = 11.1)
		#
		# examples: 895946D95299E18F (min size), 8FCA3A1C0CF13DD0 (max size), 81DC2CDB45872F11 (8 sections), 9347CDA478F55078 (31 sections)

		# MM: none

		self.version = version
		
		self.magic, self.offset_to_stream_sections, self.stream_sections_size = struct.unpack("<III", f.read(12))
		self.unk = f.read(24)
		self._raw_dat1 = f.read()

		if self.magic != self.MAGIC:
			print("[!] Bad Model magic: {} (isn't equal to expected {})".format(self.magic, self.MAGIC))

		self.dat1 = dat1lib.types.dat1.DAT1(io.BytesIO(self._raw_dat1), self)

	def save(self, f):
		offset_to_indexbuf = 0
		for s in self.dat1.header.sections:
			if s.tag == 0x0859863D:
				offset_to_indexbuf = s.offset

		self.offset_to_stream_sections = offset_to_indexbuf
		self.stream_sections_size = self.dat1.header.size - offset_to_indexbuf

		f.write(struct.pack("<III", self.magic, self.offset_to_stream_sections, self.stream_sections_size))
		f.write(self.unk)
		self.dat1.save(f)

	def print_info(self, config):
		print("-------")
		print("Model {:08X}".format(self.magic))
		if self.magic != self.MAGIC:
			print("[!] Unknown magic, should be {}".format(self.MAGIC))
		print("")
		print("Streaming part:")
		print("- offset = {}".format(self.offset_to_stream_sections))
		print("- size   = {}".format(self.stream_sections_size))
		if False:
			print("")
			print(utils.treat_as_bytes(12, self.unk[:12]))
			print(utils.treat_as_bytes(12, self.unk[12:]))
		print("-------")
		print("")

		self.dat1.print_info(config)

	def _get_suffix_type(self, section_header, section):
		if section_header.offset < self.offset_to_stream_sections:
			return " (info)"

		return " (streaming)"

class Model2(Model): # MM variation
	MAGIC = 0xDB40514C

	# MSMR: none
	
	# MM
	# 37147 occurrences
	# size = 2260..31112412 (avg = 82484.5)
	# from 5 to 35 sections (avg = 11.0)
	#
	# examples: 895946D95299E18F (min size), A6E98A5F0D076856 (max size), 85BD78D439151B00 (5 sections), A1069ACB1E139D38 (35 sections)

class ModelRcra(Model):
	MAGIC = 0x9D2C0FA9

	# RCRA
	# 11387 occurrences
	# size = 2090..107925756 (avg = 618725.7)
	# from 5 to 35 sections (avg = 12.0)
	#
	# examples: 811265E7146EA7C8 (min size), AE2DF2353798682F (max size), ADE5909F821E9DDE (35 sections)

	def __init__(self, f, version=None):
		if version is None:
			version = dat1lib.VERSION_RCRA

		Model.__init__(self, f, version)
