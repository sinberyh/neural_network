from todo.student import Student


def hello():
    s = Student('yjl')
    print(s.name)
    print("hello world.")
    print("changed https to ssh")


def main():
    hello()


if __name__ == '__main__':
    main()
