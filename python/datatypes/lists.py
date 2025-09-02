friends=['vaibhav','gaurav','somil'] #mutable
friends.append('sahil')
for i in range(len(friends)):
    print(friends[i])
friends.remove('vaibhav')
others=['ishita','trusha']
friends.extend(others)
print(friends)
friends.insert(3,'vaibhav')
friends.append('vaibhav')
who_got_removed=friends.pop()
print(friends)
print(who_got_removed)
friends.reverse()
print(friends)
friends.sort()
print(friends)
#max and min is also possible in list
print(max(friends))
print(min(friends))
final_friends=friends+others
print(final_friends)
f_f=friends*2
print(f_f)
raw_data=bytearray(b"hello")
raw_data=raw_data.replace(b"e",b"a")
print(raw_data)