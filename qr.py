import qrcode

url = "www.example.com"

img = qrcode.make(url)
img.save("qrcode.png")

print("สร้าง QR Code เรียบร้อยแล้ว")