import sys, select

print("You have 1 seconds to answer!")

i, o, e = select.select( [sys.stdin], [], [], 0.5 )

if (i):
  print("You said", sys.stdin.readline().strip())
else:
  print("You said nothing!")
