
from thainlp import nlp as thainlp
import pykakasi
import korean_romanizer
import pinyin




#possible_formats: a list with possible format (first one is the default one)
def get_format(format,possible_formats):
	if (format==None):
		return  possible_formats[0]
	elif format not in possible_formats:
		raise Exception("format "+format+" not in the possible_formats: "+"|".join(possible_formats))
	else:
		return format





#https://github.com/PyThaiNLP/thainlp
class Romanizer_th:
	def __init__(self,format=None):
		allowed_formats=["split","continue"]
		self.format=get_format(format,allowed_formats)
	def romanize(self,text):
		sep=" " if self.format=="split" else ""
		return sep.join(thainlp(text).romanize)




#https://github.com/miurahr/pykakasi
class Romanizer_ja:
	def __init__(self,format=None):
		allowed_formats=["hepburn","kunrei","passport"]
		self.format=get_format(format,allowed_formats)
		self.kks = pykakasi.kakasi()
	def romanize(self,text):
		list_jpwords=self.kks.convert(text)
		return "".join([x[self.format] for x in list_jpwords])


#https://github.com/osori/korean-romanizer
class Romanizer_ko:
	def __init__(self,format=None):
		self.format=format # Currently not in use
	def romanize(self,text):
		return korean_romanizer.romanizer.Romanizer(text).romanize()



#https://github.com/lxyu/pinyin
class Romanizer_zh:
	def __init__(self,format=None):
		allowed_formats=["diacritical","numerical","strip"]
		self.format=get_format(format,allowed_formats)
	def romanize(self,text):
		return pinyin.get(text,format=self.format)






class Romanizer:
	def __init__(self, language, format=None):
		if language=="ja" or language=="jp":
			self.romanizer_class=Romanizer_ja(format)
		if language=="th":
			self.romanizer_class=Romanizer_th(format)
		if language=="ko":
			self.romanizer_class=Romanizer_ko(format)
		if language=="zh":
			self.romanizer_class=Romanizer_zh(format)
	def romanize(self,text):
		return self.romanizer_class.romanize(text)


