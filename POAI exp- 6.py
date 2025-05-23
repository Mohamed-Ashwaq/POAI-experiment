def negate_literal(literal):
    return literal[1:] if literal.startswith('~') else '~' + literal

def resolve(ci, cj):
    resolvents = []
    for li in ci:
        for lj in cj:
            if li == negate_literal(lj):
                # Remove li and lj, combine the rest
                new_clause = list(set(ci + cj))
                new_clause.remove(li)
                new_clause.remove(lj)
                # Sort for consistency
                resolvents.append(sorted(new_clause))
    return resolvents

def resolution(kb, query):
    clauses = kb[:]
    # Add negation of the query
    negated_query = [negate_literal(lit) for lit in query]
    clauses.append(negated_query)

    new = set()

    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i + 1, n)]
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            for resolvent in resolvents:
                if resolvent == []:
                    return False  # contradiction found
                resolvent_tuple = tuple(sorted(resolvent))
                if resolvent_tuple not in new:
                    new.add(resolvent_tuple)

        if all(list(clause) in clauses for clause in new):
            return True  # no new information, satisfiable

        for clause in new:
            if list(clause) not in clauses:
                clauses.append(list(clause))

# Define Knowledge Base and Query
kb = [['~P', 'Q'], ['P'], ['~Q', 'R'], ['~R']]
query = ['R']

print("Knowledge Base:", kb)
print("Query:", query)

if resolution(kb, query):
    print("The query is satisfiable.")
else:
    print("The query is not satisfiable.")
