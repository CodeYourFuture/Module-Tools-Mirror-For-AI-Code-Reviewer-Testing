# Implement `cat`

You should already be familiar with the `cat` command line tool.

Your task is to implement your own version of `cat`.

It must act the same as `cat` would, if run from the directory containing this README.md file, for the following command lines:

* `cat sample-files/1.txt`
* `cat -n sample-files/1.txt`
* `cat sample-files/*.txt`
* `cat -n sample-files/*.txt`
* `cat -b sample-files/3.txt`

Matching any additional behaviours or flags are optional stretch goals.

We recommend you start off supporting no flags, then add support for `-n`, then add support for `-b`.

Run the Python implementation from this directory with `python cat.py sample-files/1.txt`
or `python cat.py -n sample-files/1.txt sample-files/2.txt`. Use `-b` to number
nonempty lines. Python 3 is required. Pass filenames explicitly if your shell
does not expand wildcards.
