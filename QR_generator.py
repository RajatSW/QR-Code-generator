import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10, border=4,)
qr.add_data(input("Paste your link:"))
qr.make(fit=True)
img = qr.make_image(fill_color="ivory", back_color="tan")
filename = input("Enter your file name (without extension): ")
img.save(f"{filename}.png")