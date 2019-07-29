# This scripts is used to copy the processed images from data/processed/vn folder to
# data/train, data/validation and data/test folders automatically

import argparse
import os
import sys
import random
import shutil

# List of images
def get_images(source):
    print("Getting images from {}...".format(source))
    images = []
    source_path = source

    if not os.path.isabs(source):
        current_path = os.path.abspath(os.path.dirname(__file__))
        source_path = os.path.join(current_path, source)

    for root,_,  files in os.walk(source_path):
        for file in files:
            if file.endswith(".jpg"):
                images.append(os.path.join(root, file))

    return images

# Shuffle
def shuffle_images(images):
    random.shuffle(images)
    
    return images

# Divide into train, validation and test
def divide_images(images, train=None, validation=None, test=None):
    print("Dividing {} images...".format(len(images)))

    if train is None and validation is None and test is None:
        raise ValueError("[ERROR] At least one of the datasets (train, validation) must have a value bigger than 0")

    if train + validation + test > 100:
        raise ValueError("[ERROR] The total percentage of train + validation + test must be between 0 and 100")

    amount_train_images = 0
    amount_validation_images = 0
    amount_test_images = 0
    total_images = len(images)

    if train is not None:
        amount_train_images = total_images * train * 0.01
        amount_train_images = 1 if amount_train_images > 0 and amount_train_images < 1 else int(amount_train_images)
    if validation is not None:
        amount_validation_images = total_images * validation * 0.01
        amount_validation_images = 1 if amount_validation_images > 0 and amount_validation_images < 1 else int(amount_validation_images)
    if test is not None:
        amount_test_images = total_images * test * 0.01
        amount_test_images = 1 if amount_test_images > 0 and amount_test_images < 1 else int(amount_test_images)

    train_images = []
    validation_images = []
    test_images = []

    train_images = images[0:amount_train_images]

    validation_images = images[amount_train_images:amount_train_images + amount_validation_images]

    test_images = images[amount_train_images + amount_validation_images : amount_train_images + amount_validation_images + amount_test_images]

    return train_images, validation_images, test_images

# Copy to destination folders
def copy_images(images, destination):
    for img in images:
        print("{} --> {}".format(img, destination))
        shutil.copy(img, destination)

parser = argparse.ArgumentParser()
parser.add_argument('source', help='Source folder')
parser.add_argument('destination', help='Destination folder, is the parent folder of train, validation and test folders')
parser.add_argument('-train', '-T', help='Amount of train images to copy, percentage value (int)', type=int)
parser.add_argument('-validation', '-V', help='Amount of validation images to copy, percentage value (int)', type=int)
parser.add_argument('-test', '-t', help='Amount of test image to copy, percentage value(int)', type=int)

args = parser.parse_args()

source_images = get_images(args.source)

source_images = shuffle_images(source_images)

try:
    train_images, validation_images, test_images = divide_images(source_images, args.train, args.validation, args.test)
except ValueError as e:
    print(e)
    sys.exit(1)

train_destination = os.path.join(args.destination, 'train')
validation_destination = os.path.join(args.destination, 'validation')
test_destination = os.path.join(args.destination, 'test')

if len(train_images) > 0:
    print("Copying train images...")
    copy_images(train_images, train_destination)

if len(validation_images) > 0:
    print("Copying validation images...")
    copy_images(validation_images, validation_destination)

if len(test_images) > 0:
    print("Copying test images...")
    copy_images(test_images, test_destination)

print("Total train images: {}".format(len(train_images)))
print("Total validation images: {}".format(len(validation_images)))
print("Total test images: {}".format(len(test_images)))