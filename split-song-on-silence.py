#!/usr/bin/python

import pydub
import sys
import os

if len(sys.argv) < 2:
    print "usage: %s <song-file-path>" % sys.argv[0]
    exit(1)

input_song = sys.argv[1]
input_file, input_ext = os.path.splitext(input_song)

song = pydub.AudioSegment.from_file(input_song)

chunks = pydub.silence.split_on_silence(song, 400, -30, 400)

for i, chunk in enumerate(chunks):
    with open("%s-%s%s" % (input_file, i, input_ext), "wb") as f:
        chunk.export(f, format="mp3", parameters=["-filter:a", "atempo=0.8"])
