#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import HTMLParser

h = HTMLParser.HTMLParser()
s = h.unescape('&#24314;&#20110;1826&#24180;&#65292;&#26159;&#32445;&#32422;&#24066;')
print s
