import qrcode

data = "https://moodsunset.com/"

qr = qrcode.QRCode(
    version=1, # 버전. 1-40 사이의 값. 값이 커질수록 QR 크기가 커짐.
    error_correction=qrcode.constants.ERROR_CORRECT_L, # 오류 수정 수준
    box_size=10, # 박스(점)의 크기
    border=4, # 테두리 너비
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

img.save("moodsunset.png")