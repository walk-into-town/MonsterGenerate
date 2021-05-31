
import gpt_2_simple as gpt2
from datetime import datetime

import os
import sys
import time
import re
import gpt_2_simple as gpt2
import shutil
import math
from PIL import Image

run_name = 'pokemon-gpt-2-multigen-250000'

output_folder = 'pokemon-gpt-2-image' #@param {type:"string"}
generate_count = 3000 #@param {type:"integer"}
temperature = 1.07 #@param {type:"slider", min:0.9, max:1.3, step:0.01}
width = 64 #@param {type:"integer"}
height =  64#@param {type:"integer"}
save_texts = False #@param {type:"boolean"}

def createImage(text, path):
    lines = text.split('\n')

    imageWidth = 0
    imageHeight = 0

    for line in lines:
        split = line.split(' ')

        marker = split[0]
        match = re.search("^([0-9]+)([du])$", marker)

        if match:
            groups = match.groups()
            index = int(groups[0])

            width = len(split) - 1
            height = index + 1

            if width > imageWidth:
                imageWidth = width

            if height > imageHeight:
                imageHeight = height

    pixels = []
    for y in range(imageHeight):
        for x in range(imageWidth):
            pixels.append((0, 0, 0, 0))

    for line in lines:
        split = line.split(' ')

        marker = split[0]
        match = re.search("^([0-9]+)([du])$", marker)

        if match:
            groups = match.groups()
            index = int(groups[0])

            for x in range(len(split) - 1):
                s = split[x + 1]

                if s != '~':
                    r = 0
                    g = 0
                    b = 0
                    
                    if s == 'a':
                        r = g = b = 107
                    elif s == 'b':
                        r = g = b = 187
                    else:
                        c = ord(s[0]) - 33

                        b = (c & 3) * 64
                        if b == 192:
                            b += 63

                        c = c >> 2
                        g = (c & 3) * 64
                        if g == 192:
                            g += 63

                        c = c >> 2
                        r = (c & 3) * 64
                        if r == 192:
                            r += 63

                    i = (index * imageWidth) + x

                    pixels[i] = (r, g, b, 255)

    image = Image.new('RGBA', (imageWidth, imageHeight))
    image.putdata(pixels)
    image.save(path)

def blankLines():
    lines = []

    for i in range(0, height):
        lines.append('')

    return lines

sess = None

for ii in range(0, generate_count):
    print(ii)
    
    if not sess:
        sess = gpt2.start_tf_sess()
    else:
        sess = gpt2.reset_session(sess)
    
    gpt2.load_gpt2(sess, run_name=run_name)

    lines = blankLines()
    prefix = ''
    hasColor = False

    while True:
        text = gpt2.generate(sess, run_name=run_name, prefix=prefix, temperature=temperature, return_as_list=True)[0]

        print('\n\noutput:')
        print(text)

        newLines = text.split('\n')

        direction = None
        lastIndex = None
        for line in newLines:
                split = line.split(' ')[:width + 2]

                if len(split) < 55:
                    break

                marker = split[0]
                match = re.search("^([0-9]+)([du])$", marker)

                if match:
                    groups = match.groups()

                    try:
                        index = int(groups[0])
                    except:
                        break

                    if direction == None:
                        direction = groups[1]

                    if groups[1] != direction:
                        print('direction changed')
                        break

                    if lastIndex != None:
                        if groups[1] == 'd' and index <= lastIndex:
                            print('bad line order')
                            break
                        elif groups[1] == 'u' and index >= lastIndex:
                            print('bad line order')
                            break
                    lastIndex = index

                    split[0] = marker.replace('u', 'd')

                    if not hasColor:
                        for character in split[2:]:
                            if character != '~' and character != '`':
                                hasColor = True
                                break

                    while len(split) < width:
                        split.append('~')

                    try:
                        lines[index] = ' '.join(split)
                    except IndexError:
                        break

        if not hasColor:
            print('no color')
            lines = blankLines()
            continue

        topIndex = None
        for i in range(0, height):
            if lines[i]:
                topIndex = i
                break

        bottomIndex = None
        for i in range(topIndex, height):
            if lines[i]:
                bottomIndex = i
            else:
                break

        print('\n\ntop %i bottom %i' % (topIndex, bottomIndex))

        sectionSize = 5
        if topIndex > 0:
            section = lines[topIndex:min(topIndex+sectionSize+1, bottomIndex+1)]
            section.reverse()
            for i in range(0, len(section)):
                section[i] = section[i].replace('d', 'u')

        elif bottomIndex < height - 1:
            section = lines[max(bottomIndex-sectionSize, topIndex):bottomIndex+1]

        else:
            print('\n'.join(lines))
            filename = '%i' % int(time.time())
            text = '\n'.join(lines)

            if not os.path.exists('./%s' % output_folder):
                os.makedirs('./%s' % output_folder)

            if save_texts:
                text_file = open('./%s/%s.txt' % (output_folder, filename), 'w')
                text_file.write(text)
                text_file.close()
            
            createImage(text, './%s/%s.png' % (output_folder, filename))

            print('saved !')
            break

        prefix = '\n'.join(section)
        print('\n\nprefix:\n%s' % prefix)