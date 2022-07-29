import atheris
import sys
import os
from pytils import numeral

def TestOneInput(data):
    barray=bytearray(data)
    fdp=atheris.FuzzedDataProvider(data)
    numeral.in_words(fdp.ConsumeInt(len(data)))


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
