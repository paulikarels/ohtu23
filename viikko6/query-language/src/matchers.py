class Matcher:
    def __init__(self, *matchers):
        self._matchers = matchers
        
    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True
class All:
    def __init__(self, matcher):
        self.matcher = matcher

    def test(self, player):
        return True

class Not:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return False

        return True

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class PlaysIn:
    def __init__(self, team, matcher):
        self._team = team
        self.matcher = matcher

    def test(self, player):
        if not self.matcher.test(player):
            return False
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr, matcher):
        self._value = value
        self._attr = attr
        self.matcher = matcher

    def test(self, player):
        player_value = getattr(player, self._attr)

        if not self.matcher.test(player):
            return False
        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr, matcher):
        self._value = value
        self._attr = attr
        self.matcher = matcher

    def test(self, player):
        player_value = getattr(player, self._attr)

        if not self.matcher.test(player):
            return False
        return player_value < self._value
    
class Or:
    def __init__(self, *matchers, matcher):
        self.matcher = matcher
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if (matcher.test(player)):
                return True

        return False