# Implement `ls`

You should already be familiar with the `ls` command line tool.

Your task is to implement your own version of `ls`.

It must act the same as `ls` would, if run from the directory containing this README.md file, for the following command lines:

* `ls -1`
* `ls -1 sample-files`
* `ls -1 -a sample-files`

Matching any additional behaviours or flags are optional stretch goals.

We recommend you start off supporting just `-1`, then adding support for `-a`.

Run the Python implementation from this directory with `python ls.py -1 sample-files`
or `python ls.py -1 -a sample-files`. Python 3 is required.
