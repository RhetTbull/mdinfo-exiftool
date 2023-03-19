"""Test the mdinfo_exiftool plugin"""

import os

import pytest
from click.testing import CliRunner
from mdinfo.cli import cli

TEST_FILE = "tests/test_files/pears.jpg"

TEST_DATA = {
    "{exiftool:Keywords|sort}": ["fruit pears"],
    "{exiftool:XMP:Title}": ["Pears on a tree"],
}


@pytest.mark.parametrize("template,expected", TEST_DATA.items())
def test_exiftool_1(template, expected):
    """Test exiftool template"""
    cwd = os.getcwd()
    with CliRunner().isolated_filesystem():
        result = CliRunner().invoke(
            cli, ["--no-filename", "-p", template, os.path.join(cwd, TEST_FILE)]
        )
        assert result.exit_code == 0
        assert result.output.strip() == ", ".join(expected)
