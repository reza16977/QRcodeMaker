import qrcode
from PIL import Image

qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "https://github.com/reza16977"

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color='white')
img.save('my_github.png')
