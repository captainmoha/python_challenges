import pickle


def dePeekHell():
    inputFile = open("banner.p", 'rb')
    result = pickle.load(inputFile)
    outputFile = open("output.py", 'w')
    outputFile.write(str(result))


dePeekHell()
# output is a list of lists of tuples
banner = [[(' ', 95)], [(' ', 14), ('#', 5), (' ', 70), ('#', 5), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)], [(' ', 6), ('#', 3), (' ', 6), ('#', 4), (' ', 3), ('#', 3), (' ', 9), ('#', 3), (' ', 7), ('#', 5), (' ', 3), ('#', 3), (' ', 4), ('#', 5), (' ', 3), ('#', 3), (' ', 10), ('#', 3), (' ', 7), ('#', 4), (' ', 1)], [(' ', 3), ('#', 3), (' ', 3), ('#', 2), (' ', 4), ('#', 4), (' ', 1), ('#', 7), (' ', 5), ('#', 2), (' ', 2), ('#', 3), (' ', 6), ('#', 4), (' ', 1), ('#', 7), (' ', 3), ('#', 4), (' ', 1), ('#', 7), (' ', 5), ('#', 3), (' ', 2), ('#', 3), (' ', 5), ('#', 4), (' ', 1)], [(' ', 2), ('#', 3), (' ', 5), ('#', 3), (' ', 2), ('#', 5), (' ', 4), ('#', 4), (' ', 3), ('#', 3), (' ', 3), ('#', 4), (' ', 4), ('#', 5), (' ', 4), ('#', 4), (' ', 2), ('#', 5), (' ', 4), ('#', 4), (' ', 3), ('#', 3), (' ', 5), ('#', 3), (' ', 3), ('#', 4), (' ', 1)], [(' ', 1), ('#', 3), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 3), (' ', 4), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 6), ('#', 4), (' ', 2), ('#', 4), (' ', 1)], [(' ', 1), ('#', 3), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 10), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 7), ('#', 3), (' ', 2), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 2), (' ', 3),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 7), ('#', 3), (' ', 2), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 10), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 14), (' ', 2), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 4), ('#', 4), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 12), ('#', 4), (' ', 1)], [('#', 4), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 5), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 12), ('#', 4), (' ', 1)], [(' ', 1), ('#', 3), (' ', 11), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 5), ('#', 3), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 12), ('#', 4), (' ', 1)], [(' ', 2), ('#', 3), (' ', 6), ('#', 2), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 4), ('#', 4), (' ', 4), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 3), (' ', 6), ('#', 2), (' ', 3), ('#', 4), (' ', 1)], [(' ', 3), ('#', 3), (' ', 4), ('#', 2), (' ', 3), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 11), (' ', 3), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 4), (' ', 5), ('#', 4), (' ', 4), ('#', 3), (' ', 4), ('#', 2), (' ', 4), ('#', 4), (' ', 1)], [(' ', 6), ('#', 3), (' ', 5), ('#', 6), (' ', 4), ('#', 5), (' ', 4), ('#', 2), (' ', 4), ('#', 4), (' ', 1), ('#', 6), (' ', 4), ('#', 11), (' ', 4), ('#', 5), (' ', 6), ('#', 3), (' ', 6), ('#', 6)], [(' ', 95)]]

# I think it's a drawing or something


def draw(lista):
    drawing = open("drawing.txt", 'w')
    for line in lista:
        for glyph in line:
            for char in range(glyph[1]):
                drawing.write(glyph[0])
        drawing.write('\n')

draw(banner)

# output: Channel
# solved!

