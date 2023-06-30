# GCASS
GCode ASSembly is an extension of standard GCode to aid in writing by hand. It allows you to make loops and use values of registers in your GCode. 

In its current iteration it essentially acts as a translator to convert gcass to normal gcode.

The following instructions are currently supported:
```
@mark <label>
@set <register> <value>
@add <register> <value>
@jinz <register> <label>
@jiz <register> <label>
```
These instructions are planned but not yet implemented:
```
@sub <register> <value>
@radd <register> <register>
@rsub <register> <register>
@push <register>
@pop <register>
@copy <register> <register>
@subr <label> ;run subroutine named <label>
@return ;end of subroutine definition 
```

## known issues
- gcass cannot tell when the code leads to an infinite loop.
