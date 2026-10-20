#std_num = int(input("What's your school number?"))
#print(f"Hello, my student number is {std_num}!")

#name_lower = 'name'
#name_upper = name_lower.upper()
#print(name_upper)

#[başlangıç:bitiş:adım]
#name_reversed = name_lower[::-1]
#print(name_reversed)

this_year = str(2026)
first_two = this_year[:2]
last_two = this_year[2:]

first_two = float(first_two)
last_two = float(last_two)

msum = first_two + last_two

print(f"{msum:.2f}")

if msum ==46:
    print("Correct")
else:
    print("Wrong")    
