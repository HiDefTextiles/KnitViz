# KnitViz
**KnitViz** is a visualization tool for interpreting knitting patterns from JSON format and presenting them as graphical stitch maps using ggplot2 in R. This project is part of the **HiDef Textiles** initiative, a research project led by Dr. Helga Ingimundardóttir, Assistant Professor in Industrial Engineering at the University of Iceland. HiDef Textiles explores the intersections between textiles, data visualization, and computational design.

## Features
- **Pattern Parsing**: Reads and interprets knitting patterns in JSON format.
- **Stitch Visualization**: Generates graphical representations of stitch sequences using ggplot2.
- **Size Customization**: Easily adjust visualizations for different sizes.
- **Flexible Pattern Representation**: Handles complex patterns, including increases, decreases, and special stitch types.

## Getting Started

### Prerequisites
- **R** (version 4.0 or higher)
- **ggplot2** package

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/HiDefTextiles/KnitViz.git
   ```
2. Install the ggplot2 package in R:
   ```R
   install.packages('ggplot2')
   ```

### Usage
1. Load your JSON knitting pattern file into R.
2. Run the visualization script:
   ```R
   source("code/visualize_pattern.R")
   ```
3. View and adjust the ggplot output as needed for your pattern visualization.

### Contributing
We welcome contributions! To propose enhancements or report issues, please use the [Issues](../../issues/) tab. Suggestions on supporting additional pattern formats or visualizations are especially appreciated.

## License
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](LICENSE).

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

Under the following terms:

- **Attribution**  — You must give appropriate credit, provide a link to the license, and indicate if changes were made. Attribution should be made to the HiDef Textiles initiative led by Dr. Helga Ingimundardóttir at the University of Iceland.
- **NonCommercial** — You may not use the material for commercial purposes.
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

For further information, see the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
