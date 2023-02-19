import qrcode


# generates a qr_code for any web link
def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="purple", back_color="white")
    img.save("CV.png")


generate_qr_code("https://www.linkedin.com/in/pantelimon-ev/")
