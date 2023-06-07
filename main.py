from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathout = './Image Editor/editedImgs'  # Remove the leading slash

# Create the output directory if it doesn't exist
if not os.path.exists(pathout):
    os.makedirs(pathout)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathout}/{clean_name}_edited.jpg')
