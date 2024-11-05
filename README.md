# KnitViz

**KnitViz** is a Python-based visualization tool for interpreting knitting patterns from JSON
format and presenting them as graphical stitch maps. This project is part of the _HiDef Textiles_
initiative, a research project led by Dr. Helga Ingimundardóttir, Assistant Professor in
Industrial Engineering at the University of Iceland. _HiDef Textiles_ explores the intersections
between textiles, data visualization, and computational design.

## Features

- **Pattern Parsing**: Reads and interprets knitting patterns in JSON format.
- **Stitch Visualization**: Generates graphical representations of stitch sequences using ggplot2.
- **Size Customization**: Easily adjust visualizations for different sizes.
- **Flexible Pattern Representation**: Handles complex patterns, including increases, decreases, and
  special stitch types.

## Getting Started

### Prerequisites

- **Python** (version 3.6 or higher)
- **Pillow** and **CairoSVG** packages for image processing and SVG handling

### Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/HiDefTextiles/KnitViz.git
   cd KnitViz
   ```
2. **Install required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Preprocess SVG Files**: Convert SVG files for each stitch type to PNG format using the
   preprocessing script:
   ```bash
   python code/preprocess_svg.py
   ```

### Usage

1. **Add Your JSON Pattern File**:
   Place your JSON knitting pattern file in the `data/` directory (
   e.g., [data/devil_helmet.json](data/devil_helmet.json)).
2. **Run the visualization script**: Generate the pattern visualization using the following command:
   ```bash   
   python main.py --pattern data/devil_helmet.json
   ```
   This will produce PNG images for each pattern part and size, saved in the `figures/` directory.

3. **View and Adjust Output**: The resulting images can be opened and reviewed in any image viewer.
   Helper lines and custom styling adjustments are available within `render_pattern_image` in
   [KnitViz/renderer.py](renderer.py).

### Contributing

We welcome contributions! To propose enhancements or report issues, please use
the [Issues](../../issues/) tab. Suggestions on supporting additional pattern formats or
visualizations are especially appreciated.

## License

This work is licensed under
a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](LICENSE).

You are free to:

- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

Under the following terms:

- **Attribution**  — You must give appropriate credit, provide a link to the license, and indicate
  if changes were made. Attribution should be made to the HiDef Textiles initiative led by Dr. Helga
  Ingimundardóttir at the University of Iceland.
- **NonCommercial** — You may not use the material for commercial purposes.
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your
  contributions under the same license as the original.

For further information, see
the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
