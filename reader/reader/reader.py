import os

from reader.compressed import bzipped, gzipped

extention_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener,
}

class Reader:
    def __init__(self, filename, *args, **kwargs):
        extension = os.path.splitext(filename)[1]
        opener = extention_map.get(extension, open)
        self.f = opener(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()