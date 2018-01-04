'''
Given two version strings composed of several non-negative decimal fields separated by periods ("."), both strings contain equal number of numeric fields. Return true if the first version is higher than the second version and false otherwise.

The syntax follows the regular semver ordering rules:

1.0.5 < 1.1.0 < 1.1.5 < 1.1.10 < 1.2.0 < 1.2.2
< 1.2.10 < 1.10.2 < 2.0.0 < 10.0.0
There are no leading zeros in any of the numeric fields, i.e. you do not have to handle inputs like 100.020.003 (it would instead be given as 100.20.3).

Example
'''
def higherVersion(ver1, ver2):
    spVer1 = ver1.split('.')
    spVer2 = ver2.split('.')
    for i in range(len(spVer1)):
        d1, d2 = int(spVer1[i]) , int(spVer2[i])
        if d1 > d2:
            return True
        elif d2 > d1:
            return False
    return False
