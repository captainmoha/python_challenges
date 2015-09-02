import Image


def oxygen():
    file_name = 'oxygen.png'
    img = Image.open(file_name)
    img_size = width, height = img.size

    # after inspecting the image I think the bar of shades of grey is the key
    # I'm gonna crop the image and leave only that
    area_to_crop = (0, 44, 607, 51)
    cropped_img = img.crop(area_to_crop)
    cropped_img.save('cropped_' + file_name)

    # then I am gonna work with the cropped image
    imgData = list(cropped_img.getdata())

    # print imgData
    # observing the imgData list I noticed that each color has the same rgb components
    # let's save the values in a list.
    color_list = []
    for color in imgData:
        if color[0] not in color_list:
            # color[0] or 1 or 2. because they are all the same except for the
            # alpha channel
            color_list.append(color[0])
    print color_list
    for c in color_list:
        print chr(c),
    # output
    # s m a r t   g u y , o d e i . h n x l v [ 1 0 5 6 3 4 2 ]
    # well that's not very helpful but I think I am close I need to get the
    # colors differently


def oxygen2():

    file_name = 'oxygen.png'
    img = Image.open(file_name)
    img_size = width, height = img.size

    # after inspecting the image I think the bar of shades of grey is the key
    # I'm gonna crop the image and leave only that
    area_to_crop = (0, 43, 608, 51)
    cropped_img = img.crop(area_to_crop)
    cropped_img.save('cropped_' + file_name)

    # then I am gonna work with the cropped image
    # since the other way didn't work I'm gonna use a different way to get the values of the colors
    # gonna go through each block instead of going through the whole image

    start = 0  # starting x coordinate
    end = 606  # ending x coordinate
    step = 7  # step to jumb through blocks
    y = 2		# y coordinate
    color_values_list = []

    for x in range(start, end, step):
        coordinate = (x, y)
        block_color = cropped_img.getpixel(coordinate)
        color_values_list.append(block_color[0])
    # print color_values_list
    
    # what if I convert the numbers in the list to ascii charachters?
    potential_str = ''
    for value in color_values_list:
        potential_str += chr(value)

    print potential_str
    # It worked! output: smart guy, you made it. the next level is [105, 110,
    # 116, 101, 103, 114, 105, 116, 121]

    # let's convert that list into ascii also
    next_level = ''
    lista = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    for value in lista:
        next_level += chr(value)

    print next_level
    # it worked !

oxygen2()
