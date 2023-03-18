# mdinfo

Meta Data Info (mdinfo) is a command line tool for printing metadata information about files.

It is designed to be a simple, fast, and flexible tool for extracting metadata of all types from files
using a rich templating system. It is written in Python and can be used both as a package for your own
Python projects or as a command line tool. mdinfo includes a plugin system for adding support for
other types of metadata or different file formats.

The mdinfo command line tool can output selected metadata in CSV and JSON format.

Currently tested on Linux and macOS.
## Synopsis


## Command Line Usage

<!-- [[[cog
import cog
from mdinfo.cli import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli, ["--help"])
help = result.output.replace("Usage: cli", "Usage: mdinfo")
cog.out(
    "```\n{}\n```".format(help)
)
]]] -->

<!-- [[[end]]] -->