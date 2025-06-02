import pyqrcode
import png
import pyqrcode import QRCode

url=("https://www.youtube.com/")

s=pyqrcode.create(url)
s.png("myqr.png",scale=8)
url.png("myqr.png",scale=8)
