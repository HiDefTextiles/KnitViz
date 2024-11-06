def sanity_check(instructions, stitch_counts, repeated, stitches_on_needle, stitch_mapping):
    assert len(instructions) == len(
        stitch_counts), "Mismatch between instructions and stitch counts"

    incoming_stitches = sum(
        stitch_mapping[instr]['in'] * count for instr, count in zip(instructions, stitch_counts))
    outgoing_stitches = sum(
        stitch_mapping[instr]['out'] * count for instr, count in zip(instructions, stitch_counts))

    assert incoming_stitches == stitches_on_needle, (
        f"Mismatch between incoming stitches {incoming_stitches} and "
        f"stitches on needle {stitches_on_needle}")
    if repeated:
        assert incoming_stitches == outgoing_stitches, "When repeating pattern rows, incoming and outgoing stitch counts must align"

    return incoming_stitches, outgoing_stitches
