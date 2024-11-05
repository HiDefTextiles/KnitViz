import argparse
import os
from knitviz.utils import load_json
from knitviz.pattern_parser import process_pattern

def main():
    parser = argparse.ArgumentParser(description="Parse and visualize a knitting pattern.")
    parser.add_argument('--mapping', default='data/stitch_mapping.json', help="Path to the JSON stitch mapping file")
    parser.add_argument('--pattern', default='data/devil_helmet.json', help="Path to the JSON knitting pattern file")
    parser.add_argument('--output_dir', default='figures', help="Directory to save output images")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    stitch_mapping = load_json(args.mapping)
    pattern_data = load_json(args.pattern)

    for part_name in pattern_data['parts']:
        part_data = pattern_data[part_name]
        name = os.path.splitext(os.path.basename(args.pattern))[0] + "_" + part_name
        process_pattern(stitch_mapping, name, part_data, args.output_dir)

if __name__ == "__main__":
    main()
