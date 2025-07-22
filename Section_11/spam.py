def spam1():
    def spam2():
        def spam3():
            z = " even more spam"
            return z
        y = " more spam"
        y += spam3()
        return y
    x = "spam" # X must exist before spam 2 is called
    x += spam2()
    return x

print(spam1())