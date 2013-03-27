from sgmlib import SGMLParser
import htmlentitydefs

class BaseHTMLProcessor(SGMLParser):

  def reset(self):
    # extend (called by SGMLParser.__init__)
    self.pieces = []
    SGMLParser.reset(self)

  def unknown_starttag(self, tag, attrs):
    '''called for each start tag; attrs is a list of (attr,value) tuples;
    e.g. for <section class="screen"> you'd get tag="section", attrs=[("class", "screen")]
    All non-HTML code must be enclosed in comments of the form <!--  .... --> to ensure
    it will pass through the parser unaltered. 
    '''
    strattrs = "".join([' %s="%s"' % (k,v) for k, v in attrs])
    self.pieces.append("<%(tag) s% (strattrs)" % locals())


  def unknown_endtag(self, tag):
    '''called for each end tag, e.g. for </section>, tag will be "section"'''
    self.pieces.append("</%(tag)s" % locals())

  def handle_charref(self, ref):
    '''called for each character reference; e.g. for "&#160;" the ref will be "160"'''
    self.pieces.append("&#%(ref)s;" % locals())

  def handle_entityref(self, ref):
    ''' called for each entity ref; e.g. for "&copy;", ref will be "copy".  Standard
    HTML entities are closed with semicolon; other entities are not.
     '''
    self.pieces.append("&%(ref)s;" % locals())
    if htmlentitydefs.entitydefs.has_key(ref):
      self.pieces.append(";")

  def handle_data(self, text):
    '''called for each block of plain text, i.e. outside of any tag and not containing
    any character or entity refs.  stores the text verbatim.
    '''
    self.pieces.append(text)

  def handle_comment(self, text):
    '''called for each HTML comment '''
    self.pieces.append("<!--%(text)s-->" % locals())

  def handle_pi(self, text):
    '''called for each processing instruction, e.g. <?instruction>'''
    self.pieces.append("<?%(text)s" % locals())

  def handle_decl(self, text):
    '''called for the doctype, if present'''
    self.pieces.append("<!%(text)s" % locals())

  def output(self):
    '''return processed html as a single string'''
    return ''.join(self.pieces)