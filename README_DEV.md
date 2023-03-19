# Notes for Developers

These are notes to remind me how to do things on this project.

## Installation

pip install -e ".[dev]"

## Building

mdinfo-exiftool uses [doit](https://pydoit.org/) for building.

To build the project, run:

    `doit`

## Testing

mdinfo-exiftool uses [pytest](https://docs.pytest.org/en/stable/) for testing.
The test suite can be run with the following command:

    `pytest`

or

    `doit test`

## README update

The README.md is updated automatically using [cogapp](https://nedbatchelder.com/code/cog/).
The README.md will be updated when running `doit`.
