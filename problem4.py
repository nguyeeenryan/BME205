
input_string = input("Enter String: ")
indices = input("Enter indices a b c d: ").split(" ")
indices = [int(x) for x in indices]

print(input_string[indices[0]:indices[1]+1], input_string[indices[2]:indices[3]+1])
