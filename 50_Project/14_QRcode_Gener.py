# Basic Type
''' import qrcode as qr
img = qr.make("Hello Niteesh Your are coder Now!")
img.save("QRcode.png")'''

# Advanced Type
import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size = 10, border = 3,)

qr.add_data("https://www.linkedin.com/in/niteesh-kumar-1b1b3b1b1/")
qr.make(fit=True)
img = qr.make_image(fill_color = "black", back_color = "lightblue")
img.save("QRcode1.png")
img.show()#  to show the image in gallery directly
