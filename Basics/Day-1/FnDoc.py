"""
A program to print the documentation of a function
"""
import builtins

fn=input()
print((getattr(builtins,fn).__doc__))
