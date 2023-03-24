
4
This assumes that the length of the stream is known.
You've done something, but it isn't reservoir sampling.
Come to office hours and let's get this cleared up.

str_list = list(stream)

This collects everything into memory, which reservoir sampling is designed to avoid.
The core of the algorithm is essentially correct though. Come to office hours and we can discuss.

Your output of all 900's for range(1000) indicates an error in the implementation.

9
Show output from range(1000)

Show output from unit tests

len(stream)
Don't assume that the length of stream is known.
Don't assume that the length of stream is known, or that you can index into it.
Instead, loop directly over the stream.
I need to add a test case to prevent this!

