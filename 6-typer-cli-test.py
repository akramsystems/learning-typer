from typing import Optional

import typer

app = typer.Typer()

# typer 6-typer-cli.py run hello --name Camila


@app.command()
def hello(name: Optional[str] = None):
    if name:
        typer.echo(f"Hello {name}")
    else:
        typer.echo("Hello World!")

# typer 6-typer-cli.py run bye --name Camila


@app.command()
def bye(name: Optional[str] = None):
    if name:
        typer.echo(f"Bye {name}")
    else:
        typer.echo("Goodbye!")
