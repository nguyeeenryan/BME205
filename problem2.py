from collections import defaultdict

ACGT_dict = defaultdict(lambda: 0)

DNA_string = input("Enter in DNA string: ")

for x in DNA_string:
    ACGT_dict[x] += 1

print(ACGT_dict["A"], ACGT_dict["C"], ACGT_dict["G"], ACGT_dict["T"])
