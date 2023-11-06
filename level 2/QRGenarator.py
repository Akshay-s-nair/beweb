import qrcode

x=qrcode.QRCode(version=1,box_size=40,border=3)
x.add_data('https://akshay-s-nair.github.io/My_Portfolio')
x.make(fit=True)
img=x.make_image()
img.save('portfolio.png')
# x=qrcode.make('hello')
img.save('img.png')