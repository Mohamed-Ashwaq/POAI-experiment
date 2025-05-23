# Initial stacks
stacks = [[0], [1], [2]]

def print_stacks():
    for stack in stacks:
        print("Block(s) on stack:", stack)
    print()

# Output Header
print("Output:\n")

# Initial State
print("Initial state:")
print_stacks()

# Goal State (just a display, no change in state yet)
print("Goal state set.")
print("Block(s) on stack:", [0, 1])
print("Block(s) on stack:", [2])
print()

# Performing Moves
print("Performing Moves:")

# Step 1: Move block 0 to stack 2 (on top of 2), stack[0] becomes empty
stacks[2].insert(0, stacks[0].pop())  # move 0 to stack 2 (front)
print_stacks()

# Step 2: Repeat the current state (unchanged)
print_stacks()

# Step 3: Move block 2 from stack 2 to stack 0, then block 1 to stack 0
block_2 = stacks[2].pop(1)  # 2 is now at position 1
stacks[0].append(block_2)

block_1 = stacks[1].pop()
stacks[0].append(block_1)

print_stacks()
