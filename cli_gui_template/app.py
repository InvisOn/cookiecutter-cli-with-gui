"""
Template for a CLI with optional GUI.
"""
from user_interface import spawn_cli, spawn_gui

def main():
    args = spawn_cli()
    if args['graphical_user_interface']:
        args = spawn_gui()
