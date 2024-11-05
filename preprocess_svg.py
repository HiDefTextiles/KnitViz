import os
import cairosvg

def convert_svg_to_png(svg_dir='svg', png_dir='png', scale=0.5):
    # Ensure the output directory exists
    os.makedirs(png_dir, exist_ok=True)

    # Convert each SVG file in the svg directory to PNG
    for svg_filename in os.listdir(svg_dir):
        if svg_filename.endswith('.svg'):
            svg_path = os.path.join(svg_dir, svg_filename)
            png_filename = svg_filename.replace('.svg', '.png')
            png_path = os.path.join(png_dir, png_filename)

            # Convert SVG to PNG
            cairosvg.svg2png(url=svg_path, write_to=png_path, scale=scale)
            print(f"Converted {svg_filename} to {png_filename}")

if __name__ == "__main__":
    convert_svg_to_png()
