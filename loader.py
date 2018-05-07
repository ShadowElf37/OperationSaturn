from people import Person, Relationship

def load_people():
    f = open('people.cfg')
    data = ''
    people = []
    mode = 0
    p = None
    v1 = ''
    v2 = ''
    for char in f.read():
        if char not in ';{}=':
            data += char
            continue
        elif char == '{' and mode == 0:
            p = Person(data.strip())
            people.append(p)
            mode = 1
        elif char == '=' and mode == 1:
            v1 = data.strip()
        elif char == ';' and mode == 1:
            v2 = data.strip()
            setattr(p, v1, float(v2))
        elif char == '}' and mode == 1:
            mode = 0
        data = ''

    return people

def load_relationships(people):
    f = open('relationships.cfg')
    data = ''
    mode = 0
    p = None
    r = None
    v1 = ''
    v2 = ''
    for char in f.read():
        if char not in ';{}=':
            data += char
            continue
        elif char == '{' and mode == 0:
            p = [p for p in people if p.name == data.strip()][0]
            mode = 1
        elif char == '{' and mode == 1:
            p2 = [p for p in people if p.name == data.strip()][0]
            try:
                r = [r for r in p.relationships if data.strip() in map(lambda x: x.name, r.people)][0]
            except IndexError:
                r = Relationship(p, p2)
                p.relationships.append(r)
                p2.relationships.append(r)
            mode = 2
        elif char == '=' and mode == 2:
            v1 = data.strip()
        elif char == ';' and mode == 2:
            v2 = data.strip()
            a = getattr(r, v1)
            a[p] = float(v2)
            setattr(r, v1, a)
        elif char == '}' and mode == 2:
            mode = 1
        elif char == '}' and mode == 1:
            mode = 0
        data = ''