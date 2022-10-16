import typer

# python 3-add-cli-option.py Camila Gutiérrez
# python 3-add-cli-option.py Camila Gutiérrez --formal
def main(name: str, lastname: str, formal: bool = False):
    if formal:
        print(f"Good day Mr. {name} {lastname}.")
    else:
        print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
