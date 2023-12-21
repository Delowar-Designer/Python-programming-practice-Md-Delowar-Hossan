# Queue Example
bank = ["x","y","a"]
print(bank)
bank.append("z")
print(bank)

from collections import deque

bank1 = deque(["Anis","Karim","Bijoy"])
print(bank1)
bank1.popleft()
print(bank1)
bank1.popleft()
print(bank1)
bank1.popleft()
print(bank1)
if not bank1:
    print("No person Left")