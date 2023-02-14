
def multi_bracket_validation(string):
    open_ = ["[", "{", "("]
    closed = ["]", "}", ")"]
    empty = []
    for i in string:
        if i in open_:
            empty.append(i)
        elif i in closed:
            pos = closed.index(i)
            if len(empty) > 0 and open_[pos] == empty[len(empty) - 1]:
                empty.pop()
            else:
                return False
    if len(empty) == 0:
        return True
    else:
        return False
