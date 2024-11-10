"""
Handle REZ Package repository from CLI
"""

from rez.command import Command
from rez.config import config

# This attribute is optional, default behavior will be applied if not present.
command_behavior = {
    "hidden": False,  # (bool): default False
    "arg_mode": None,  # (str): "passthrough", "grouped", default None
}


def setup_parser(parser, completions=False):
    parser.add_argument("action", choices=["add", "remove", "list"], default="list")
    parser.add_argument("folder", nargs="*")

def command(opts, parser=None, extra_arg_groups=None):
    from rez_repository.package_repository import PackageRepositoryHandler
    package_handler = PackageRepositoryHandler(config, opts.folder, opts.action)
    package_handler.run()

class RepositoryCommand(Command):
    @classmethod
    def name(cls):
        return "repository"


def register_plugin():
    return RepositoryCommand
