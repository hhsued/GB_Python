from PIL import Image

img = Image.open('Kindergottesdienst-März2020.jpg').convert('LA')
img.save('Neu.jpg')