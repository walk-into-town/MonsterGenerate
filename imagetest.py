#폴더 찾고 이미지를 불러오는 것을 테스트 하는 파ㅣㅇㄹ.
#뭘 해야할까?
#일단 폴더의 경로를 찾는다
#폴더 경로에 있는 파일을 찾는다
#파일 이름을 띄운다
#파일이 이미지면 띄운다
#파일이 이미지면 프린트 성공
#파일이 이미지가 아니거나 널이면 실패출력
import glob
import os
from PIL import Image
import math

#여기 폴더 경로 찾기
imgs=glob.glob('pokemon/*.jpg')

#여기 폴더 파일 찾기
print(os.path.exists('pokemon'))

for img in imgs:
    image = Image.open(img).convert('RGBA')
    pixels = image.load()
    width = image.size[0]
    height = image.size[1]
    lines = []

    for y in range(height):
        split = ['%02dd' % y]

        for x in range(width):
            color = pixels[x, y] 

            s = '~'

            if len(color) < 4 or color[3] > 128:
                r = color[0]
                g = color[1]
                b = color[2]
               
                if r == 85 and g == 85 and b == 85:
                    s = 'a' # use grayscale character 1

                elif r == 170 and g == 170 and b == 170:
                    s = 'b' # use grayscale character 2

                else: # use one of 64 color characters
                    mR = math.floor(r/64)
                    mG = math.floor(g/64)
                    mB = math.floor(b/64)

                    c = 0

                    c += mR
                    c = c << 2
                    c += mG
                    c = c << 2
                    c += mB

                    s = chr(c+33)

            split.append(s)

        lines.append(' '.join(split))

    reversed = []
    for line in lines:
        reversed.insert(0, (line.replace('d ', 'u ', 1)))

    print('\n'.join(reversed))
    print('\n'.join(lines))

print('성공')