brackets = {'(': ')', '{': '}', '[': ']'}


def is_correct_bracket_seq(line):
    open_brackets = []
    for i in line:
        if i in brackets.keys():

            open_brackets.append(i)
        else:
            if not open_brackets:
                return False
            if i != brackets[open_brackets.pop()]:
                return False
    return not open_brackets


print(is_correct_bracket_seq(input()))
