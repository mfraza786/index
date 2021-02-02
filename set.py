#create an Empty Set
s=set()

#Add Element to Set.
s.add(1)
s.add(3)
s.add(5)
s.add(2)
s.add(1)
s.add(7)
s.add(4)
print(s)
s.remove(4)
print(" Set ofter Remove Function : ", s)
new = int (input("Enter New number: "))
s.add(new)
print(" Set after add new number",s)
print()
print(f"The set has {len(s)} Elements")
