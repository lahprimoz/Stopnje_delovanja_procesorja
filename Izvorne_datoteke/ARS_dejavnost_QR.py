import qrcode
# Paket qrcode je najprej potrebno prenesti z uporabo ukaza v terminalu:
# pip install qrcode[pil]

url = input("Vnesi URL: ").strip()
filepath = "C:\\Users\\primo\\OneDrive\\Namizje\\Fax\\PEF\\2.  letnik\\ARS HDD SSD\\Dejavnost\\ARS_QRcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(filepath)

print("Izvedeno")