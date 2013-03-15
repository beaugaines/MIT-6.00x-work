""" A framework for extracting filetype metadata, from Mark Pilgrim's 'Dive into Python'.
I'm spending the time typing it out because I think it's good practice to get good code
'in the fingers' as much as possible.  And I like commenting other people's code - to document
for myself the logic of their work."""

import os
import sys

from UserDict import UserDict


def stripnulls(data):
  "strip whitespace and nulls"
  return data.replace("\00", "").strip()


# create new class inheriting fro UserDict

class FileInfo(UserDict):
  "store file metadata"
  def __init__(self, filename=None):
    UserDict.__init__(self)
    self["name"] = filename


# specific class for extracting MP3 tag data - inheriting from FileInfo class
# the dataMap hash stores the pointers for various bits of information in ID3
# tags, and the method that will be used to process the chunks of info - i.e. stripnulls
# apart from genre, which calls ord - returning the integer ordinal of a one char string

class MP3FileInfo(FileInfo):
  "store ID3 MP3 tags"
  tagDataMap = {
    "title":  (3, 33, stripnulls),
    "artist": (33, 63, stripnulls),
    "album": (63, 93, stripnulls),
    "year": (93, 97, stripnulls),
    "comment": (97, 126, stripnulls),
    "genre": (127, 128, ord)
  }

  # private parse method

  def __parse(self,filename):
    "parse ID3 tags from MP3 file"
    self.clear()
    try:
      fsock = open(filename, 'rb', 0)
      try:
        # 'rewind' to the start of the file and read in its data - the first 128 chars
        fsock.seek(-128,2)
        tagdata = fsock.read(128)
      finally:
        # close the file to free up precious system resources!
        fsock.close()
      if tagdata[:3] == "TAG":
        for tag, (start,end, parseFunc) in self.tagDataMap.items():
          self[tag] = parseFunc(tagdata[start:end])
    except IOError:
      # file does not exist...or the seek fails...or file is corrupted...or...
      pass
