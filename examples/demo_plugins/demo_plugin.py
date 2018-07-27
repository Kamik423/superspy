#!/usr/bin/env python3
"""Demo plugin implementing some Monty Python jokes.
"""

from superspy import ast, language


@language.register_function('joke', 0)
class Joke(ast.Function):
    """The funniest joke in the world.
    This morning, shortly after eleven o'clock, comedy struck this little
    house in Dibley Road. Sudden ...violent ... comedy. Police have sealed off
    the area, and Scotland Yard's crack inspector is with me now.

    Attributes:
        funniest_joke_in_the_world (str): The funniest joke in the world.
    """

    funniest_joke_in_the_world = 'Wenn ist das Nunstück git und Slotermeyer? '\
        'Ja! Beiherhund das Oder die Flipperwaldt gersput!'
    def execute(self):
        """Print the funniest joke in the world. Exercise caution.
        """
        print(self.funniest_joke_in_the_world)


@language.register_function('spam')
class Spam(ast.Function):
    """Spam a few times.
    """

    def execute(self):
        """Spam a specified amount of times.
        """

        for _ in range(int(self.argument.execute())):
            print('SPAM')
