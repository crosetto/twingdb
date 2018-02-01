# twingdb

This is a simple GDB script which opens two executions and compares them, stopping at the fist difference.
It is using GDB underneeth with multiple inferiors, it exists because I needed it, and it's nothing fancy, nor
am I a gdb ninja. But it suits my purpose.

# Installation instructions:
clone the repo somewhere, and export the environment variable 
```
export TWINGDBPATH=<somewhere>
```

then print the help
```
<somewhere>/twingdb -h
```
