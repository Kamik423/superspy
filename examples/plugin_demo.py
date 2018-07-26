#! /usr/bin/env python3
"""Demonstration of plugin usage.
"""

import sys

from superspy import ast, code_source, language


def main() -> int:
    """Main function.

    Returns:
        int: Exit code
    """

    lang = language.SuperSpyLanguage(['demo_plugins'])
    source = code_source.ShellSource()
    source.prompt = '[SUPERSPY DEMO] >>> '
    my_ast = ast.Ast(source, lang)
    my_ast.error_mode = ast.ErrorMode.PRINT
    print('You can in addition to the usual commands use `spam <amount>`'
          'and `joke`.\n'
          'These can be integrated into normal script and flow control'
          'like loops.')
    return my_ast.complete_run(run_after_each_line=True)


if __name__ == '__main__':
    EXIT_CODE = main()
    sys.exit(EXIT_CODE)
