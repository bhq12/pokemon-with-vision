import os
from PIL import Image
import random
import torch
from torchvision.transforms import v2

DATASET_PATH = "./custom_dataset"

#TODO REMAINING:
#- Fix bounding box label format for the sprites on image creation 
#- Add object sprites to the source data (houses, pokecenter, trees, water, etc.)
#- Explore more transforms
#- Generate train, test, and validate sets
#- Crank the dataset size from 100 to thousands

def randomly_place_sprite(image, sprite):
    image_height, image_width = image.size
    sprite_height, sprite_width = sprite.size

    # Ensure the sprite fits in the image
    max_x = image_width - sprite_width
    max_y = image_height - sprite_height

    sprite_x = int(max_x * random.random())
    sprite_y = int(max_y * random.random())


    print(f'image_width: {image_width}, image_width: {image_width}')
    print(f'sprite_width: {sprite_width}, sprite_width: {sprite_width}')
    print(f'sprite_x: {sprite_x}, sprite_y: {sprite_y}')

    Image.Image.paste(image, sprite, (sprite_x, sprite_y))

    return [
        str(sprite_x - (sprite_width // 2)),
        str(sprite_x + (sprite_width // 2)),
        str(sprite_y - (sprite_height // 2)),
        str(sprite_y + (sprite_height // 2))
    ]


def generate_new_image(file_number):
    new_image = Image.new("RGB", (144, 160), (255, 255, 255))
    selected_sprites = []
    labels = []
    for i in range(int(3 * random.random())):
        # Open random sprite
        sprites = os.listdir('./pokemon_sprites')
        selected_sprite = sprites[int(len(sprites) * random.random())]
        sprite = Image.open(f'./pokemon_sprites/{selected_sprite}')
        selected_sprites.append(selected_sprite.replace('.png', ''))


        # randomly distort the sprite
        transforms = v2.Compose([
            v2.RandomAffine(degrees=30, scale=(0.7,1.3), translate=(0.2,0.2), fill=255),
            v2.RandomPerspective(distortion_scale=0.3, fill=255),
            #v2.ElasticTransform(fill=255)
        ])

        transformed_sprite = transforms(sprite)

        # place the transformed sprite on the blank image
        label_location = randomly_place_sprite(new_image, transformed_sprite)
        labels.append([selected_sprite] + label_location)

    file_name = f"{file_number}_{'_'.join(selected_sprites)}"
    image_path = f"{DATASET_PATH}/train/images/{file_name}.png"
    label_path = f"{DATASET_PATH}/train/labels/{file_name}.txt"
    new_image.save(image_path, "PNG")
    label_file = open(label_path, 'w+')
    for label in labels:
        print(' '.join(label) + '\n')
        label_file.write(' '.join(label) + '\n')
    label_file.close()

def setup_dataset_directories():
    os.makedirs(f"{DATASET_PATH}/train/images", exist_ok=True)
    os.makedirs(f"{DATASET_PATH}/train/labels", exist_ok=True)
    os.makedirs(f"{DATASET_PATH}/test/images", exist_ok=True)
    os.makedirs(f"{DATASET_PATH}/test/labels", exist_ok=True)
    os.makedirs(f"{DATASET_PATH}/val/images", exist_ok=True)
    os.makedirs(f"{DATASET_PATH}/val/labels", exist_ok=True)


setup_dataset_directories()
for i in range(100):
    generate_new_image(i)
