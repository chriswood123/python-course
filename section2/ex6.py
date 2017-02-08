#!/usr/bin/env python

def update_biggest(size, destination, length, width, height):
    biggest_parcel['destination'] = destination
    biggest_parcel['length'] = length
    biggest_parcel['width'] = width
    biggest_parcel['height'] = height

def update_smallest(size, destination, length, width, height):
    smallest_parcel['destination'] = destination
    smallest_parcel['length'] = length
    smallest_parcel['width'] = width
    smallest_parcel['height'] = height

def print_biggest():
    print "Biggest"
    for key in biggest_parcel:
        print "%s: %s" % (key, biggest_parcel[key])

def print_smallest():
    print "Smallest"
    for key in smallest_parcel:
        print "%s: %s" % (key, smallest_parcel[key])


def parse_dim_string(text):
    elements = text.split(' ')
    if len(elements) != 3:
        raise ValueError("There must be three elements seperated by spaces")
    dims = []
    for i in elements:
        try:
            dims.append(int(i))
        except ValueError:
            raise ValueError('Could not convert text to integer "{0}"'.format(i))
    return dims

def get_dims_from_user():
    while True:
        try:
            dim_string = raw_input('Dimensions (L W H): ')
            parsed_dims = parse_dim_string(dim_string)
            return parsed_dims
        except ValueError as e:
            print(e)


def main():
    biggest_parcel = {}
    smallest_parcel = {}
    biggest = 0
    smallest = None
    while True:
        print 'Enter a parcel'
        destination = raw_input('Destination: ')
        if destination == '':
            print_biggest()
            print_smallest()
            break
        try:
            parsed_dims = get_dims_from_user()
        except KeyboardInterrupt:
            print('\nBad dimensions, cacelling parcel')
            continue
        length = int(parsed_dims[0])
        width = int(parsed_dims[1])
        height = int(parsed_dims[2])
        size = length * width * height
        if size > biggest:
            biggest = size
            update_biggest(size, destination, length, width, height)
        if smallest is None or size < smallest:
            smallest = size
        update_smallest(size, destination, length, width, height)


if __name__ == '__main__':
    main()
