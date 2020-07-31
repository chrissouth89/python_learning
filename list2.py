lucky_numbers = [4, 8, 15, 16, 23, 42]

friends = ["Michael", "Dwight", "Kevin", "Jim", "Angela", "Oscar", "Pam", "Jim", "Jim"]
friends.insert(1, "Kelly")
friends.remove("Angela")
print(friends)
print(friends.count("Jim"))
friends2 = friends.copy()
friends.clear()
print(friends)

lucky_numbers.reverse()
print(lucky_numbers)


print(friends2)
