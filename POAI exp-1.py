# Mohamed Ashwaq .Y
# 241501113
# mohamedashwaq.y.2024.aiml@rajalakshmi.edu.in
# Function to unify two terms
def unify(var1, var2):
    if var1 == var2:
        return True  # Already unified
    elif isinstance(var1, str) and var1.islower():
        return {var1: var2}  # Assign var1 to var2
    elif isinstance(var2, str) and var2.islower():
        return {var2: var1}  # Assign var2 to var1
    else:
        return None  # Cannot unify

# Function to negate a literal correctly
def negate(literal):
    if isinstance(literal, list):  # Ensures lists are handled correctly
        return [negate(lit) for lit in literal]
    return literal[1:] if literal.startswith("~") else f"~{literal}"

# Function to resolve two clauses
def resolve(clause1, clause2):
    resolvents = []
    for lit1 in clause1:
        for lit2 in clause2:
            if lit1 == negate(lit2):
                new_clause = list(set(clause1 + clause2))
                new_clause.remove(lit1)
                new_clause.remove(lit2)
                resolvents.append(new_clause)
    return resolvents

# Function to perform resolution algorithm
def resolution(kb, query):
    clauses = kb + [negate(query)] if isinstance(query, str) else kb + [[negate(lit) for lit in query]]
    
    while True:
        new_clauses = []
        for clause1 in clauses:
            for clause2 in clauses:
                if clause1 == clause2:
                    continue
                resolvents = resolve(clause1, clause2)
                if [] in resolvents:
                    return True  # Query is satisfiable
                new_clauses.extend(resolvents)
        if all(new in clauses for new in new_clauses):
            return False  # No new information, query not satisfiable
        clauses.extend(new_clauses)

# User Input for Knowledge Base and Query
knowledge_base = [
    ["~P", "Q"],
    ["P"],
    ["~Q", "R"],
    ["~R"]
]
query = ["R"]  # Query as a list

# Print Input Information
print("Knowledge Base:", knowledge_base)
print("Query:", query)

# Run Resolution Algorithm
result = resolution(knowledge_base, query)

# Print Output
if result:
    print("The query is satisfiable.")
else:
    print("The query is not satisfiable.")
