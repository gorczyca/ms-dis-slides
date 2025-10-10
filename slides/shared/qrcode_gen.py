from manim import *
import qrcode
from PIL import Image, ImageOps, ImageChops

def qr_code(link: str, out_path: str = "qr.png") -> str:
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    img.save(out_path)
    return out_path
