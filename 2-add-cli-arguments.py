import typer

# python 2-add-cli-arguments.py Camila Gutiérrez
def main(name: str, lastname: str):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)
