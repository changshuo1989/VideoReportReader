import csv
import os


class VideoReportReader(object):
	
	class NoDirectoryError(ValueError):
		pass
		
	def __init__(self, dir, date):
		self.dir=dir
		self.date=date
	
	def getFile(self):
		if not os.path.exists(self.dir):
			raise NoDirectoryError('invalid directory')
		else:
			for fname in os.listdir(path=self.dir):
				if self.date in fname:
					fname=os.path.abspath(os.path.join(self.dir,fname))	
					return fname
					break
			
			

	def getSuccessRate(self):
		dict={}
		file=self.getFile()
		with open(file, 'rt') as csvFile:
			reader=csv.reader(csvFile)
			isHeader=True
			for row in reader:
				if isHeader:
					isHeader=False
					continue
				try:
					int(row[2])
					dict[row[2]]=float(row[5])
				except ValueError:
					continue

		return dict				
