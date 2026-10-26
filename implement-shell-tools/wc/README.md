# Implement `wc`

You should already be familiar with the `wc` command line tool.

Your task is to implement your own version of `wc`.

It must act the same as `wc` would, if run from the directory containing this README.md file, for the following command lines:

* `wc sample-files/*`
* `wc -l sample-files/3.txt`
* `wc -w sample-files/3.txt`
* `wc -c sample-files/3.txt`
* `wc -l sample-files/*`

Matching any additional behaviours or flags are optional stretch goals.

We recommend you start off supporting no flags for one file, then add support for multiple files, then add support for the flags.

Run the Python implementation from this directory with `python wc.py sample-files/1.txt`
or `python wc.py -l sample-files/3.txt`. Multiple filenames and combined count
flags are supported. Expand wildcards in your shell, or pass filenames explicitly
if your shell does not expand them. Python 3 is required.
