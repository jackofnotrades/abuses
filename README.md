# abuses
These are all terrible ideas


You really shouldn't do these things.

**fib.py**
A recursive Fibonacci sequence generator.  Python 3's recursion limit turns out to be 997, so this one will batch requests bigger than this by chunks <= 997, and return the full list.  It can be used as a library (import one or both of fib() and/or fib_helper()) or as a command-line script with a shebang line specifying Python 3; update the first line in the file to say `#!/usr/bin/env python` if you only have or want to use a different version to run it as a script.  Run it as `$>./fib.py <Fibonacci sequence length> [<output file name> (optional)]` (must be made executable, as in `chmod u+x fib.py`) or `python fib.py <Fibonacci sequence length> [<output file name> (optional)]`.

In the event of bugs, I deny all responsibility (FAKE NEWS!).  Use this script at your own risk.  The numbers get absurdly large, and it uses compute and memory resources.  Running it on my laptop to get the first 100000 took 4 minutes + 4.6 seconds to output to the shell, or 3 minutes + 53.3 seconds to write directly to a file (it would be included here, but it far exceeds Github's maximum file size, and can easily be recreated locally, if you feel like doing something absurd today).
