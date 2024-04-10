import os
from PIL import Image

screenshots_path = 'screenshots'
wireframes_path = 'wireframes'
stitched_path = 'stitched'

if not os.path.exists(stitched_path):
    os.makedirs(stitched_path)

target_size = (540, 960)

for filename in os.listdir(screenshots_path):
    screenshot_file = os.path.join(screenshots_path, filename)
    wireframe_file = os.path.join(wireframes_path, os.path.splitext(filename)[0] + '.png')
    stitched_file = os.path.join(stitched_path, filename)

    try:
        img1 = Image.open(wireframe_file)
        img2 = Image.open(screenshot_file)

        # Resize if necessary
        if img1.size != target_size:
            img1 = img1.resize(target_size, Image.ANTIALIAS)
        if img2.size != target_size:
            img2 = img2.resize(target_size, Image.ANTIALIAS)

        new_img = Image.new('RGB', (img1.width + img2.width, max(img1.height, img2.height)))
        new_img.paste(img1, (0, 0))
        new_img.paste(img2, (img1.width, 0))
        new_img.save(stitched_file)

        print(f'Successfully stitched: {stitched_file}')

    except Exception as e:
        print(f'Error processing {filename}: {e}')