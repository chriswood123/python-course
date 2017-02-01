#!/usr/bin/env python

biggest_parcel = {}
biggest = 0

while True:
    print 'Enter a parcel'
    destination = raw_input('Destination: ')
    if destination == '':
        for key in biggest_parcel:
            print "%s: %s" % (key, biggest_parcel[key])
        break
    length = int(raw_input('Length: '))
    width = int(raw_input('Width: '))
    height = int(raw_input('Height: '))
    size = length * width * height
    if size > biggest:
        biggest = size
        biggest_parcel['destination'] = destination
        biggest_parcel['length'] = length
        biggest_parcel['width'] = width
        biggest_parcel['height'] = height


