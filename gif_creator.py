from PIL import Image
import glob
import os

# Путь к папке с изображениями
image_folder = './images/'

# Получаем все файлы изображений из папки
files = glob.glob(image_folder + '*.png') + glob.glob(image_folder + '*.jpg') + glob.glob(image_folder + '*.jpeg')

# Сортируем файлы в порядке возрастания
files = sorted(files)

# Открываем изображения и добавляе
