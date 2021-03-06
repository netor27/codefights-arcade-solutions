'''
Court is in session. We got a group of witnesses who have all taken an oath to tell the truth. The prosecutor is pointing at the defendants one by one and asking each witnesses a simple question - "guilty or not?". The witnesses are allowed to respond in one of the following three ways:

I am sure he/she is guilty.
I am sure he/she is innocent.
I have no idea.
The prosecutor has a hunch that one of the witnesses might not be telling the truth so she decides to cross-check all of their testimonies and see if the information gathered is consistent, i.e. there are no two witnesses A and B and a defendant C such that A says C is guilty while B says C is innocent.

Example

For

evidences = [[ 0, 1, 0, 1], 
             [-1, 1, 0, 0], 
             [-1, 0, 0, 1]]
the output should be
isInformationConsistent(evidences) = true;

For

evidences = [[ 1, 0], 
             [-1, 0], 
             [ 1, 1],
             [ 1, 1]]
the output should be
isInformationConsistent(evidences) = false.
'''

def isInformationConsistent(evidences):
    for j in range(len(evidences[0])):
        aux = 0
        for i in range(len(evidences)):
            if evidences[i][j] != 0:
                if aux == 0:
                    aux = evidences[i][j]
                elif aux != evidences[i][j]:
                    return False
    return True
            