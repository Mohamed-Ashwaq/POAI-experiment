# Facts: The knowledge base containing information about facts
facts = {
    'a': True,
    'b': True,
    'c': False
}

# Rules: List of rules where each rule is a tuple (conclusion, conditions)
rules = [
    ('d', ['a', 'b']),  # d can be concluded if a and b are true
    ('e', ['b', 'c']),  # e can be concluded if b and c are true
    ('f', ['d', 'e'])   # f can be concluded if d and e are true
]

# Backward Chaining Function
def backward_chaining(goal, facts, rules):
    # If goal is already in known facts
    if goal in facts:
        return facts[goal]

    # Search for rules that can infer the goal
    for head, body in rules:
        if head == goal:
            # Recursively check all conditions in the rule body
            if all(backward_chaining(subgoal, facts, rules) for subgoal in body):
                # If all conditions are satisfied, the goal is achieved
                return True

    # If no rule can infer the goal or some conditions failed
    return False

# Function to evaluate and print result for a given goal
def evaluate_goal(goal):
    if backward_chaining(goal, facts, rules):
        print(f"The goal '{goal}' can be achieved.")
    else:
        print(f"The goal '{goal}' cannot be achieved.")

# Check for goals 'f' and 'd'
print("Expected Output for the Goal 'f':")
evaluate_goal('f')

print("\nExpected Output for the Goal 'd':")
evaluate_goal('d')
