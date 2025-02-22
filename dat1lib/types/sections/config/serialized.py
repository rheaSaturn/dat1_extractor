import dat1lib.crc32 as crc32
import dat1lib.types.sections
import io
import json
import struct

class ConfigTypeSection(dat1lib.types.sections.SerializedSection):
	TAG = 0x4A128222 # Config Type
	TYPE = 'config'

	def __init__(self, data, container):
		dat1lib.types.sections.SerializedSection.__init__(self, data, container)

		# MSMR
		# 2521 occurrences in 2521 files (always present)
		# size = 56..84 (avg = 65.1)
		# always first
		#
		# examples: 80880A03CBA9B6B0 (min size), 852FD4D4179A4F46 (max size)

		# MM
		# 2026 occurrences in 2026 files (always present)
		# size = 56..84 (avg = 65.2)
		# always first
		#
		# examples: 804C47786C04D879 (min size), 826CCE238253182B (max size)

		# RCRA
		# 1847 occurrences in 1847 files (always present)
		# size = 56..84 (avg = 64.9)
		# always first
		#
		# examples: 819BFE537D2E0858 (min size), 90E14CDA8DD9D960 (max size)

	def get_short_suffix(self):
		return "type"

	def print_verbose(self, config):
		##### "{:08X} | ............ | {:6} ..."
		print("{:08X} | Config Type  | {}".format(self.TAG, self.root))
		if len(self.extras) > 0:
			print(" "*10, self.extras)

	def web_repr(self):
		return {"name": "Config Type", "type": "json", "readonly": False, "content": self.root}

###

class ConfigContentSection(dat1lib.types.sections.SerializedSection):
	TAG = 0xE501186F # Config Built
	TYPE = 'config'

	def __init__(self, data, container):
		dat1lib.types.sections.SerializedSection.__init__(self, data, container)

		# MSMR
		# 2521 occurrences in 2521 files (always present)
		# size = 16..975836 (avg = 3205.9)
		#
		# examples: 813381135A2CC078 (min size), A5C3BBB75C76D0FA (max size)

		# MM
		# 2026 occurrences in 2026 files (always present)
		# size = 16..1230252 (avg = 3679.2)
		# always last
		#
		# examples: 813381135A2CC078 (min size), 97425517EBC3BB3F (max size)

		# RCRA
		# 1847 occurrences in 1847 files (always present)
		# size = 16..3322020 (avg = 4698.9)
		#
		# examples: 94982925AD887B35 (min size), BB876CAC4C37B181 (max size)

	def get_short_suffix(self):
		return "content"

	def print_verbose(self, config):
		##### "{:08X} | ............ | {:6} ..."
		print("{:08X} | Content      |".format(self.TAG))
		print(json.dumps(self.root, indent=4, sort_keys=True))
		if len(self.extras) > 0:
			print(" "*10, self.extras)

	def web_repr(self):
		return {"name": "Config Built", "type": "json", "readonly": False, "content": self.root}
