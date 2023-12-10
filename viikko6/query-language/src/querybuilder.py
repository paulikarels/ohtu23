from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, All, Or, Matcher

class QueryBuilder:
    def __init__(self, matcher = Matcher()):
        self.matcher = matcher

    def all(self):
        return QueryBuilder(All(self.matcher))

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team, self.matcher))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(value, attr, self.matcher))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(value, attr, self.matcher))

    def build(self):
        return self.matcher