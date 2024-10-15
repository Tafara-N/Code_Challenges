# Deep Thought

```
“All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
“You’re really not going to like it,” observed Deep Thought.
“Tell us!”
“All right,” said Deep Thought. “The Answer to the Great Question…”
“Yes…!”
“Of Life, the Universe and Everything…” said Deep Thought.
“Yes…!”
“Is…” said Deep Thought, and paused.
“Yes…!”
“Is…”
“Yes…!!!…?”
“Forty-two,” said Deep Thought, with infinite majesty and calm.”

  — The Hitchhiker’s Guide to the Galaxy, Douglas Adams
```

In `deep.py`, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting `Yes` if the user inputs `42` or (case-insensitively) `forty-two` or `forty two`. Otherwise output `No`.

**Hints**

- No need to convert the user’s input to an `int` if you check for equality with `"42"`, a `str`, rather than `42`, an `int`!
- It’s okay if your output or the user’s wraps onto multiple lines.

## Before You Begin
Log into cs50.dev, click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```bash
$
```

Next execute

```bash
mkdir deep
```

to make a folder called `deep` in your codespace.

Then execute

```bash
cd deep
```

to change directories into that folder. You should now see your terminal prompt as `deep/ $`. You can now execute

```bash
code deep.py
```

to make a file `called deep.py` where you’ll write your program.

### How to Test

Here’s how to test your code manually:

- Run your program with `python deep.py`. Type `42` and press Enter. Your program should output:

```bash
    Yes
```

- Run your program with `python deep.py`. Type `Forty Two` and press Enter. Your program should output:

```bash
    Yes
```

- Run your program with `python deep.py`. Type `forty-two` and press Enter. Your program should output

```bash
    Yes
```

- Run your program with `python deep.py`. Type `50` and press Enter. Your program should output

```bash
    No
```

Be sure to vary the casing of your input and “accidentally” add spaces on either side of your input before pressing enter. Your program should behave as expected, case- and space-insensitively.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```bash
check50 cs50/problems/2022/python/deep
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

### How to Submit

In your terminal, execute the below to submit your work.

```bash
submit50 cs50/problems/2022/python/deep
```
