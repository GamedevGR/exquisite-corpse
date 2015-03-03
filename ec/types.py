"""Game configuration types."""

import yorm


@yorm.map_attr(mac=yorm.standard.String)
@yorm.map_attr(win=yorm.standard.String)
@yorm.map_attr(nix=yorm.standard.String)
class Instructions(yorm.extended.AttributeDictionary):

    """Collection of OS-specific shell commands."""

    def __init__(self, mac, win, nix):
        super().__init__()
        self.mac = mac
        self.win = win
        self.nix = nix


@yorm.map_attr(url=yorm.standard.String)
@yorm.map_attr(rev=yorm.standard.String)
@yorm.map_attr(build=Instructions)
@yorm.map_attr(run=Instructions)
class Game(yorm.extended.AttributeDictionary):

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


@yorm.map_attr(all=Game)
class Games(yorm.container.List):

    """List of games."""


@yorm.map_attr(games=Games)
@yorm.store_instances("{self.path}")
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
