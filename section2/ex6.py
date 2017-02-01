#!/usr/bin/env python

biggest_parcel = {}
smallest_parcel = {}
biggest = 0
smallest = None

while True:
    print 'Enter a parcel'
    destination = raw_input('Destination: ')
    if destination == '':
        print "Biggest"
        for key in biggest_parcel:
            print "%s: %s" % (key, biggest_parcel[key])
        print "Smallest"
        for key in smallest_parcel:
            print "%s: %s" % (key, smallest_parcel[key])
        break
    dimensions = raw_input('Dimensions (L W H): ')
    length = int(dimensions.split(' ')[0])
    width = int(dimensions.split(' ')[1])
    height = int(dimensions.split(' ')[2])
    size = length * width * height
    if size > biggest:
        biggest = size
        biggest_parcel['destination'] = destination
        biggest_parcel['length'] = length
        biggest_parcel['width'] = width
        biggest_parcel['height'] = height
    if smallest is None or size < smallest:
        smallest = size
        smallest_parcel['destination'] = destination
        smallest_parcel['length'] = length
        smallest_parcel['width'] = width
        smallest_parcel['height'] = height



