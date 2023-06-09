#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for n in range(0, len(dir(hidden_4))):
        if f"{dir(hidden_4)[n][:2]}" != f"__":
            print(dir(hidden_4)[n])
