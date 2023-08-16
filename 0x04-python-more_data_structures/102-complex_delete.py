#!/usr/bin/python3
def complex_delete(primDictionary, primValue):
    for key, value in sorted(primDictionary.items()):
        if value == primValue:
            del primDictionary[key]
    return prmDictionary
