import atheris
import sys
import os
from pytils import numeral

def TestOneInput(data):
    barray=bytearray(data)
    fdp=atheris.FuzzedDataProvider(data)
    try:
        numeral.in_words(fdp.ConsumeInt(len(data)))
    except ValueError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
