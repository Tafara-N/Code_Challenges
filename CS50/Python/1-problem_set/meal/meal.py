#!/usr/bin/env python3

"""
Program prompts the user for a time and outputs whether it’s breakfast time,
lunch time, or dinner time.

If it’s not time for a meal, don’t output anything at all.

Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.

And assume that each meal’s time range is inclusive.

For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between,
it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be
called by main) that converts time, a str in 24-hour format, to the corresponding
number of hours as a float.

For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes),
convert should return 7.5 (i.e., 7.5 hours).

"""


def main() -> None:
    """
    Main function for meal program
    """

    time = input("What time is it? ")

    converted_time = convert(time)

    match converted_time:
        case _ if 7.0 <= converted_time <= 8.0:
            print("breakfast time")
        case _ if 12.0 <= converted_time <= 13.0:
            print("lunch time")
        case _ if 18.0 <= converted_time <= 19.0:
            print("dinner time")
        case _:
            pass


def convert(time: str) -> float:
    """
    Convert time from 12/24-hour format to float.

    Arguments:
        time: Time in 24-hour format

    Returns:
        float
            The corresponding number of hours as a float
    """

    time = time.lower().replace(".", "")

    if "am" in time or "pm" in time:
        # Split time, store time and it's meridiem
        time, meridiem = time.split()

        # Split time, convert hr and minutes to int, store hr and minutes
        hours, minutes = map(int, time.split(":"))

        if meridiem == "pm" and hours != 12:
            hours += 12
        elif meridiem == "am" and hours == 12:
            hours = 0
    else:
        hours, minutes = map(int, time.split(":"))

    return hours + (minutes / 60)


if __name__ == "__main__":
    main()
