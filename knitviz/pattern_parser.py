from .sanity_check import sanity_check
from .renderer import render_pattern_image


def display_instructions_header(instructions):
    def format_instruction(instr):
        # If the instruction is a list, recursively format each item
        if isinstance(instr, list):
            # Format each sub-item in the list, then join them with ", "
            return f"({','.join(format_instruction(sub_instr) for sub_instr in instr)})"
        else:
            # If the instruction is a string (not a list), return it as is
            return instr

    instructions = [format_instruction(instr) for instr in instructions]

    # Build the row with dynamic spacing
    row_data = ['Row', 'stitches', 'RS'] + [ inst.rjust(3) for inst in instructions] + ['Repeat']
    spaces = [len(col) for col in row_data]

    # Join and print the formatted row
    action_line = " ".join(row_data)
    print(action_line)

    return spaces


def display_instructions_row(row_number, stitch_counts, repeat_factor, incoming_stitches, side,
                             spaces):
    # Build the row with dynamic spacing based on 'spaces'
    row_data = [row_number, f"({incoming_stitches})", 'RS' if side else 'WS'] + stitch_counts + [
        f"{repeat_factor}x"]
    assert len(spaces) == len(row_data), "Mismatch between spaces and row data"
    row_data = [f"{col:>{spaces[i]}}" for i, col in enumerate(row_data)]

    # Join and print the formatted row
    count_line = " ".join(row_data)
    print(count_line)


def print_to_console(name, pattern, instructions, stitch_mapping):
    # find the indices of the instructions that are not "none"
    indices = [i for i, instr in enumerate(instructions) if instr != "none"]
    # filter out the instructions that are none
    instructions = [instructions[i] for i in indices]

    print("-" * 50)
    print(f"Pattern for {name}:")
    spaces = display_instructions_header(instructions)
    row_number = 1
    stitches_on_needle, max_stitches = 0, 0
    for (stitch_counts, repeat_factor, side) in pattern["rows"]:
        stitch_counts = [stitch_counts[i] for i in indices]  # Skip the "none" instructions
        incoming_stitches, outgoing_stitches = sanity_check(
            instructions, stitch_counts, repeat_factor > 1, stitches_on_needle, stitch_mapping)
        stitches_on_needle = outgoing_stitches

        if incoming_stitches > max_stitches:
            max_stitches = incoming_stitches

        # Display in console
        display_instructions_row(row_number, stitch_counts, repeat_factor, incoming_stitches,
                                 side, spaces)
        row_number += repeat_factor
    return max_stitches


def process_pattern(stitch_mapping, name, part_data, output_dir):
    instructions = part_data["instructions"]
    sizes = part_data["sizes"]

    for size_name, size_data in sizes.items():
        max_stitches = print_to_console(f"{name}_{size_name}", size_data, instructions,
                                        stitch_mapping)

        pattern = []
        for (stitch_counts, repeat_factor, side) in size_data["rows"]:
            # Keep track of the pattern for rendering
            for _ in range(repeat_factor):
                row = [instr for instr, count in zip(instructions, stitch_counts)
                       for _ in range(count)]
                pattern.append((row, side))

        # Render the pattern to an image
        render_pattern_image(f"{name}_{size_name}", pattern, output_dir, max_stitches,
                             stitch_mapping)
