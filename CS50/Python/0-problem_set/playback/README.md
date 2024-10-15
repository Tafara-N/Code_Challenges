# Playback Speed

Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called `playback.py`, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with `...` (i.e., three periods).

## Before You Begin

Log into cs50.dev, click on your terminal window, and execute cd by itself. You should find that your terminal window’s prompt resembles the below:

```bash
$
```

Next execute

```bash
mkdir playback
```

to make a folder called `playback` in your codespace.

Then execute

```bash
cd playback
```

to change directories into that folder. You should now see your terminal prompt as `playback/ $`. You can now execute

```bash
code playback.py
```

to make a file called `playback.py` where you’ll write your program.

### How to Test

Here’s how to test your code manually:

Run your program with python playback.py. Type This is CS50 and press Enter. Your program should output:
This...is...CS50
Run your program with python playback.py. Type This is our week on functions and press Enter. Your program should output:
This...is...our...week...on...functions
Run your program with python playback.py. Type Let's implement a function called hello and press Enter. Your program should output
Let's...implement...a...function...called...hello
You can execute the below to check your code using check50, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

check50 cs50/problems/2022/python/playback
Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that check50 outputs to see the input check50 handed to your program, what output it expected, and what output your program actually gave.

### How to Submit

In your terminal, execute the below to submit your work.

```bash
submit50 cs50/problems/2022/python/playback
```
