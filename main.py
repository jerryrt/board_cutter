from rectpack import newPacker
from PIL import Image, ImageDraw

rectangles = [(100, 30), (40, 60), (30, 30),(70, 70), (100, 50), (30, 30), (30, 30), (30, 30), (30, 30), (100, 50), (100, 50),(290, 150), (290, 150), (290, 150)]
bins = [(1200, 2400), (1200, 2400),(1200, 2400),(1200, 2400),(1200, 2400),(1200, 2400),(1200, 2400),(1200, 2400),(1200, 2400),(1200, 2400)]

packer = newPacker()

# Add the rectangles to packing queue
for r in rectangles:
	packer.add_rect(*r)

# Add the bins where the rectangles will be placed
for b in bins:
	packer.add_bin(*b)

# Start packing
packer.pack()


# Full rectangle list
all_rects = packer.rect_list()
for rect in all_rects:
	b, x, y, w, h, rid = rect
	print("Bin index: {bin}, User asigned rectangle id or None: {rid}".format(bin=b, rid=rid))
	print("Rectangle bottom-left corner x coordinate: {x}, Rectangle bottom-left corner y coordinate: {y}, Rectangle width: {w}, Rectangle height: {h}".format(x=x,y=y,w=w,h=h))

# b - Bin index
# x - Rectangle bottom-left corner x coordinate
# y - Rectangle bottom-left corner y coordinate
# w - Rectangle width
# h - Rectangle height
# rid - User asigned rectangle id or None

im = Image.new('RGB', (500, 300), (128, 128, 128))
draw = ImageDraw.Draw(im)

draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)

# im.show()