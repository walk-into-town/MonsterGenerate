##해당 파일들은 https://github.com/MatthewRayfield/pokemon-gpt-2 에서 가져 왔습니다.##

# Pokemon GPT-2

This repo contains EVERYTHING you need to train a GPT-2 model with images of your choosing THEN generate new images with that model.

## Google Colab Notebooks

There's a good chance you can do what you want directly with Google Colab (and use a shiny free GPU):

- [Pokemon GPT-2 Train Colab Notebook](https://colab.research.google.com/drive/1c1kmO9tixviyBB7IGh-jVpLvOh2RpLYk)
- [Pokemon GPT-2 Generate Colab Notebook](https://colab.research.google.com/drive/1qgt8cSwKF957PgPTKhRcNwDIfWrMhbV9)

## Files

For those of you (sickos!) that want to run this code locally, here is a rundown of the key files:

- **image-to-text.py** - Converts images into a text-based format for training.
- **text-to-image.py** - Converts text-based image format into a PNG.
- **train.py** - Trains a GPT-2 model with input text.
- **generate.py** - Generates images with a trained model.
- **misc/** - This folder contains things that are probably not useful but were used in this project. USE AT YOUR OWN PERIL !
    - **image-to-text.js** - The original Javascript implementation of image-to-text (outofdate!)
    - **remove-background.js** - Removes white surrounding an image and replaces with transparent pixels. 
    - **resize.js** - Centers images into a certain size. I don't remember why I didn't just use imagemagick, but I *must* have had a good reason.
    - **text-to-image.js** - The original Javascript implementation of text-to-image (outofdate!)

## Instructions

So you want to do the thing ? You don't just want to use the Google Colab Notebook ? Weird, but okay try this:

1. Install the requirements. People like to do that like this: `pip install -r requirements.txt`
2. Get your input images into a folder. I used a bunch of Pokemon sprites all sized to 64x64.
3. Convert those images into a big text file like this: `python image-to-text.py images/*.jpg > all-image.txt`
4. Modify (i trust you) train.py to your liking. Good stuff start at line 8. More steps = more training.
5. Run train.py and wait a long time !
6. Make a folder named "output". (yeah yeah)
7. Now modify generate.py to your needs. Line 6-9 and line 27. Temp in line 35 controls "craziness" of output.
8. Run generate.py and wait a long time !
9. Turn the output texts into images with: `python text-to-image.py output/*.txt`
10. Enjoy your sprites in output folder !
11. Tweak input, settings, etc. and repeat !

## Pre-Trained Model

If you want to generate sprites with a model already trained on Pokemon sprites you can download my model here: [pokemon-gpt-2-multigen-250000.zip](https://ipfs.io/ipfs/QmRjkH2szrkez3QaHUKPM1jr3aHnJyN11JpcoRM2EwFHdQ?filename=pokemon-gpt-2-multigen-250000.zip)

To use this, make a folder named "checkpoint" and place the unzipped pokemon-gpt-2-multigen-250000 folder there then follow above instructions from step 8 on.

## Thanks !

Big thanks to the [GPT-2-Simple](https://github.com/minimaxir/gpt-2-simple) project by Max Woolf. I wouldn't have done any of this if that project hadn't made GPT-2 work so straight forward.

## How to use?
1. GenerateModule.py와 pokemon-gpt-2-multigen-250000.zip 을 다운 받아줍니다.
2. pip install -r requirements.txt를 해주고 tensorflow=1.15 버전을 다운받아 줍시다.(vs코드에서 아나콘다를 사용할시에 텐서플로에 import에러가 생깁니다. 텐서플로는 아나콘다에서 따로 설치해 줍시다.그리고 저는 파이썬 3.7 버전을 사용했습니다.) 
3. 해당 파일이 있는 위치에 checkpoint폴더를 생성해주고 pokemon-gpt-2-multigen-250000.zip의 압축을 풀어줍니다.
4. GenerateModule.py를 실행시켜줍니다.
5. pokemon-gpt-2-image 파일이 생성되고 해당 폴더에 이미지들이 저장됩니다.
