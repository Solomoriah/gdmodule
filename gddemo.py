#!/usr/bin/env python

import gd, os, cStringIO, urllib2

os.environ["GDFONTPATH"] = "."

FONT = "adventure"

def simple():
    im = gd.image((200, 200))

    white = im.colorAllocate((255, 255, 255))
    black = im.colorAllocate((0, 0, 0))
    red = im.colorAllocate((255, 0, 0))
    blue = im.colorAllocate((0, 0, 255))

    im.colorTransparent(white)
    im.interlace(1)

    im.rectangle((0,0),(199,199),black)
    im.arc((100,100),(195,175),0,360,blue)
    im.fill((100,100),red)

    print im.get_bounding_rect(FONT, 12.0, 0.0, (10, 100), "Hello Python")

    im.string_ttf(FONT, 20.0, 0.0, (10, 100), "Hello Python", black)

    f=open("xx.png","w")
    im.writePng(f)
    f.close()

    f=open("xx.jpg", "w")
    im.writeJpeg(f,100)
    f.close()

    f=cStringIO.StringIO()
    im.writePng(f)
    print "PNG size:", len(f.getvalue())
    f.close()
    
    f = urllib2.urlopen("http://www.gnu.org/graphics/gnu-head-sm.jpg")
    im = gd.image(f, "jpg")
    f.close()
    print "GNU Image Size:", im.size()

simple()

