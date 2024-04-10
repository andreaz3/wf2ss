import os
import shutil
import tarfile
from random import shuffle

stitched_path = 'stitched'
train_path = 'train'
test_path = 'test'
val_path = 'val'
archive_path = 'wireframes2screenshots.tar.gz'

for path in [train_path, test_path, val_path]:
    if not os.path.exists(path):
        os.makedirs(path)

images = [f for f in os.listdir(stitched_path) if os.path.isfile(os.path.join(stitched_path, f))]
shuffle(images)

total_images = len(images)
train_split = int(0.8 * total_images)
test_split = train_split + int(0.1 * total_images)

train_images = images[:train_split] # 80% for train
test_images = images[train_split:test_split] # 10% for train
val_images = images[test_split:] # 10% for train

def copy_files(files, source, destination):
    for f in files:
        shutil.copy(os.path.join(source, f), os.path.join(destination, f))
    print(f"Copied {len(files)} files to {destination}")

copy_files(train_images, stitched_path, train_path)
copy_files(test_images, stitched_path, test_path)
copy_files(val_images, stitched_path, val_path)

def compress_folders(folders, archive_name):
    with tarfile.open(archive_name, "w:gz") as tar:
        for folder in folders:
            tar.add(folder, arcname=os.path.basename(folder))
    print(f"Compressed folders into {archive_name}")

compress_folders([train_path, test_path, val_path], archive_path)
