import sys
from PIL import Image, ImageDraw, ImageFont

def render_text_to_image(input_file, output_file, bg_color="#1e1e1e", fg_color="#d4d4d4", font_size=16):
    try:
        with open(input_file, "r") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {input_file}: {e}")
        return

    # Basic logic to determine size
    max_line_length = max([len(line) for line in lines] + [1])
    width = max_line_length * (font_size // 2 + 3) + 40
    height = len(lines) * (font_size + 4) + 40

    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    try:
        # Try a monospaced font
        font = ImageFont.truetype("DejaVuSansMono.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    y_text = 20
    for line in lines:
        line = line.rstrip() # remove trailing newline
        draw.text((20, y_text), line, font=font, fill=fg_color)
        y_text += font_size + 4

    img.save(output_file)
    print(f"Saved {output_file}")

if __name__ == "__main__":
    render_text_to_image("hasil/kuis3.py", "hasil/sc_code.png", font_size=14)
    render_text_to_image("hasil/output.txt", "hasil/sc_output.png", font_size=16, fg_color="#a6e22e")
