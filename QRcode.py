import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_M,
                 box_size=10,border=5)
qr.add_data("https://www.linkedin.com/in/karishma-singh-817580279/")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("Linked_in.png")

