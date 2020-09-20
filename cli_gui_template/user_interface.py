from gooey import GooeyParser, Gooey


def cli() -> GooeyParser:
    """Creates the CLI parser without the -gui argument.

    Returns:
        GooeyParser:
    """
    parser = GooeyParser(description='A template CLI app with optional GUI.')

    return parser


def add_gui_arg(parser: GooeyParser) -> GooeyParser:
    """Adds -gui argument to a GooeyParser.

    Args:
        parser (GooeyParser):

    Returns:
        GooeyParser:
    """
    parser.add_argument('-gui', '--graphical-user-interface',
                        help='Spawn a GUI.',
                        action='store_true')

    return parser


def spawn_cli() -> GooeyParser:
    """Spawns the full command line interface (with -gui argument).

    Returns:
        GooeyParser:
    """
    parser = add_gui_arg(cli())

    return vars(parser.parse_args())


@Gooey(program_name='Template')
def spawn_gui():
    """Spawn a GUI based on the CLI without -gui argument.
    """
    # -gui argument is not needed because the gui has already been spawned.
    return cli().parse_args()
