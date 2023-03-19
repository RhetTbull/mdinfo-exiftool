"""Task list for doit, used to build the project; run with `doit` or `doit list` to see commands"""


def task_update_readme():
    """Update README with CLI output"""
    return {"actions": ["cog -r README.md"]}


def task_convert_readme():
    """Convert README.md to README.rst because I can't #@%^ figure out how to get build to use markdown from pyproject.toml"""
    return {"actions": ["m2r2 --overwrite README.md"]}


def task_test():
    """Run tests"""
    return {"actions": ["pytest"]}


# def task_docs():
#     """Build docs"""
#     return {"actions": ["poetry run mkdocs build"]}


# def task_gh_docs():
#     """Build docs and push to gh-pages"""
#     return {
#         "actions": [
#             "poetry run mkdocs gh-deploy --force",
#         ]
#     }


def task_clean_build_files():
    """Clean out old build files"""
    return {
        "actions": ["rm -rf dist/", "rm -rf build/"],
    }


def task_build():
    """Build python project"""
    return {"actions": ["python3 -m build"]}
