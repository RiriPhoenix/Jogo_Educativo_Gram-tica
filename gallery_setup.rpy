init python:

    def MaxScale(img, minwidth=config.screen_width, minheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(minwidth) / currwidth
        yscale = float(minheight) / currheight

        if xscale > yscale:
            maxscale = xscale
        else:
            maxscale = yscale

        return im.FactorScale(img, maxscale, maxscale)

    def MinScale(img, maxwidth=config.screen_width, maxheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(maxwidth) / currwidth
        yscale = float(maxheight) / currheight

        if xscale < yscale:
            minscale = xscale
        else:
            minscale = yscale

        return im.FactorScale(img, minscale, minscale)

    maxnumx = 2
    maxnumy = 2
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    closeup_page = 0


    class GalleryItem:
        def __init__(self, name, images, thumb, locked="lockedthumb"):
            self.name = name
            self.images = images
            self.thumb = thumb
            self.locked = locked
            self.refresh_lock()

        def num_images(self):
            return len(self.images)

        def refresh_lock(self):
            self.num_unlocked = 0
            lockme = False
            for img in self.images:
                if not renpy.seen_image(img):
                    lockme = True
                else:
                    self.num_unlocked += 1
            self.is_locked = lockme


    gallery_items = []
    #gallery_items.append(GalleryItem("Capitulo1", ["cg0"], "thumb1")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg1"], "thumb1")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg2", "cg2_2"], "thumb2")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg3", "cg4", "cg5", "cg6", "cg7"], "thumb3")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg8"], "thumb8")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg9"], "thumb9")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg10"], "thumb10")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg11"], "thumb11")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg12"], "thumb12")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg13"], "thumb13")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg14"], "thumb14")) # Ok
