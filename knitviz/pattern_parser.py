from .sanity_check import sanity_check
from .renderer import render_pattern_image


def display_instructions(instructions, stitch_counts, repeat_factor, incoming_stitches):
    action_line = "Action    stitches   " + "   ".join(
        f"{instr:>5}" for instr in instructions) + "    Repeat"
    print(action_line)

    count_line = "Count     " + f"({incoming_stitches:>6})   " + "   ".join(
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

        stitch_counts, repeat_factor = size_data["rows"]
        incoming_stitches, _ = sanity_check(instructions, stitch_counts, repeat_factor > 1,
                                            stitches_on_needle, stitch_mapping)

        # Display in console
        display_instructions(instructions, stitch_counts, repeat_factor, incoming_stitches)

        # Render image
        pattern = [
            [instr for instr, count in zip(instructions, stitch_counts) for _ in range(count)]
            for _ in range(repeat_factor)
        ]
        render_pattern_image(f"{name}_{size_name}", pattern, output_dir, stitches_on_needle)
