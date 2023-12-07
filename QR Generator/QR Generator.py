import pyqrcode
import png

name ='Saran'
qr =pyqrcode.create(name)
qr.png('qrcode.png',scale=10)