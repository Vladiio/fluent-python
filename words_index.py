import re
import sys

WORD_RE = re.compile('\w+')

def main(filename):
    index = {}


    with open(filename) as file:
        for line_number, line_text in enumerate(file.readlines()):
            for match in WORD_RE.finditer(line_text):
                world = match.group()
                column_number = match.start() + 1
                location = (line_number, column_number)
                occurrences = index.get(world, [])
                occurrences.append(location)
                index[world] = occurrences




if __name__ == '__main__':
    main(sys.argv[-1])
