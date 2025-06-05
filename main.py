#!/usr/bin/env python3

"""This file is to test the behavior of the agent when there is an existing 
lint error in the codebase.
"""
import os
import sys
tracer_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../execution-tracing/src"))
sys.path.insert(0, tracer_path)
from missing_colon import division
from tracer.core import start_tracing, stop_tracing

   
def f821():
    print("Function f821 called.")

def do_division(a: float, b: float):
    f821()
    return a / b

def another_func():
    result = division(10, 2)
    print(f"Result from division in another_func: {result}")


if __name__ == "__main__":

    start_tracing(scope_path=os.getcwd(), track_external_calls=False)
    print(f"Start tracing with scope: {os.getcwd()}")

    print(another_func())
    print(do_division(123, 15))

    stop_tracing("trace_output.json")
    print(f"Done tracing!")   
