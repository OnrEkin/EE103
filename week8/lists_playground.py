# Lists: Indices and slicing
# Run this script. When the (Pdb) prompt appears in the terminal, type:
#   len(seq)    -> 4
#   seq[3]      -> [1, 2]
#   seq[-1]     -> [1, 2]      last element
#   seq[3][0]   -> 1           first element of the inner list
#   seq[4]      -> IndexError: list index out of range (only indices 0..3 exist)
#   seq[1]      -> 'a'
#   seq[-2:]    -> [4, [1, 2]] slicing a list gives a list
#   seq[1:3]    -> ['a', 4]    index 3 is not included
# Type c (continue) or q (quit) to exit pdb.
#
# Step 4: comment out the pdb line, put a VS Code breakpoint on the print(seq) line,
# press F5 and type the same expressions in the DEBUG CONSOLE.

seq = [2, 'a', 4, [1, 2]]

print(seq)
import pdb; pdb.set_trace()
