import dat1lib.types.sections
import struct

class SpanEntry(object):
	def __init__(self, data):
		self.asset_index, self.count = struct.unpack("<II", data)

class SpansSection(dat1lib.types.sections.Section):
	TAG = 0xEDE8ADA9
	TYPE = 'toc'

	def __init__(self, data):
		dat1lib.types.sections.Section.__init__(self, data)

		ENTRY_SIZE = 8
		count = len(data)//ENTRY_SIZE
		self.entries = [SpanEntry(data[i*ENTRY_SIZE:(i+1)*ENTRY_SIZE]) for i in xrange(count)]
