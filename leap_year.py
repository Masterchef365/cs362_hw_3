#!/usr/bin/env python3
def is_leap_year(y):
    if y % 4 != 0:
        return False
    if y % 100 != 0:
        return True
    return y % 400 == 0

def main():
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


if __name__ == "__main__":
    main()
