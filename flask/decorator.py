def awesome(func):
    def wrapper():
        func()
        print("No, you are awesome")
    return warapper

@login_required
def ordinary():
    print("I am ordinary")

extra_ordinary = awesome(ordinary)
print(extra_ordinary)