def isBalanced(text):
    b = 0
    for i in range(0, len(text)):
        c = text[i]
        if c == '(':
            b += 1
        elif b == 0:
            return i
        else:
            b -= 1
    return -1 if b == 0 else len(text)


def test(text, balanced):
    assert(isBalanced(text) == balanced)

test("()", -1)
test("(())", -1)
test("(()", 3)
test("((())", 5)
test("(())()", -1)
test("()())()", 4)
test("(())())", 6)