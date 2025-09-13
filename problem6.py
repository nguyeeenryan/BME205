f = open("rosalind_ini5.txt", "r")


f2 = open("result_file.txt", "w")

lines = f.readlines()
count = 1

for line in lines:
    if count%2  == 0:
        f2.write(line)
    count += 1

f.close()
f2.close()

        
