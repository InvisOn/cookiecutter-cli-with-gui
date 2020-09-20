from gooey import GooeyParser, Gooey

def spawn_cli():
    parser = Gooey.ArgumentParser(description='A template CLI app with optional GUI.')
    parser.add_argument('-gui', '--graphical-user-interface',
                        help='Spawn a GUI.',
                        action='store_true')

    return vars(parser.parse_args())


def spawn_gui():
    """Spawn a GUI based on the CLI.

    Args:
        gui (bool): [description]
    """
    Gooey(spawn_cli)()
