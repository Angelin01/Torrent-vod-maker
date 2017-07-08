import os
import sys
from dottorrent import Torrent # pip install dottorrent
from datetime import datetime # pip install datetime

trackerList = ['udp://tracker.openbittorrent.com:80/announce'] # Add trackers here
videoFormats = ['flv', 'mp4', 'webm', 'mkv', 'ogv', 'ogg', 'avi'] # Add vod file formats here
rootDir = "Vods/" # The root directory for the files

if not os.path.isdir(rootDir):
	sys.exit("rootDir is not a valid directory")

for root, directories, files in os.walk(rootDir): 
	for file in files:
		filePath = rootDir + os.path.join(os.path.relpath(root, rootDir), file)
		fileName, fileExtension = os.path.splitext(filePath)
		if fileExtension != '.torrent' and ((os.path.splitext(file)[0] + '.torrent') not in files) and file.endswith(tuple(videoFormats)):
			# Torrent library documentation can be found here https://dottorrent.readthedocs.io/en/latest/library.html
			torrent = Torrent(filePath, trackers = trackerList, creation_date = datetime.now(), comment = "Jefmajor vod " + fileName, private = False)
			if not torrent.generate():
				print("Error generating torrent for " + filePath + fileExtension)
				continue
			
			torrentPath = fileName + ".torrent" # Just adjusting the .torrent file name to be file - extension + .torrent
			
			# Saving torrent
			torrentFile = open(torrentPath, 'wb')
			torrent.save(torrentFile)
			torrentFile.close()
			print("Created .torrent for " + fileName + fileExtension)
		else:
			print("File " + fileName + fileExtension + " is either a .torrent, has a respective .torrent or isn't of the right format, ignoring")
			