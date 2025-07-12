import os
from PIL import Image
import random
import torch
from torchvision.transforms import v2

#TODO REMAINING:
#- Generate bounding box labels on image creation
#- Add object sprites to the source data (houses, pokecenter, trees, water, etc.)
#- Explore more transforms
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


def generate_new_image(file_number):
    new_image = Image.new("RGB", (144, 160), (255, 255, 255))
    selected_sprites = []
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
        randomly_place_sprite(new_image, transformed_sprite)


    new_image.save(f"./custom_dataset/{file_number}_{'_'.join(selected_sprites)}.png", "PNG")

for i in range(100):
    generate_new_image(i)
