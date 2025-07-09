import os
from PIL import Image

TRAINING_SET_DIR = './dataset_v0.v1i.yolov11/train/images'
VALIDATION_SET_DIR = './dataset_v0.v1i.yolov11/valid/images'
IMAGE_DIRS = [TRAINING_SET_DIR, VALIDATION_SET_DIR]

for directory in IMAGE_DIRS:
    for image_file in os.listdir(directory):
        full_path = f'{directory}/{image_file}'
        img = Image.open(full_path).convert('L')
        img.save(full_path)
        print(f'Succesfully converted: {full_path} to greyscale')
print('Finished')
