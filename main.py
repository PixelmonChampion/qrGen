import qrcode

url = input("Enter the URL: ")

img = qrcode.make(url)

img.save("qr.png")
