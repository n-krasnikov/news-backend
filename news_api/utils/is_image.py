IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.svg')

def is_image(image):
    return (image.name.lower().endswith(IMAGE_EXTENSIONS))