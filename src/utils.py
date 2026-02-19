import os
import sys

def get_system_info():
    # Line 15: Unused import 'os'
    return sys.platform

# BUG: IMPORT Error
from math import non_existent_function