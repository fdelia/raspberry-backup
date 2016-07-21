path = 'LogTemp.log'

fi = open(path, 'rb')
data = fi.read()
fi.close()
fo = open(path, 'wb')
fo.write(data.replace('\x00', ''))
fo.close()

