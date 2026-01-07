import qrcode
from PIL import Image
data = input("Введите ссылку: ")
name = input("Введите название сохраняемого файла: ")
logo_place = input("Введите расположение изображение на компьютере: ")
logo = Image.open(logo_place)
qr = qrcode.QRCode(
    version = 2,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
    )
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(
    fill_color="black",
    back_color="white"
    ).convert('RGB')
qr_width, qr_height = img.size
logo_size = qr_width // 10
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
logo_pos = (
    (qr_width - logo_size) // 2,
    (qr_height - logo_size) // 2
    )
img.paste(logo, logo_pos)
img.save(f"C:/python/small/qr_code_generator/{name}.JPG")
img.show()
