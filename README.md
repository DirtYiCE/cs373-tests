Unit tests for Udacity CS373 homeworks
======================================

* [https://github.com/DirtYiCE/cs373-tests](https://github.com/DirtYiCE/cs373-tests)

Requirements
------------

* `git` (to clone the repo ;) )
* `python-2.x` (tested with 2.7.2, but probably works with 2.6 too)
* text editor of your choice

Quick usage
-----------

1.  Clone the repo (if you haven't done already):

        $ git clone git://github.com/DirtYiCE/cs373-tests.git
        $ cd cs373-tests

2.  Make sure you have set `$EDITOR` to your favourite text editor, then issue:

        $ ./test.py <homework_number> edit

    Where `<homework_number>` is in format like `1.4` for the 4<sup>th</sup>
    question in the first homework. You can also just open
    `<homework_number>/code.py` with your editor if you do not like to use the
    command like (altough you may need to create the file first).

    It will be an empty file, do not worry. It will set the given variables to
    the given values before executing your code. You actually only have to write
    the part after the "do not modify anything before" lines, and you also don't
    have to print it (just place in the correct variable).

    For example, given a task to add two numbers together, you would get
    something like this to edit:

        a = 4.0
        b = 5.0

        # ENTER CODE BELOW

        c = 0.0



        # You must print it with the following code:

        print(c)

    Then, when you run `./test.py <num> edit`, you only have to enter

        c = a + b

    And it will work like you just inserted it after `c = 0.0`.

3.  When you think you should test your code, with the examples given in the
    homework assigment, run:

       $ ./test.py <homework_number>

    If all test passes, you will see an `OK` at the end of output. Otherwise it
    will tell you which tests failed, the expected and your output.

4.  When you are done, simply paste your code into the correct place in the web
    interface. Alternatively, you can use

        $ ./test.py <homework_number> format

    to print your code (to the stdout) with all the required header and footer
    stuff. If you use `run` instead of `format`, it will run the code in python,
    just to check if everything is right.

    You will probably want to run the code before saving it (in the browser),
    just in case Udacity's python handles somehing differently.

Available commands
------------------

General syntax is:

    $ ./test.py <homework_number> [command] [arguments]

`command` defaults to `test` when not specified. Available commands:

* `edit`: open your solution (`<homework_number>/code.py`) with `$EDITOR`
* `zap`: deletes your solution
* `test`: run the tests. Arguments you pass will be handled by
  [python unittest](http://docs.python.org/library/unittest.html#command-line-options).
* `format`: place headers and footers around your solution, then print to stdout.
* `run`: executes the output of `format`

License
-------

`*/template.py` files are from Udacity. Other files were written by me, and
you're free to do whatever you want do with them. They are available under the
terms of [WTFPL](http://sam.zoy.org/wtfpl/), if you like that better.

This program is free software. It comes without any warranty, to the extent
permitted by applicable law.

Bugs/contribution
-----------------

Use github's issue tracker or create a pull request with your patch.

Notes
-----

This program doesn't contain the solution to the homework, nor tells you if
they're correct. It justs tests that the example inputs given in the assigment
produces the same output as in the video. It only saves you from manually typing
the inputs then comparing the numbers (which is quite error prone). Otherwise,
it gives you no advantage.
