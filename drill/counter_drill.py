from collections import Counter

my_list = ["thisisalist", "thisisanotherlist"]
my_str = "thisisalist"
print(Counter(my_str))

self_defined_counter = {}
for letter in my_str:
    if letter not in self_defined_counter:
        self_defined_counter[letter] = 1
    else:
        self_defined_counter[letter] += 1
print(self_defined_counter)