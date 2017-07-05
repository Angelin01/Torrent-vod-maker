import os
from dottorrent import Torrent # pip install dottorrent
from datetime import datetime # pip install datetime

trackerList = ['udp://tracker.openbittorrent.com:80/announce'] # Add trackers here
videoFormats = ['flv', 'mp4', 'webm', 'mkv', 'ogv', 'ogg', 'avi'] # Add vod file formats here
rootDir = "Vods/" # The root directory for the files

if not os.path.isdir(rootDir):
	print("Your rootDir doesn't exist")

for root, directories, files in os.walk(rootDir): 
	for file in files:
		if file.endswith(tuple(videoFormats)):
			filePath = rootDir + os.path.join(os.path.relpath(root, rootDir), file)
			fileName, fileExtension = os.path.splitext(filePath)
			# Torrent library documentation can be found here https://dottorrent.readthedocs.io/en/latest/library.html
			torrent = Torrent(filePath, trackers = trackerList, creation_date = datetime.now(), comment = "Jefmajor vod " + fileName, private = False)
			torrent.generate()
			
			torrentPath = fileName + ".torrent" # Just adjusting the .torrent file name to be file - extension + .torrent
			
			# Saving torrent
			torrentFile = open(torrentPath, 'wb')
			torrent.save(torrentFile)
			torrentFile.close()
			