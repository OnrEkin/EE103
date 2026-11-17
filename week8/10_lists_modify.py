# Lists: Modify a list

# Part 1: Define and append
L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2          # + creates a NEW list
print("L4 = L1 + L2      ->", L4)   # ['re', 'mi']

L3.append(L4)         # append adds L4 as ONE element (a list inside a list)
print("L3.append(L4)     ->", L3)   # ['do', ['re', 'mi']]

L = L1.append(L3)     # append changes L1 in place and returns None
print("L = L1.append(L3) -> L =", L)    # None
print("                     L1 =", L1)  # ['re', ['do', ['re', 'mi']]]

# Part 2: Step-by-step modifications
notes = ['do', 're', 'mi']
print("start          ", notes)
notes.extend(['fa', 'sol', 'la', 'si'])
print("extend         ", notes)   # ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']
notes.insert(6, 'ti')
print("insert(6,'ti') ", notes)   # ['do', 're', 'mi', 'fa', 'sol', 'la', 'ti', 'si']
notes[0] = 'DO'
print("notes[0]='DO'  ", notes)
notes[1:3] = ['RE', 'MI']
print("notes[1:3]=... ", notes)   # ['DO', 'RE', 'MI', 'fa', 'sol', 'la', 'ti', 'si']
notes.remove('ti')
print("remove('ti')   ", notes)   # ['DO', 'RE', 'MI', 'fa', 'sol', 'la', 'si']
last_note = notes.pop()
print("pop()          ", notes, " last_note =", last_note)   # 'si'
removed = notes.pop(2)
print("pop(2)         ", notes, " removed =", removed)       # 'MI'
del notes[0]
print("del notes[0]   ", notes)   # ['RE', 'fa', 'sol', 'la']
notes.reverse()
print("reverse()      ", notes)   # ['la', 'sol', 'fa', 'RE']
notes.sort()
print("sort()         ", notes)   # ['RE', 'fa', 'la', 'sol'] (uppercase comes before lowercase in ASCII)
notes.clear()
print("clear()        ", notes)   # []
