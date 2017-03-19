from acid.commands import BaseCommand
from acid.nvim import get_acid_ns


class Command(BaseCommand):

    name = 'FormatCode'
    priority = 0
    cmd_name = 'AcidFormatCode'
    handlers = ['MetaRepl']
    mapping = 'cfc'
    shorthand = '''normal! mx$?^("sy%`x'''
    opfunc = True
    nargs='*'
    op = "format-code"

    def prepare_payload(self, *args):
        return {'code': " ".join(args), }
