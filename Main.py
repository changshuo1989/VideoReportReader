import time
import datetime
import VideoReportReader
import configparser


def compareRecords(list, minimum):
	res=[]
	dict={}
	l=len(list)
	if l != 0:
		for i in list:
			for key, value in i.items():
				if value <= float(minimum):
					if key in dict:
						times=dict[key]
						dict[key]=times+1
					else:
						dict[key]=1
		for key, value in dict.items():
			if value == l:
				res.append(key)

	return res


while True:

	section='SETTINGS'

	list=[]
	
	'today=time.strftime("%Y-%m-%d")'


	config=configparser.ConfigParser()
	config.read('application.cfg')
	dir=config.get(section,'dir')
	minimum=config.get(section,'minimum')
	days=config.get(section,'days')
	repeat=config.get(section, 'repeat')	

	'''
	reportReader = VideoReportReader.VideoReportReader(dir, today) 
	reportReader.getSuccessRate()
	'''
	
	for i in range(int(days)):
		adate=datetime.date.today()-datetime.timedelta(i)
		ds=adate.strftime('%Y-%m-%d')
		
		reportReader=VideoReportReader.VideoReportReader(dir, ds)
		list.append(reportReader.getSuccessRate())
		
		
		
	res=compareRecords(list, minimum)
	print(res)

	time.sleep(float(repeat))
	
