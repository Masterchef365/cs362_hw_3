#!/usr/bin/env python3
def is_leap_year(y):
    if y % 4 != 0:
        return False
    if y % 100 != 0:
        return True
    return y % 400 == 0

def main():
    pass

if __name__ == "__main__":
    main()
