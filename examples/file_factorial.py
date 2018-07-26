#! /usr/bin/env python3
"""Demonstration of running a script from file.
"""

import os
import sys

from superspy import ast, code_source, language


def main() -> int:
    """Main function.

    Returns:
        int: Exit code
    """

    lang = language.SuperSpyLanguage()
    example_folder = os.path.dirname(sys.argv[0])
    source = code_source.FileSource(f'{example_folder}/factorial_script.spy')
    my_ast = ast.Ast(source, lang)
    return my_ast.complete_run()

    # # In "one line":
    #
    # ast.Ast(
    #     code_source.FileSource(
    #         f'{os.path.dirname(sys.argv[0])}/factorial_script.spy'),
    #     language.SuperSpyLanguage()
    # ).complete_run()


if __name__ == '__main__':
    EXIT_CODE = main()
    sys.exit(EXIT_CODE)
