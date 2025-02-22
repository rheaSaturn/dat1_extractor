import dat1lib.crc32 as crc32
import dat1lib.types.sections
import dat1lib.utils as utils
import io
import struct

class Event(object):
	def __init__(self, data):
		self.ulid, self.small, self.flags, self.zero, self.flags2, self.a, self.b = struct.unpack("<IHHHHHH", data)
		# a == b most of the time (if not, a < b)

class EventsSection(dat1lib.types.sections.Section):
	TAG = 0x0E19E37F
	TYPE = 'soundbank'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# MSMR
		# 1309 occurrences in 1345 files
		# size = 16..123424 (avg = 1184.0)
		#
		# examples: 81456C2A07996ED7 (min size), 826509A0F509A671 (max size)

		# MM
		# 1164 occurrences in 1239 files
		# size = 16..97584 (avg = 841.9)
		#
		# examples: 805A011970FE88E3 (min size), AA47C17532AF52AC (max size)

		# RCRA
		# 1168 occurrences in 1218 files
		# size = 16..45792 (avg = 563.5)
		#
		# examples: 8019125F734A3957 (min size), 8E7F2FAFC675D9EF (max size)

		ENTRY_SIZE = 16
		count = len(data)//ENTRY_SIZE
		self.events = [Event(data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE]) for i in range(count)]

	def get_short_suffix(self):
		return "events ({})".format(len(self.events))

	def print_verbose(self, config):
		##### "{:08X} | ............ | {:6} ..."
		print("{:08X} | Events       | {:6} events".format(self.TAG, len(self.events)))
		print("")
		#######........ | 12  12345678  1234  12345  1234  12345  12345  12345
		print("           #       ulID     ?  flags  zero  flag2      ?      ?")
		print("         ------------------------------------------------------")
		for i, e in enumerate(self.events):
			print("         - {:<2}  {:08X}  {:4}  {:5}  {:4}  {:5}  {:5}  {:5}".format(i, e.ulid, e.small, e.flags, e.zero, e.flags2, e.a, e.b))

		print("")

###

class StringsSection(dat1lib.types.sections.StringsSection):
	TAG = 0x3E8490A3
	TYPE = 'soundbank'

	def __init__(self, data, container):
		dat1lib.types.sections.StringsSection.__init__(self, data, container)

		# MSMR
		# 1345 occurrences in 1345 files (always present)
		# size = 36..188456 (avg = 1981.2)
		#
		# examples: 9D2635C59FA63EF4 (min size), 826509A0F509A671 (max size)

		# MM
		# 1239 occurrences in 1239 files (always present)
		# size = 26..167447 (avg = 1559.3)
		#
		# examples: 8FA8E5C5DDC315C1 (min size), AA47C17532AF52AC (max size)

		# RCRA
		# 1218 occurrences in 1218 files (always present)
		# size = 26..83460 (avg = 1096.5)
		#
		# examples: 9257F71232118757 (min size), 8E7F2FAFC675D9EF (max size)

	def get_short_suffix(self):
		return "strings ({})".format(len(self._strings))

	def print_verbose(self, config):
		##### "{:08X} | ............ | {:6} ..."
		print("{:08X} | Strings      | {:6} strings".format(self.TAG, len(self._strings)))
		for s in self._strings:
			print(" "*11 + "- '{}'".format(s))
		print("")

###

class HeaderSection(dat1lib.types.sections.Section):
	TAG = 0x4765351A
	TYPE = 'soundbank'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# MSMR
		# 1345 occurrences in 1345 files (always present)
		# size = 64
		# always first
		#
		# examples: 801825F7A321A714

		# MM
		# 1239 occurrences in 1239 files (always present)
		# size = 64
		# always first
		#
		# examples: 800BAAC604A8B370

		# RCRA
		# 1218 occurrences in 1218 files (always present)
		# size = 64
		# always first
		#
		# examples: 800582AB4AE61DB1

		self.a, self.b, self.bnk_section_size = struct.unpack("<HHI", data[:8])
		rest = data[8:]

		ENTRY_SIZE = 4
		count = len(rest)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", rest[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in range(count)]

	def get_short_suffix(self):
		return "header?"

	def print_verbose(self, config):
		##### "{:08X} | ............ | {:6} ..."
		print("{:08X} | Header?      |".format(self.TAG))
		print(" "*11 + "{}  {}  {}".format(self.a, self.b, self.bnk_section_size))
		print(" "*11 + " ".join(["{}".format(x) for x in self.entries]))
		print("")
