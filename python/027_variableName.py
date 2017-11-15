import re

def variableName(name):
    '''
    Correct variable names consist only of Latin letters, digits and underscores 
    and they can't start with a digit.
    Check if the given string is a correct variable name.
    '''
    p = re.compile("^[a-zA-Z_$][a-zA-Z_$0-9]*$")
    return p.match(name) is not None

print(variableName("asdf"))
print(variableName("0sdf"))
print(variableName("____f24fsdf__"))
print(variableName("sgwda_asdfasdf__asdf__"))