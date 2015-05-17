"""Game configuration types."""

import yorm


@yorm.attr(mac=yorm.converters.String)
@yorm.attr(win=yorm.converters.String)
@yorm.attr(nix=yorm.converters.String)
class Instructions(yorm.converters.AttributeDictionary):

    """Collection of OS-specific shell commands."""

    def __init__(self, mac, win, nix):
        super().__init__()
        self.mac = mac
        self.win = win
        self.nix = nix


@yorm.attr(url=yorm.converters.String)
@yorm.attr(rev=yorm.converters.String)
@yorm.attr(build=Instructions)
@yorm.attr(run=Instructions)
class Game(yorm.converters.AttributeDictionary):

    """Game's clone, build, and run instructions."""

    def __init__(self, url, rev, build, run):
        super().__init__()
        self.url = url
        self.rev = rev
        self.build = build
        self.run = run

    def __repr__(self):
        return "<game {}>".format(self)

    def __str__(self):
        return "'{u}' @ {r}".format(u=self.url, r=self.rev)


@yorm.attr(all=Game)
class Games(yorm.converters.List):

    """List of games."""


@yorm.attr(games=Games)
@yorm.sync("{self.path}")
class Config:

    """Configuration file for games to run."""

    def __init__(self, path):
        super().__init__()
        self.path = path
        self.games = []

    def __repr__(self):
        return "<config {}>".format(self)

    def __str__(self):
        return "{p}".format(p=self.path)
