import pyqrcode
import png

link = 'https://photos.app.goo.gl/W8eTuoSgezLmiygb9'
x = pyqrcode.create(link)
x.png('link.png', scale=10)