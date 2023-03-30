from PIL import Image

# Load the original square picture (has to be named pic.png)
# Make sure the picture is square or this will fail!
img = Image.open('pic.png')

# Get the dimensions of the original picture
width, height = img.size

# Calculate the size of the new square pictures
quarter_size = int(width / 2)

# Split the original picture into four square pictures
top_left = img.crop((0, 0, quarter_size, quarter_size))
top_right = img.crop((quarter_size, 0, width, quarter_size))
bottom_left = img.crop((0, quarter_size, quarter_size, height))
bottom_right = img.crop((quarter_size, quarter_size, width, height))

# Save the new square pictures
top_left.save('top_left.png')
top_right.save('top_right.png')
bottom_left.save('bottom_left.png')
bottom_right.save('bottom_right.png')