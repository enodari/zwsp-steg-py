MODE_ZWSP = 0
MODE_FULL = 1

ZERO_WIDTH_SPACE = '\u200b'
ZERO_WIDTH_NON_JOINER = '\u200c'
ZERO_WIDTH_JOINER = '\u200d'
LEFT_TO_RIGHT_MARK = '\u200e'
RIGHT_TO_LEFT_MARK = '\u200f'

list_ZWSP = [
    ZERO_WIDTH_SPACE,
    ZERO_WIDTH_NON_JOINER,
    ZERO_WIDTH_JOINER,
]

list_FULL = [
    ZERO_WIDTH_SPACE,
    ZERO_WIDTH_NON_JOINER,
    ZERO_WIDTH_JOINER,
    LEFT_TO_RIGHT_MARK,
    RIGHT_TO_LEFT_MARK,
]


def get_padding_length(mode):
    return 11 if mode == MODE_ZWSP else 7  # Keep padding as small as possible


def to_base(num, b, numerals='0123456789abcdefghijklmnopqrstuvwxyz'):
    """
    Python implementation of number.toString(radix)
    Thanks to jellyfishtree from https://stackoverflow.com/a/2267428
    """
    return ((num == 0) and numerals[0]) or (to_base(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


def encode(message, mode=MODE_FULL):
    if not isinstance(message, str):
        raise TypeError('Cannot encode {0}'.format(type(message).__name__))

    alphabet = list_ZWSP if mode == MODE_ZWSP else list_FULL
    padding = get_padding_length(mode)
    encoded = ''

    if (len(message) == 0):
        return ''

    for message_char in message:
        code = '{0}{1}'.format('0' * padding, int(str(to_base(ord(message_char), len(alphabet)))))
        code = code[len(code) - padding:]
        for code_char in code:
            index = int(code_char)
            encoded = encoded + alphabet[index]

    return encoded


def decode(message, mode=MODE_FULL):
    if not isinstance(message, str):
        raise TypeError('Cannot decode {0}'.format(type(message).__name__))

    alphabet = list_ZWSP if mode == MODE_ZWSP else list_FULL
    padding = get_padding_length(mode)
    encoded = ''
    decoded = ''

    for message_char in message:
        if message_char in alphabet:
            encoded = encoded + str(alphabet.index(message_char))

    if (len(encoded) % padding != 0):
        raise TypeError('Unknown encoding detected!')

    cur_encoded_char = ''

    for index, encoded_char in enumerate(encoded):
        cur_encoded_char = cur_encoded_char + encoded_char
        if index > 0 and (index + 1) % padding == 0:
            decoded = decoded + chr(int(cur_encoded_char, len(alphabet)))
            cur_encoded_char = ''

    return decoded
