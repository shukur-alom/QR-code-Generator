import qrcode as myqq
import matplotlib.pyplot as plt

qr = myqq.QRCode(
    version=2,
    box_size=15,
    border=5
)
data = """Name : Shukur Alam
Adress : Hajiganj
Work : In AI
        """
img_name = 'test.jpg'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black',back_color='white')
img.save(img_name)

img = plt.imread(img_name)
plt.imshow(img)
plt.show()