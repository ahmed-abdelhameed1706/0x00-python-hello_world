#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    sorted_names = sorted(names)
    for name in sorted_names:
        if name[:2] != "__":
            print(name)
