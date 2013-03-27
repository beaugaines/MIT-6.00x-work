import re

from BaseHTMLProcessor import BaseHTMLProcessor

class Dialectizer(BaseHTMLProcessor):

  subs = ()

  def reset(self):
    '''extend (called from __init__ in ancestor)'''
    self.verbatim = 0
    BaseHTMLProcessor.reset(self)