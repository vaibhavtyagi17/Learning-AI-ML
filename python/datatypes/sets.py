A={1, 2, 3}
B={3, 4, 5}
C=A.union(B)
D=A.intersection(B)
E=A|B
F=A&B
print(C)
print(D)
print(E)
print(F)
G=A-B #A.difference(B) A-(A&B)
H=A-(A&B)
print(H)
print(G)