from PIL import Image, ImageDraw, ImageFont
import textwrap

# Function to create a text image
def text_to_image(text, font_path=None, font_size=40, text_color=(0, 0, 0), bg_color=(255, 255, 255)):
    # Define font
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()
    
    # Define image size based on text length
    lines = textwrap.wrap(text, width=40)
    max_line_length = max([len(line) for line in lines])
    img_width = font_size * max_line_length // 2
    img_height = font_size * (len(lines) + 1)
    
    # Create image with background color
    image = Image.new("RGB", (img_width, img_height), color=bg_color)
    draw = ImageDraw.Draw(image)
    
    # Position text
    y_text = 10
    for line in lines:
        draw.text((10, y_text), line, font=font, fill=text_color)
        y_text += font_size

    return image

# Get user input for the text and create an image
user_text = input("Enter the text to convert into an image: ")

# Set customizations
font_path = None  # Path to a .ttf font file (leave as None for default font)
font_size = 30
text_color = (0, 0, 0)  # Black text
bg_color = (255, 255, 255)  # White background

# Generate the image
img = text_to_image(user_text, font_path=font_path, font_size=font_size, text_color=text_color, bg_color=bg_color)

# Save or display the image
img.show()       # Display the image
img.save("text_image.png")  # Save the image as PNG
