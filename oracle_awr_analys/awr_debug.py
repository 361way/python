#! /usr/bin/python
import awr_configure

def d_print(input_string,level):
    if  awr_configure.debug_flag >= level:
        print input_string   
    return

if __name__ == "__main__":
    d_print(1234)
