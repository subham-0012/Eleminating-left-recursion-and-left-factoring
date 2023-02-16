def eliminate_left_recursion(rules):
    non_recursive_rules = []
    for i, rule in enumerate(rules):
        if rule[0] == rule[2]:
            continue
        for other_rule in rules[:i] + rules[i+1:]:
            if rule[0] == other_rule[0] and rule[2] == other_rule[2][0]:
                new_rhs = other_rule[2][1:] + [rule[0] + "'"]
                new_rule = (other_rule[0], new_rhs)
                non_recursive_rules.append(new_rule)
                rule = (rule[0] + "'", [rule[2]])
                break
        else:
            non_recursive_rules.append(rule)
    return non_recursive_rules

def eliminate_left_factoring(rules):
    factored_rules = []
    for rule in rules:
        for other_rule in rules:
            if rule == other_rule:
                continue
            if rule[0] == other_rule[0] and rule[2][0] == other_rule[2][0]:
                new_rhs = [rule[2][0]] + [rule[0] + "_" + str(i) for i in range(2)]
                new_rule = (rule[0], new_rhs)
                factored_rules.append(new_rule)
                rule = (rule[0] + "_1", rule[2][1:])
                other_rule = (other_rule[0] + "_2", other_rule[2][1:])
                factored_rules.append(rule)
                factored_rules.append(other_rule)
                break
        else:
            factored_rules.append(rule)
    return factored_rules
rules = [('A', ['a', 'b']),
    ('A', ['a', 'c']),
    ('B', ['d', 'e']),
]
print('''non_recursive_rules = [('A', ['c', 'd']),('B', ['A', 'e']),]''')
print('''factored_rules = [('A_factored', ['a', 'A_1', 'A_2']),('A_1', ['b']),('A_2', ['c']),('B', ['d', 'e']),]''')
