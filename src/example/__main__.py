import os

import click


def config_logging():
    return


@click.command()
@click.option(
    "--env",
    type=click.Choice(["local", "dev", "prd"], case_sensitive=False),
    default="local",
)
@click.option(
    "--debug",
    type=click.BOOL,
    is_flag=True,
    default=False,
)
def main(env: str, debug: bool):
    os.environ["ENV"] = env
    os.environ["DEBUG"] = str(debug)
    print(f"hello world {env}, {debug}")


if __name__ == "__main__":
    main()
