"""Generate README.md help"""

from __future__ import annotations

from textwrap import dedent

from .mdinfo_exiftool import get_template_help


def format_markdown_table(data: list[list[str] | tuple[str]], width=None) -> str:
    """Convert an list of lists or tuples into a markdown table. The first row is the header row."""

    # Calculate the maximum length of data in each column
    column_lengths = [
        max(len(str(row[i])) for row in data) for i in range(len(data[0]))
    ]

    # If a width is provided, adjust the column widths to fit within the width
    if width is not None:
        total_width = sum(column_lengths) + (len(data[0]) + 1) * 3
        if total_width > width:
            column_width_ratio = width / total_width
            column_lengths = [
                int(length * column_width_ratio) for length in column_lengths
            ]

    # Create the markdown table header row
    header = (
        "| "
        + " | ".join([str(data[0][col]).ljust(column_lengths[col]) for col in range(len(data[0]))])
        + " |\n"
    )

    # Create the markdown table separator row
    separator = (
        "| "
        + " | ".join(["-" * column_lengths[i] for i in range(len(data[0]))])
        + " |\n"
    )

    rows = "".join(
        (
            "| "
            + " | ".join(
                [str(row[i]).ljust(column_lengths[i]) for i in range(len(row))]
            )
            + " |\n"
        )
        for row in data[1:]
    )

    # Return the full formatted markdown table
    return header + separator + rows


def get_markdown_help():
    """Generate help text for this template as markdown"""
    help = ""
    for help_item in get_template_help():
        # items from get_template_help are either markdown strings or lists of lists
        if type(help_item) is str:
            help += dedent(help_item)
            help += "\n"
        elif isinstance(help_item, (tuple, list)):
            help += format_markdown_table(help_item, width=78)
            help += "\n"
    return help
