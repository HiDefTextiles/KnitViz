from PIL import Image, ImageDraw
import os


def load_png_image(png_path):
    assert os.path.exists(png_path), f"PNG file {png_path} not found."
    return Image.open(png_path)


def render_pattern_image(name, pattern, output_dir, number_of_stitches):
    png_dir = 'png'  # Directory containing pre-generated PNG files
    empty_path = os.path.join(png_dir, "none.png")  # Path to baseline empty cell
    empty_cell = load_png_image(empty_path)
    gridsize = empty_cell.size[0]  # Assume square grid cells

    # Calculate canvas dimensions based on pattern structure
    width = gridsize * number_of_stitches
    height = gridsize * len(pattern)  # Height is based on the number of rows
    img = Image.new("RGBA", (width, height), (255, 255, 255, 0))

    # Loop through each row in the pattern
    for row_idx, row in enumerate(pattern):
        y = row_idx * gridsize  # Vertical position for each row
        x = 0
        for col_idx, instr in enumerate(row):
            png_path = os.path.join(png_dir, f"{instr}.png")
            instr_image = load_png_image(png_path) or empty_cell

            # Paste the image at the calculated position
            img.paste(instr_image, (x, y), instr_image.convert("RGBA"))

            # Update the horizontal position for the next cell
            x += instr_image.size[0]

    # Draw red helper lines every 10 columns
    draw = ImageDraw.Draw(img)
    for col in range(10, len(pattern[0]), 10):
        x = col * gridsize
        draw.line([(x, 0), (x, height)], fill="red", width=1)

    # Save the final image
    output_path = os.path.join(output_dir, f"{name}.png")
    img.save(output_path)
    print(f"Image saved to {output_path}")
