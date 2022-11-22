import click

from pki_a22_app.haarcascades.haarcascades import show


@click.group()
def pki_a22_app():
    pass

@pki_a22_app.command()
@click.option('--name', help='Name of person to greet')
def run(name):
    run_app(name)

def main(name):
    run_app(name)

def run_app(name):
    print(f"Hello {name}!")
    show()

if __name__ == '__main__':
    main("Bob")
