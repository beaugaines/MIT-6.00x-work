"""Kant Generator for Python
    From Mark Pilgrim's 'Dive into Python' - which I'm really enjoying
    by the way, thanks Mark.

    Generates mock philosophy based on a context−free grammar
    Usage: python kgp.py [options] [source]

    Options:
    −g ..., −−grammar=...   use specified grammar file or URL
    −h, −−help              show this help
    −d                      show debugging information while parsing

    Examples:
    kgp.py                          generates several paragraphs of Kantian philosophy
    kgp.py −g husserl.xml           generates several paragraphs of Husserl
    kpg.py "<xref id='paragraph'/>" generates a paragraph of Kant
    kgp.py template.xml             reads from template.xml to decide what to generate
"""

from xml.dom import minidom
import random
import toolbox
import sys
import getopt

# sto eto?
_debug = 0

s
