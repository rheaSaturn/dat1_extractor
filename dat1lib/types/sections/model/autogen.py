import dat1lib.types.sections
import io
import struct

class x00823787_Section(dat1lib.types.sections.Section):
	TAG = 0x00823787
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 20 occurrences in 38298 files
		# size = 4
		#
		# examples: 8401B7F8A3E0B9EA
		
		ENTRY_SIZE = 4
		count = len(data)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in xrange(count)]

	def save(self):
		of = io.BytesIO(bytes())
		for e in self.entries:
			of.write(struct.pack("<I", e))
		of.seek(0)
		return of.read()

	def get_short_suffix(self):
		return "00823787 ({})".format(len(self.entries))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | 00823787     | {:6} entries".format(self.TAG, len(self.entries))

#

class x14D8B13C_Section(dat1lib.types.sections.Section):
	TAG = 0x14D8B13C
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# size = 14976
		#
		# examples: 98E675D6ADB2647B
		
		ENTRY_SIZE = 4
		count = len(data)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in xrange(count)]

	def save(self):
		of = io.BytesIO(bytes())
		for e in self.entries:
			of.write(struct.pack("<I", e))
		of.seek(0)
		return of.read()

	def get_short_suffix(self):
		return "14D8B13C ({})".format(len(self.entries))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | 14D8B13C     | {:6} entries".format(self.TAG, len(self.entries))

#

class x27CA5246_Section(dat1lib.types.sections.Section):
	TAG = 0x27CA5246
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 31 occurrences in 38298 files
		# size = 9084..770184 (avg = 315614.7)
		#
		# examples: 858060AD687726AF (min size), 9870FFAD9BAF955A (max size)
		
		ENTRY_SIZE = 4
		count = len(data)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in xrange(count)]

	def save(self):
		of = io.BytesIO(bytes())
		for e in self.entries:
			of.write(struct.pack("<I", e))
		of.seek(0)
		return of.read()

	def get_short_suffix(self):
		return "27CA5246 ({})".format(len(self.entries))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | 27CA5246     | {:6} entries".format(self.TAG, len(self.entries))

#

class x3C9DABDF_Section(dat1lib.types.sections.Section):
	TAG = 0x3C9DABDF
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 31 occurrences in 38298 files
		# size = 2512..15072 (avg = 8386.8)
		#
		# examples: 858060AD687726AF (min size), 857EF55F37F5BDCF (max size)
		
		ENTRY_SIZE = 4
		count = len(data)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in xrange(count)]

	def save(self):
		of = io.BytesIO(bytes())
		for e in self.entries:
			of.write(struct.pack("<I", e))
		of.seek(0)
		return of.read()

	def get_short_suffix(self):
		return "3C9DABDF ({})".format(len(self.entries))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | 3C9DABDF     | {:6} entries".format(self.TAG, len(self.entries))

#

class x5A39FAB7_Section(dat1lib.types.sections.Section):
	TAG = 0x5A39FAB7
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 64 occurrences in 38298 files
		# size = 38..1414 (avg = 388.9)
		#
		# examples: 8A9C0AD7B6F3BBF4 (min size), 8C00E8BCEACF88E5 (max size)
		pass

	def get_short_suffix(self):
		return "5A39FAB7 ({} bytes)".format(len(self._raw))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | 5A39FAB7     | {:6} bytes".format(self.TAG, len(self._raw))

#

class x5240C82B_Section(dat1lib.types.sections.Section):
	TAG = 0x5240C82B
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 77 occurrences in 38298 files
		# size = 256..14816 (avg = 4554.5)
		#
		# examples: AA3C0092DD64C101 (min size), BB6E44C6B57852B0 (max size)
		pass

	def get_short_suffix(self):
		return "5240C82B ({} bytes)".format(len(self._raw))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | 5240C82B     | {:6} bytes".format(self.TAG, len(self._raw))

#

