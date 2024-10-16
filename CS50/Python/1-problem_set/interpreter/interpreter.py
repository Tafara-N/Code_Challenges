#!/usr/bin/env python3

"""
Program prompts the user for an arithmetic expression and then calculates and
outputs the result as a floating-point value formatted to one decimal place.

Assume that the user’s input will be formatted as x y z, with one space between
x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer

"""


def interpreter(x: int, y: str, z:int) -> float:
    """
    Calculate the result of an arithmetic expression.

    Arguments:
        x: First operand
        y: Operator
        z: Second operand

    Returns:
        float
            The result of the arithmetic expression.
    """

    match y:
        case "+":
            return float(x) + float(z)
        case "-":
            return float(x) - float(z)
        case "*":
            return float(x) * float(z)
        case "/":
            try:
                return float(x) / float(z)
            except ZeroDivisionError as error:
                print(f"Error: {error}")
                exit(1)
        case _:
            return 0.0


def main() -> None:
    """
    Prompt the user for an arithmetic expression and then calculate and output
    """

    x, y, z = input("Expression: ").split()

    result = interpreter(int(x), y, int(z))

    print(f"{result:.1f}")


if __name__ == "__main__":
    main()
