import os
from time import time

from django.conf import settings

def save_image(image, directory):
    image_path = settings.STATIC_ROOT + directory + str(time()) + image.name
    
    path = (
        settings.BACKEND_URL 
        + settings.BACKEND_PORT 
        + settings.STATIC_URL 
        + os.path.relpath(image_path, start = settings.STATIC_ROOT)
    )
    
    with open(image_path, 'wb') as f:
        f.write((image.file).read())

    return path