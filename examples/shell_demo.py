#! /usr/bin/env python3
"""Demonstration of an interactive shell.
"""

import sys

from superspy import ast, code_source, language


def main() -> int:
    """Main function.

    Returns:
        int: Exit code
    """

    lang = language.SuperSpyLanguage()
    source = code_source.ShellSource()
    my_ast = ast.Ast(source, lang)
    my_ast.error_mode = ast.ErrorMode.PRINT
    return my_ast.complete_run(run_after_each_line=True)


if __name__ == '__main__':
    EXIT_CODE = main()
    sys.exit(EXIT_CODE)
