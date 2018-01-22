import exifread
#open image file for reading (binary mode)
f=open(image01.jpg, 'rb')

#return exif tags
tags = exifread.process_file(f)




#https://pypi.python.org/pypi/ExifRead
