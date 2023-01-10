#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    lists = dir(hidden_4)

    for i in lists:
        if i[:2] != "__":
            print(i)
