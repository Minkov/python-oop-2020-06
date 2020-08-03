BUFFER_SIZE = 1 << 10


def get_str(bytes):
    try:
        return bytes.decode()
    except:
        return bytes


def read_all(stream):
    stream.seek(0)
    parts = []

    while True:
        part = stream.read(BUFFER_SIZE)
        if not part:
            break
        parts.append(part)

    return ''.join(get_str(x) for x in parts)
