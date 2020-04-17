import pysynth as psb


def k(key):
    le = len(key)
    note = key[0:le - 1]
    value = int(key[-1])
    return tuple([note, value])


def split(keys):
    keys = keys.replace('\n', '').replace('    ', ' ').strip()
    s = []
    for i in keys.split(' '):
        s.append(k(i))
    return s


if __name__ == '__main__':
    trans = split('''
    c58 c58 c58 c58 e58 e58 e58 e58
    d58 d58 d58 d58 g58 g58 g58 g58
    a58 a58 a58 a58 a58 a58 a58 a58
    a58 a58 a58 a58 d58 c58 b48 g48
    ''')
    main = split('''
    a44 a48 e58 d54 c54
    b44 b48 b48 d54 b48 g48
    a44 a48 c68 b58 c68 b58 c68
    a44 a48 c68 b58 c68 b58 c68
    ''')
    song = []
    song.extend(trans)
    song.extend(main)
    song.extend(main)
    psb.make_wav(song, fn="song.wav")
