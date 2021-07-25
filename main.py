import argparse


morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...---', '4': '....-', '5': '......', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----',
}


def find_character(inputs: str):
    convert = ''
    for key in inputs:
        if key == '-':
            value = '       '
            convert += value
        else:
            value = morse_code.get(key)
            if value:
                convert += value + '   '
            else:
                return "Have Character can't convert to morse code"
    return convert


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="text convert to morse code and use - for separate words.")
    parser.add_argument("-v", "--verbose", help="increase output verbosity.", action="store_true")
    args = parser.parse_args()
    result = find_character(args.echo)
    if args.verbose:
        print("verbosity turn on.")

    print(result)
