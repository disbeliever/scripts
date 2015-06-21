#!/usr/bin/env python3

import os
import sys
import re


class ExtM3UPlaylist():

    def __init__(self, filename):
        self.entries = []
        self.filename = filename
        try:
            with open(os.path.expanduser(filename)) as f:
                lines = list(map(lambda x: x.rstrip(), f.readlines()))
        except IOError as e:
            print("{0}: {1}".format(e.args[1], os.path.expanduser(filename)))
            return None
        if (lines[0].rstrip() != "#EXTM3U"):
            print("Doesn't look like moc playlist")
            return None

        for l in lines[1:]:
            filename = ""
            extinf = ""
            # if l.startswith("#EXTINF"):
            #    extinf = l
            if not l.startswith("#"):
                filename = l
            if (filename != ""):
                self.entries.append(ExtM3UEntry(filename, extinf))

    def __str__(self):
        return "#EXTM3U" + ''.join([x.extinf +
                                    "\n" +
                                    x.filename for x in self.entries])

    def is_file_exist(self, e):
        try:
            os.stat(e.filename)
            return True
        except OSError:
            return False

    def purge_non_existent(self):
        len_before = len(self.entries)
        self.entries = list(filter(self.is_file_exist, self.entries))
        len_after = len(self.entries)
        return len_before - len_after

    def write(self):
        with open(os.path.expanduser(self.filename), "w") as f:
            f.write(str(self))


class ExtM3UEntry():

    def __init__(self, filename, extinf):
        self.filename = filename
        self.extinf = extinf

    def __str__(self):
        return self.extinf + "\n" + self.filename


def main():
    playlist = ExtM3UPlaylist("~/.moc/playlist.m3u")
    if (len(playlist.entries) == 0):
        return 1

    removed_count = playlist.purge_non_existent()
    playlist.write()
    print(playlist)
    print("Removed {0} items".format(removed_count))


if __name__ == "__main__":
    sys.exit(main())
