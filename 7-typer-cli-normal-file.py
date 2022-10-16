# typer 7-typer-cli-normal-file.py run --name ali
def main(name: str = "World"):
    """
    Say hi to someone, by default to the World.
    """
    print(f"Hello {name}")
