from PIL import Image

def brightness_to_ascii(brightness):
    ascii_chars = "@%#*+=-:. "

    if brightness < 25:
        return ascii_chars[0]
    elif brightness < 50:
        return ascii_chars[1]
    elif brightness < 75:
        return ascii_chars[2]
    elif brightness < 100:
        return ascii_chars[3]
    elif brightness < 125:
        return ascii_chars[4]
    elif brightness < 150:
        return ascii_chars[5]
    elif brightness < 175:
        return ascii_chars[6]
    elif brightness < 200:
        return ascii_chars[7]
    elif brightness < 225:
        return ascii_chars[8]
    else:
        return ascii_chars[9]

def ascii_converter(image):
    img = Image.open(image)
    w, h = img.size
    img = img.resize((w // 6, h // 12))
    w, h = img.size
    img = img.convert("L")
    ascii_str = ""

    for y in range(h):
        for x in range(w):
            brightness = img.getpixel((x, y))
            ascii_str += brightness_to_ascii(brightness)
        ascii_str += "\n"

    with open("ascii_art.txt", "w") as f:
        f.write(ascii_str)

if __name__ == "__main__":
    ascii_converter("homer.png")