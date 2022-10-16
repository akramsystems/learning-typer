"""
There's actually a very small distinction in Python between "parameter" and "argument".

It's quite technical... and somewhat pedantic.

Parameter refers to the variable name in a function declaration. Like:

def bring_person(name: str, lastname: str = ""):
    pass

Argument refers to the value passed when calling a function. Like:

person = bring_person("Camila", lastname="Gutiérrez")

...but you will probably see them used interchangeably in most of the places (including here).
"""
import typer

# If you add a docstring to your function it will be used in the help text:
# python 5-add-cli-documentation.py --lastname Gutiérrez Camila
def main(name: str, lastname: str = "", formal: bool = False):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """
    if formal:
        print(f"Good day Mr. {name} {lastname}.")
    else:
        print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
