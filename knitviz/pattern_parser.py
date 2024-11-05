from .sanity_check import sanity_check
from .renderer import render_pattern_image

def display_instructions_header(instructions):
    action_line = "Row    stitches   " + "   ".join(
        f"{instr:>5}" for instr in instructions) + "    Repeat"
    print(action_line)

def display_instructions_row(row_number, stitch_counts, repeat_factor, incoming_stitches):
    count_line = f"{row_number:>3}    ({incoming_stitches:>6})   " + "   ".join(
        f"{count:>5}" for count in stitch_counts) + f"{repeat_factor:>9}x"
    print(count_line)


def process_pattern(stitch_mapping, name, part_data, output_dir):
    instructions = part_data["instructions"]
    sizes = part_data["sizes"]

    for size_name, size_data in sizes.items():
        print("-" * 50)
        print(f"Pattern for {name} - {size_name}:")

        stitches_on_needle = size_data['cast_on']
        print(f"Cast on {stitches_on_needle} stitches")
        max_stitches = stitches_on_needle

        pattern = []
        display_instructions_header(instructions)
        row_number = 1
        for (stitch_counts, repeat_factor) in size_data["rows"]:
            incoming_stitches, outgoing_stitches = sanity_check(instructions, stitch_counts,
                                                                repeat_factor > 1,
                                                                stitches_on_needle, stitch_mapping)
            stitches_on_needle = outgoing_stitches

            if incoming_stitches > max_stitches:
                max_stitches = incoming_stitches

            # Display in console
            display_instructions_row(row_number, stitch_counts, repeat_factor, incoming_stitches)
            row_number += repeat_factor

            # Keep track of the pattern for rendering
            for _ in range(repeat_factor):
                row = [instr for instr, count in zip(instructions, stitch_counts)
                       for _ in range(count)]
                pattern.append(row)

        # Render the pattern to an image
        render_pattern_image(f"{name}_{size_name}", pattern, output_dir, max_stitches)
