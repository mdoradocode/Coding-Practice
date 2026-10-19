import string as str


def ghostWriter(text: str) -> str:
    newstr = ""
    if len(text) == 0 and type(text) is str:
        return "The Ghost Didn't Write Anything..."
    for index, char in enumerate(text):
        if char == "#":
            newstr = newstr[:-1]
        elif char == "~":
            if len(newstr) > 0:
                newstr += newstr[-1]
        else:
            newstr += char
    return newstr


def main():
    print(ghostWriter("ghost"))
    print(ghostWriter("a#~b"))
    print(ghostWriter("ab~c#"))
    print(ghostWriter("BBB##O~"))
    print(ghostWriter("~~~B~~##~pp"))
    print(ghostWriter("B~~~~~p"))


if __name__ == "__main__":
    main()
