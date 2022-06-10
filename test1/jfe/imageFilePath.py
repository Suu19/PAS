import os

def load_images_from_folder(folder):
    images = []
    for img in os.listdir(folder):
        img = os.path.basename(folder)
        if img is not None:
            images.append(img)
    return images

print(load_images_from_folder('C:\\Users\\nawthae\\test1\\staticfiles\\images'))

