import argparse
from PIL import Image, ImageFont, ImageDraw

DESCRIPTION_STRING = "This script takes in a True Type Font and outputs a bitmap sprite sheet of of ASCII characters."

parser = argparse.ArgumentParser(prog = "ttf2bitmap", description = DESCRIPTION_STRING)
parser.add_argument("ttf_file", type = str)
parser.add_argument("--scale", default = 1, type = int)
parser.add_argument("--output", default = "sprite_sheet.png", type = str)
args = parser.parse_args()

font = ImageFont.truetype(args.ttf_file, args.scale)

# Loop through all the visible charactes and get the max width/height of the
# bounding box.
tile_width = 0
tile_height = 0
for char in range(32, 127):
    bbox = font.getbbox(chr(char))
    if bbox[2] > tile_width:
        tile_width = bbox[2]
    if bbox[3] > tile_height:
        tile_height = bbox[3]

sprite_sheet_width = (127-32) * tile_width

sprite_sheet = Image.new(mode = "RGBA", size = (sprite_sheet_width, tile_height))
draw = ImageDraw.Draw(sprite_sheet)

for char in range(32, 127):
    index = char - 32
    x_step = index * tile_width
    draw.text((x_step, 0), chr(char), font=font, fill = "BLACK")

sprite_sheet.save(args.output)

print("Tile size: %d x %d" % (tile_width, tile_height))


