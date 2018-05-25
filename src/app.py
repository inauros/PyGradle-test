from terminaltables import AsciiTable


def main():
    return AsciiTable([['Message'], ['It works fine!']], title='Info').table


if __name__ == "__main__":
    print main()