class x5E709570_Section(dat1lib.types.sections.Section):
	TAG = 0x5E709570
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 255 occurrences in 38298 files
		# size = 1248..12720124 (avg = 1245716.2)
		#
		# examples: A296B03EFEBF937A (min size), A20532A6756AC4AE (max size)
		
		ENTRY_SIZE = 4
		count = len(data)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in xrange(count)]

	def save(self):
		of = io.BytesIO(bytes())
		for e in self.entries:
			of.write(struct.pack("<I", e))
		of.seek(0)
		return of.read()

	def get_short_suffix(self):
		return "5E709570 ({})".format(len(self.entries))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | 5E709570     | {:6} entries".format(self.TAG, len(self.entries))

#

class xBCE86B01_Section(dat1lib.types.sections.Section):
	TAG = 0xBCE86B01
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 124 occurrences in 38298 files
		# size = 32..352 (avg = 51.8)
		#
		# examples: 80B239C44ED6722A (min size), AFD77FCE52114B83 (max size)
		
		ENTRY_SIZE = 4
		count = len(data)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in xrange(count)]

	def save(self):
		of = io.BytesIO(bytes())
		for e in self.entries:
			of.write(struct.pack("<I", e))
		of.seek(0)
		return of.read()

	def get_short_suffix(self):
		return "BCE86B01 ({})".format(len(self.entries))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | BCE86B01     | {:6} entries".format(self.TAG, len(self.entries))

#

class x90CDB60C_Section(dat1lib.types.sections.Section):
	TAG = 0x90CDB60C
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 2311 occurrences in 38298 files
		# size = 80
		#
		# examples: 8007367BDC86C66B
		
		ENTRY_SIZE = 4
		count = len(data)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in xrange(count)]

	def save(self):
		of = io.BytesIO(bytes())
		for e in self.entries:
			of.write(struct.pack("<I", e))
		of.seek(0)
		return of.read()

	def get_short_suffix(self):
		return "90CDB60C ({})".format(len(self.entries))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | 90CDB60C     | {:6} entries".format(self.TAG, len(self.entries))

#

class x5D5CF541_Section(dat1lib.types.sections.Section):
	TAG = 0x5D5CF541
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# size = 14976
		#
		# examples: 98E675D6ADB2647B
		
		ENTRY_SIZE = 4
		count = len(data)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in xrange(count)]

	def save(self):
		of = io.BytesIO(bytes())
		for e in self.entries:
			of.write(struct.pack("<I", e))
		of.seek(0)
		return of.read()

	def get_short_suffix(self):
		return "5D5CF541 ({})".format(len(self.entries))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | 5D5CF541     | {:6} entries".format(self.TAG, len(self.entries))
#

class x855275D7_Section(dat1lib.types.sections.Section):
	TAG = 0x855275D7
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 157 occurrences in 38298 files
		# size = 64..412 (avg = 227.9)
		#
		# examples: A2107CD6FA00E037 (min size), AB6E2F9441080649 (max size)
		
		ENTRY_SIZE = 4
		count = len(data)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in xrange(count)]

	def save(self):
		of = io.BytesIO(bytes())
		for e in self.entries:
			of.write(struct.pack("<I", e))
		of.seek(0)
		return of.read()

	def get_short_suffix(self):
		return "855275D7 ({})".format(len(self.entries))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | 855275D7     | {:6} entries".format(self.TAG, len(self.entries))

#

class x8A84E4D6_Section(dat1lib.types.sections.Section):
	TAG = 0x8A84E4D6
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 157 occurrences in 38298 files
		# size = 60..109008 (avg = 10777.9)
		#
		# examples: A2107CD6FA00E037 (min size), 86B8B887A2871FCA (max size)
		pass

	def get_short_suffix(self):
		return "8A84E4D6 ({} bytes)".format(len(self._raw))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | 8A84E4D6     | {:6} bytes".format(self.TAG, len(self._raw))

#

