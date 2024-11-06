def sanity_check(instructions, stitch_counts, repeated, stitches_on_needle, stitch_mapping):
    assert len(instructions) == len(
        stitch_counts), "Mismatch between instructions and stitch counts"

    def calculate_stitches(instr, stitch_mapping):
        # Base case: if the instruction is a string, get its 'in' and 'out' values
        if not isinstance(instr, list):
            if instr in stitch_mapping:
                return stitch_mapping[instr]['in'], stitch_mapping[instr]['out']
            else:
                # check if the instruction is a K og P instruction followed by a number
                if instr[0] in ['K', 'P'] and instr[1:].isdigit():
                    repeat = int(instr[1:])
                    stitch = stitch_mapping[instr[0]]
                    return stitch['in'] * repeat, stitch['out'] * repeat
                else:
                    raise ValueError(f"Unknown stitch instruction {instr}")

        # Check for a list with two elements, where the second element is an integer (repeated instruction)
        if len(instr) == 2 and isinstance(instr[1], int):
            sub_in, sub_out = calculate_stitches(instr[0], stitch_mapping)
            total_in = sub_in * instr[1]
            total_out = sub_out * instr[1]
            return total_in, total_out

        # Recursive case: if the instruction is a list, calculate the sum of 'in' and 'out' for each nested item
        total_in, total_out = 0, 0
        for sub_instr in instr:
            sub_in, sub_out = calculate_stitches(sub_instr, stitch_mapping)
            total_in += sub_in
            total_out += sub_out
        return total_in, total_out

    # Initialize totals for incoming and outgoing stitches
    incoming_stitches = 0
    outgoing_stitches = 0

    # Loop through instructions and stitch_counts to accumulate incoming and outgoing stitches
    for instr, count in zip(instructions, stitch_counts):
        if count == 0:
            continue
        instr_in, instr_out = calculate_stitches(instr, stitch_mapping)
        incoming_stitches += instr_in * count
        outgoing_stitches += instr_out * count

    assert incoming_stitches == stitches_on_needle, (
        f"Mismatch between incoming stitches {incoming_stitches} and "
        f"stitches on needle {stitches_on_needle}")
    if repeated:
        assert incoming_stitches == outgoing_stitches, "When repeating pattern rows, incoming and outgoing stitch counts must align"

    return incoming_stitches, outgoing_stitches
