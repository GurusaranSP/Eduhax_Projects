import pyqrcode
import png

shab = 'https://photos.app.goo.gl/i1zykNUjPJvQFUQh8'
x = pyqrcode.create(shab)
x.png('shab.png', scale=10)