class Person:
    def __init__(self, name):
        self.name = name
        self.intrigue = .0  # How willing someone is to make relationships
        self.confidence = .0  # How willing someone is to actively talk to new people
        self.allure = .0  # How likely it is that someone would talk to this person
        self.extroversion = .0  # How willing someone is to talk at all
        self.gender = .0  # 1.0 comfortable talking to males, -1.0 comfortable talking to females

        self.relationships = []

    def get_relationship(self, person):
        try:
            return [r for r in self.relationships if person in r.people][0]
        except IndexError:
            r = Relationship(self, person)
            self.relationships.append(r)
            return r

    def __repr__(self):
        return self.name


class Relationship:
    def __init__(self, p1, p2):
        self.people = [p1, p2]
        self.tolerance = {p1:.1, p2:.1}  # What each person thinks of the other
        self.strength = {p1:.0, p2:.0}  # Perceived comfort between the two people
        self.innovation = {p1:.1, p2:.1}  # Current desire to strengthen a relationship
        self.intimacy = {p1:.0, p2:.0}  # How intimate or trusting the relationship is
        self.similarity = {p1:.0, p2:.0}  # How similar the people are