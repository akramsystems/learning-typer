import typer

# can pass cli options without a name
# python 4-add-cli-option-with-value.py Camila
# python 4-add-cli-option-with-value.py Camila --lastname Gutiérrez
# python 4-add-cli-option-with-value.py --lastname Gutiérrez Camila
def main(name: str, lastname: str = "", formal: bool = False):
    if formal:
        print(f"Good day Mr. {name} {lastname}.")
    else:
        print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
