A simple requests per second (rps) counter.

Intended for use in combination with POSIX tail (or similar) program.
Example: tail -f /var/log/access-log1 /var/log/access-log2 | rps
Of course, its usage is reasonable for highly loaded services only ;-)
