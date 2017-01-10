from visidata import *

class open_zip(Sheet):
    def __init__(self, p):
        super().__init__(p.name, p)

    def reload(self):
        import zipfile
        with zipfile.ZipFile(self.source.resolve(), 'r') as zfp:
            self.rows = zfp.infolist()
        self.columns = AttrColumns('filename file_size date_time compress_size'.split())
        self.command('^J', 'vd.push(openZipFileEntry(cursorRow))', 'open this file')

    def openZipFileEntry(self, zi):
        import zipfile
        cachefn = zi.filename
        if not os.path.exists(cachefn):
            with zipfile.ZipFile(self.source.resolve(), 'r') as zfp:
                self.zfp.extract(zi)
        return openSource(cachefn)