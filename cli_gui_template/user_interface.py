from gooey import GooeyParser, Gooey


def _cli() -> GooeyParser:
    """Creates the CLI parser without the -gui argument.

    Returns:
        GooeyParser:
    """
    parser = GooeyParser(description='A template CLI app with optional GUI.')

    return parser


def _add_gui_arg(parser: GooeyParser) -> GooeyParser:
    """Adds -gui argument to a GooeyParser.

    Args:
        parser (GooeyParser):

    Returns:
        GooeyParser:
    """
    parser.add_argument('-gui', '--graphical-user-interface',
                        help='Spawn a graphical user interface.',
                        action='store_true')

    return parser


def _spawn_cli() -> GooeyParser:
    """Spawns the full command line interface (with -gui argument).

    Returns:
        GooeyParser:
    """
    parser = _add_gui_arg(_cli())

    return vars(parser.parse_args())


@Gooey(program_name='Template')
def _spawn_gui() -> dict:
    """Spawn a GUI based on the CLI without -gui argument.

    Returns:
        dict:
    """
    # -gui argument is not needed because the gui has already been spawned.
    return _cli().parse_args()


def user_interface() -> dict:
    """Spawns the user interface based.

    Returns:
        dict: Arguments passed.
    """
    args = _spawn_cli()

    if args['graphical_user_interface']:
        args = _spawn_gui()

    return args