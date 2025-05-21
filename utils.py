from PIL import Image
import io

def convert_to_rgb(image: Image.Image) -> Image.Image:
    return image.convert('RGB') if image.mode != 'RGB' else image

def image_to_byte_stream(image: Image.Image) -> io.BytesIO:
    buffer = io.BytesIO()
    image.save(buffer, format='JPEG')
    buffer.seek(0)
    return buffer
