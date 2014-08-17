from mutagen import File
from mutagen.mp4 import MP4;
import sys;

if len(sys.argv)>1:
	path=sys.argv[1];
	pathlist=path.split('\\')
	imagepath=''
	for sec in pathlist[:-1]:
		imagepath=imagepath+sec+'\\'
	imagepath=imagepath+'Folder.jpg'
else:
	print('No argument')
	raw_input()
	sys.exit()

if path[-3:]=='m4a':
	file=MP4(path)
	try:
		artwork=file.tags['covr'][0]
	except:
		print('Cover Not Found')
		raw_input()
		sys.exit()
elif path[-3:]=='mp3':
	file = File(path) 
	try:
		artwork = file.tags['APIC:'].data
	except:
		print('Cover Not Found')
		raw_input()
		sys.exit()
else:
	print('Filetype Not Supported')
	raw_input()
	sys.exit()
	
try:
	with open(imagepath, 'wb') as img:
		img.write(artwork)
except:
	print('Write Error')
	raw_input()