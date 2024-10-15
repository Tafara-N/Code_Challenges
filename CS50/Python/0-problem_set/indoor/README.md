# Indoor Voice

WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called `indoor.py`, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a `str` of your own as an argument to `input`.

## Before You Begin

Execute `cd` by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:

```bash
$
```

Next execute

```bash
mkdir indoor
```

to make a folder called `indoor` in your codespace.

Then execute

```bash
cd indoor
```

to change directories into that folder. You should now see your terminal prompt as `indoor/ $`. You can now execute

```bash
code indoor.py
```

to make a file called `indoor.py` where you’ll write your program.

### How to Test

Here’s how to test your code manually. At the `indoor/ $` prompt in your terminal: :

- Run your program with `python indoor.py`. Type `HELLO` and press Enter. Your program should output `hello`.
- Run your program with `python indoor.py`. Type `THIS IS CS50` and press Enter. Your program should output `this is cs50`.
- Run your program with `python indoor.py`. Type `50` and press Enter. Your program should output `50`.

If you run into an error saying your file cannot be opened, retrace your steps to be sure that you are inside your `indoor` folder and have saved your `indoor.py` file there. Remember how?

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```bash
check50 cs50/problems/2022/python/indoor
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

How to Submit

In your terminal, execute the below to submit your work.

```bash
submit50 cs50/problems/2022/python/indoor
```
