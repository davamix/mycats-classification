This model try to classify pictures of my cats and check who is who in an image using the pre-trained model Xception.

![blacky](./images/Blacky.jpg "Blacky")

![niche](./images/Niche.jpg "Niche")

The videos from where I extracted the images can be downloaded from [here][1] (1.2 GB). Contains 16 folders with 1 video each and 652 images in total extracted from those videos. You can use the [tools/extractor.py][2] to extract new images from the videos.


[1]: https://drive.google.com/file/d/1XQDWcHzNAgqlHcUUfETD9hF9B0gzAmEf/view?usp=sharing

[2]: https://github.com/davamix/mycats-classification/blob/master/tools/extractor.py

## Data folder structure

This is the folders structure I used to organize the data:

```
-data
  |-train
    |-Blacky
    |-Niche
  |-validation
    |-Blacky
    |-Niche
  |-test
    |-Blacky
    |-Niche
```

## Tools

There are two python scripts that helps to work with the data:

### extractor&#46;py ###

This script extract an specific amount of frames from a video
```
python extractor.py --frames 10 video_file.mp4
```
- The value of `--frames` argument is the percentage of frames to be extracted.

- The script accepts the argument `--info` to show information about the video.

### copy_images&#46;py ###

This script split the images contained in the source folder and copy them into train, validation and test folders.

```
python3 copy_images.py -train 70 -validation 20 -test 10 -L Blacky ../data/processed/v9 ../data/
```
- The values of the arguments `-train`, `-validation` and `-test` are percentages.

- `-L` is an optional argument used for copy the images into a subfolder with that name inside the train, validation or test folders, then you don't need move it manually.

