# Coded By : clarisha octa
# project : 1.0
# This Tool purpose to Download any File (exe,jar,iso,pdf,apk,zip...etc.) From Any Web Site.


import os
import urllib.request
from tqdm import tqdm
from optparse import OptionParser

def ClarishaOcta():
	print('''\033[1;31m
			  _____                             _____
			 | ___ |---------------------------| ___ |
 			  | _ |      PYTHON DOWNLOADER      | _ |
 			  |___|                             |___|
			 (_____)---------------------------(_____)''')
	print('\033[1;31m				     V.1.0 _C.OCTA				\033[1;m')																								
def Clarisha():

	parser = OptionParser('''
	\033[1;31m
			 ---------------------------------------
			 ---------------------------------------
	\033[1;m
Usage:

python3 Downloader.py -u http://www.site.com/download.(exe,apk,jar,txt,iso ......)
python3 Downloader.py --url http://www.site.com/download.(exe,apk,jar,png,iso ......)

Example :
	
python3 Downloader.py -u https://m.apkpure.com/durak-online/com.rstgames.durak.apk
python3 Downloader.py --url https://focebook.wap.sh/index.html

	''')


	parser.add_option('-u','--url',dest='clarisha_octa',type='string')

	(options,args) = parser.parse_args()

	if options.clarisha_octa == None:
		print(parser.usage)

	else :
	
		PROJECT= options.clarisha_octa
		urlopen = urllib.request.urlopen(PROJECT)
		si_cantik = URL.split('/')[-1]
		openfile = open(si_cantik,'wb')
		block_size = 1000
		file_size = int(urlopen.headers['Content-Length'])
		for i in tqdm(range(file_size)):
			Buffer = urlopen.read(block_size)
			i = i + block_size
			openfile.write(Buffer)
		openfile.close()
		print('Downloaded succeed..'.format(si_cantik))
ClarishaOcta()
Clarisha()

