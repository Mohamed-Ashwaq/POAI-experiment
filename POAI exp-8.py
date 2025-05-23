# Facts: Initial known facts
facts = {
    'a': True,
    'b': True,
    'c': False
}

# Rules: List of rules (conclusion, conditions)
rules = [
    ('d', ['a', 'b']),  # d if a and b
    ('e', ['b', 'c']),  # e if b and c
    ('f', ['d', 'e'])   # f if d and e
]

def forward_chaining(facts, rules):
    inferred = facts.copy()
    changed = True

    while changed:
        changed = False
        for head, body in rules:
            if head not in inferred:
                # Check if all conditions in the body are true
                if all(inferred.get(cond, False) for cond in body):
                    inferred[head] = True
                    changed = True
    return inferred

# Run forward chaining
inferred_facts = forward_chaining(facts, rules)

# Check specific goals
goals = ['f', 'e', 'd']
for goal in goals:
    if inferred_facts.get(goal, False):
        print(f"The goal '{goal}' can be achieved.")
    else:
        print(f"The goal '{goal}' cannot be achieved.")
