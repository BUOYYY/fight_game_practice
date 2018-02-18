import argparse


class CLIParse(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Initialize the \
            Players and the stage.")
        self._add_args(self)

    def _add_args(self):
        self.parser.add_argument(
            '-p', '--players', nargs='+', help='<Required> \
            Must pass at least 2 args to the --players flag.',
            required=True
        )
        self.parser.add_argument(
            '-s', '--stage', help='<Required> \
            Must pass a stage of Desert, Mountains, Forest, or Arctic',
            required=True
        )
