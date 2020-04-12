class F1_Team:
    """ Represents a current F1 Team.
    """
    def __init__(self, name="team_name", races=0, wins=0, drivers_championships_years=[], constructors_championships_years=[]):
        """ Initializes a team's stats.
        """
        self.name = name
        self.races = races
        self.wins = wins
        self.drivers_championships_years = drivers_championships_years
        self.constructors_championships_years = constructors_championships_years

    def __str__(self):
        return f"{self.name} have a total of {len(self.drivers_championships_years) + len(self.constructors_championships_years)} championships and {self.wins} wins in {self.races} races \
        \n{self.name} Drivers' Championships:      {self.drivers_championships_years} \
        \n{self.name} Constructors' Championships: {self.constructors_championships_years}"

    def __add__(self, other):
        return F1_Team(self.name + " & " + other.name, \
            self.races + other.races, \
            self.wins + other.wins, \
            sorted(self.drivers_championships_years + other.drivers_championships_years), \
            sorted(self.constructors_championships_years + other.constructors_championships_years))

    def __eq__(self, other):
        if -2 <= comparison(self,other) < 2:
            return f"True, {self.name} has a roughly equal F1 racing heritage to {other.name}"
        else:
            return f"False, {self.name} does not have a roughly equal F1 racing heritage to {other.name}"

    def __ne__(self, other):
        if not -2 <= comparison(self,other) < 2:
            return f"True, {self.name} has a significantly unequal F1 racing heritage to {other.name}"
        else:
            return f"False, {self.name} does not have a significantly unequal F1 racing heritage to {other.name}"

    def __gt__(self, other):
        if comparison(self,other) > 2:
            return f"True, {self.name} has a significantly greater F1 racing heritage than {other.name}"
        else:
            return f"False, {self.name} does not have a significantly greater F1 racing heritage than {other.name}"        

    def __lt__(self, other):
        if comparison(self,other) < -2:
            return f"True, {self.name} has a significantly lesser F1 racing heritage than {other.name}"
        else:
            return f"False, {self.name} does not have a significantly lesser F1 racing heritage than {other.name}"  

    def __ge__(self, other):
        if comparison(self,other) >= -2:
            return f"True, {self.name} has at least a roughly equal F1 racing heritage to {other.name}"
        else:
            return f"False, {self.name} does not have at least an even roughly equal F1 racing heritage to {other.name}" 

    def __le__(self, other):
        if comparison(self,other) <= 2:
            return f"True, {self.name} has no more than a roughly equal F1 racing heritage to {other.name}"
        else:
            return f"False, {self.name} does have more than a roughly equal F1 racing heritage to {other.name}" 

Alfa_Romeo = F1_Team("Alfa Romeo", 131, 10, [1950, 1951], [])
Ferrari = F1_Team("Ferrari", 993, 237, [1952, 1953, 1956, 1958, 1961, 1964, 1975, 1977, 1979, 2000, 2001, 2002, 2003, 2004, 2007], [1961, 1964, 1975, 1976, 1977, 1979, 1982, 1983, 1999, 2000, 2001, 2002, 2003, 2004, 2007, 2008])
Haas = F1_Team("Haas", 83, 0, [], [])
McLaren = F1_Team("McLaren", 867, 182, [1974, 1976, 1984, 1985, 1986, 1988, 1989, 1990, 1991, 1998, 1999, 2008], [1974, 1984, 1985, 1988, 1989, 1990, 1991, 1998])
Mercedes = F1_Team("Mercedes", 210, 102, [1954, 1955, 2014, 2015, 2016, 2017, 2018, 2019], [2014, 2015, 2016, 2017, 2018, 2019])
Racing_Point = F1_Team("Racing Point", 21, 0, [], [])
Red_Bull = F1_Team("Red Bull", 287, 62, [2010, 2011, 2012, 2013], [2010, 2011, 2012, 2013])
Renault = F1_Team("Renault", 386, 35, [2005, 2006], [2005, 2006])
Toro_Rosso = F1_Team("Toro Rosso", 268, 1, [], []) # Monza 2008, insane!!
Williams = F1_Team("Williams", 731, 114, [1980, 1982, 1987, 1992, 1993, 1996, 1997], [1980, 1981, 1986, 1987, 1992, 1993, 1994, 1996, 1997])

def comparison(self, other):
    """ Function comparing F1 Teams' stats,
        outside oop/class to avoid repitition,
        as used for eq/ne/gt/lt
    """
    comparison = 0
    if self.races > other.races:
        comparison += 1
    elif self.races < other.races:
        comparison -= 1
    if self.wins > other.wins:
        comparison += 1
    elif self.wins < other.wins:
        comparison -= 1
    if len(self.drivers_championships_years) > len(other.drivers_championships_years):
        comparison += 1
    elif len(self.drivers_championships_years) < len(other.drivers_championships_years):
        comparison -= 1
    if len(self.constructors_championships_years) > len(other.constructors_championships_years):
        comparison += 1
    elif len(self.constructors_championships_years) < len(other.constructors_championships_years):
        comparison -= 1
    return comparison

print(Alfa_Romeo)
print(McLaren + Mercedes)
print(Ferrari == Racing_Point)
print(Mercedes != Haas)
print(Toro_Rosso > Alfa_Romeo)
print(Alfa_Romeo >= Toro_Rosso)
print(Renault < Williams)
print(Williams <= Renault)

def non_current_championships():
    """ Returns the constructors champions won by teams not currently on the grid
    """
    current_championships = (Alfa_Romeo+Ferrari+Haas+McLaren+Mercedes+Racing_Point+Red_Bull+Renault+Toro_Rosso+Williams).constructors_championships_years
    non_current_championships = []
    year = 1958
    while year < 2020:
        if year not in current_championships:
            non_current_championships.append(year)
        year += 1
    return f"The F1 Constructors' Championships won by teams no longer on the grid are: \n{non_current_championships}"

print(non_current_championships())