class xA600C108_Section(dat1lib.types.sections.Section):
	TAG = 0xA600C108
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 255 occurrences in 38298 files
		# size = 76..709280 (avg = 133422.9)
		#
		# examples: A296B03EFEBF937A (min size), 9870FFAD9BAF955A (max size)
		
		ENTRY_SIZE = 4
		count = len(data)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in xrange(count)]

	def save(self):
		of = io.BytesIO(bytes())
		for e in self.entries:
			of.write(struct.pack("<I", e))
		of.seek(0)
		return of.read()

	def get_short_suffix(self):
		return "A600C108 ({})".format(len(self.entries))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | A600C108     | {:6} entries".format(self.TAG, len(self.entries))

#

class xDCA379A2_Section(dat1lib.types.sections.Section):
	TAG = 0xDCA379A2
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 2121 occurrences in 38298 files
		# size = 5..5642457 (avg = 157231.4)
		#
		# examples: 8D8CB10A938FE720 (min size), 8FCA3A1C0CF13DD0 (max size)
		pass

	def get_short_suffix(self):
		return "DCA379A2 ({} bytes)".format(len(self._raw))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | DCA379A2     | {:6} bytes".format(self.TAG, len(self._raw))

#

class xADD1CBD3_Section(dat1lib.types.sections.Section):
	TAG = 0xADD1CBD3
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 3 occurrences in 38298 files
		# size = 704..2720 (avg = 2048.0)
		#
		# examples: AF3AC54D239CD584 (min size), A296B03EFEBF937A (max size)
		
		ENTRY_SIZE = 4
		count = len(data)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in xrange(count)]

	def save(self):
		of = io.BytesIO(bytes())
		for e in self.entries:
			of.write(struct.pack("<I", e))
		of.seek(0)
		return of.read()

	def get_short_suffix(self):
		return "ADD1CBD3 ({})".format(len(self.entries))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | ADD1CBD3     | {:6} entries".format(self.TAG, len(self.entries))

#

class xB25B3163_Section(dat1lib.types.sections.Section):
	TAG = 0xB25B3163
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 31 occurrences in 38298 files
		# size = 47296..7250416 (avg = 2263386.3)
		#
		# examples: 858060AD687726AF (min size), B29BA0754ACB0151 (max size)
		
		ENTRY_SIZE = 4
		count = len(data)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in xrange(count)]

	def save(self):
		of = io.BytesIO(bytes())
		for e in self.entries:
			of.write(struct.pack("<I", e))
		of.seek(0)
		return of.read()

	def get_short_suffix(self):
		return "B25B3163 ({})".format(len(self.entries))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | B25B3163     | {:6} entries".format(self.TAG, len(self.entries))

#

class xCD903318_Section(dat1lib.types.sections.Section):
	TAG = 0xCD903318
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 5 occurrences in 38298 files
		# size = 68..232 (avg = 131.6)
		#
		# examples: A2107CD6FA00E037 (min size), 857EF55F37F5BDCF (max size)
		pass

	def get_short_suffix(self):
		return "CD903318 ({} bytes)".format(len(self._raw))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | CD903318     | {:6} bytes".format(self.TAG, len(self._raw))

#

class xBB7303D5_Section(dat1lib.types.sections.Section):
	TAG = 0xBB7303D5
	TYPE = 'Model'

	def __init__(self, data, container):
		dat1lib.types.sections.Section.__init__(self, data, container)

		# 31 occurrences in 38298 files
		# size = 6056..513456 (avg = 210409.8)
		#
		# examples: 858060AD687726AF (min size), 9870FFAD9BAF955A (max size)
		
		ENTRY_SIZE = 4
		count = len(data)//ENTRY_SIZE
		self.entries = [struct.unpack("<I", data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE])[0] for i in xrange(count)]

	def save(self):
		of = io.BytesIO(bytes())
		for e in self.entries:
			of.write(struct.pack("<I", e))
		of.seek(0)
		return of.read()

	def get_short_suffix(self):
		return "BB7303D5 ({})".format(len(self.entries))

	def print_verbose(self, config):
		if config.get("web", False):
			return
		
		##### "{:08X} | ............ | {:6} ..."
		print "{:08X} | BB7303D5     | {:6} entries".format(self.TAG, len(self.entries))
