intended_probability = float(input("Enter the intended probability: "))
reward = float(input("Enter the reward for each step: "))
discount = float(input("Enter the discount factor: "))

while True:
    up = float(input("Enter the value of moving up: "))
    right = float(input("Enter the value of moving right: "))
    a = reward + discount * (intended_probability * up + (1 - intended_probability) * right)
    b = reward + discount * (intended_probability * right + (1 - intended_probability) * up)
    print("The biggest value is: ", max(a, b))