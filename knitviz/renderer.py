from PIL import Image, ImageDraw
import os


def load_png_image(png_path):
    assert os.path.exists(png_path), f"PNG file {png_path} not found."
    return Image.open(png_path)


def render_pattern_image(name, pattern, output_dir, number_of_stitches, stitch_mapping, alignment):
    assert alignment in ["left", "center", "right"], "Alignment must be left, right or center"
    png_dir = 'png'  # Directory containing pre-generated PNG files
    empty_path = os.path.join(png_dir, "none.png")  # Path to baseline empty cell
    empty_cell = load_png_image(empty_path)
    gridsize = empty_cell.size[0]  # Assume square grid cells

    # Calculate canvas dimensions based on pattern structure
    width = gridsize * number_of_stitches
    height = gridsize * len(pattern)  # Height is based on the number of rows
    img = Image.new("RGBA", (width, height), (255, 255, 255, 0))

    # Loop through each row in the pattern
    for row_idx, (row, side) in enumerate(reversed(pattern)):
        y = row_idx * gridsize  # Vertical position for each row
        x = 0
        remaining_stitches = number_of_stitches - len(row)

        # Make sure that the row is reversed if it's for the WS (i.e. side=False)
        row = row if side else list(reversed(row))

        if remaining_stitches < 0:
            raise ValueError(f"Row {row_idx} has {remaining_stitches} more stitches than expected")
        elif remaining_stitches > 0:
            # append empty cells to the row based on alignment
            if alignment == "right":
                left_padding = remaining_stitches
                right_padding = 0
            elif alignment == "left":
                left_padding = 0
                right_padding = remaining_stitches
            else: # center
                left_padding = remaining_stitches // 2
                right_padding = remaining_stitches - left_padding
            row = ["none"] * left_padding + row + ["none"] * right_padding

        for col_idx, instr in enumerate(row):
            RS_stitch = instr if side else stitch_mapping[instr]['WS']
            png_path = os.path.join(png_dir, f"{RS_stitch}.png")
            instr_image = load_png_image(png_path)

            # Paste the image at the calculated position
            img.paste(instr_image, (x, y), instr_image.convert("RGBA"))

            # Update the horizontal position for the next cell
            x += instr_image.size[0]

    # Draw red helper lines every 10 columns
    draw = ImageDraw.Draw(img)
    for col in range(10, len(pattern[0][0]), 10):
        x = col * gridsize
        draw.line([(x, 0), (x, height)], fill="red", width=1)

    # Save the final image
    output_path = os.path.join(output_dir, f"{name}.png")
    img.save(output_path)
    print(f"Image saved to {output_path}")
