import pyqrcode
import png

cherry = 'https://drive.google.com/file/d/1lBudeI5OuNgssRQVmYM2_r2EDbDGY2GL/view'
x = pyqrcode.create(cherry)
x.png('bday.png', scale=10)