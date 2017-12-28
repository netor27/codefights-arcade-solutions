import itertools
def crosswordFormation(words):
    r = 0
    for w in itertools.permutations(words):
        print(w)
        #print("\t", w[0])
        for s1 in range(len(w[0]) - 2):
            ps1 = [i for i,p in enumerate(w[1]) if p == w[0][s1]]
            #if len(ps1) > 0:
                #print("\t\t", w[0][s1], " with ", w[1])
                #print("\t\t", ps1)                
            for s2 in range(s1 + 2, len(w[0])):
                ps2 = [i for i,p in enumerate(w[2]) if p == w[0][s2]]
                #if len(ps2) > 0:
                    #print("\t\t\t", w[1][s2], " with ", w[2])
                    #print("\t\t\t", ps2)
                for pw1 in ps1:
                    for pw2 in ps2:
                        #print(w[0][s1], w[1][s2], pw1, pw2)
                        for c1, c2 in zip(w[1][pw1+2:], w[2][pw2+2:]):
                            for c3, c4 in zip(w[0], w[3][s2 - s1:]):
                                r += c1 == c3 and c2 == c4
    return r


print(crosswordFormation(["crossword", 
 "square", 
 "formation", 
 "something"]))
# import ?????????
# def crosswordFormation(words):
#     r = 0
#     ??? w in itertools.permutations(words):
#         ??? s1 in range(len(w[?]) - 2):
#             ps1 = [i for i,? in enumerate(w[1]) if ? == w[0][s1]]
#             for s2 ?? range(s1 + 2, len(w[?])):
#                 ps2 = [i for i,c ?? enumerate(w[2]) if c == ?[0][s2]]
#                 for pw1 in ???:
#                     for pw2 in ps2:
#                         for ??, c2 in zip(w[1][???+2:], w[2][pw2+2:]):
#                             ??? c3, c4 in zip(w[?], w[3][s2 - s1:]):
#                                 r += ?? == c3 and c2 == c4
#     return ?




# from functools import reduce
# from ????????? import permutations

# # horizontal rotate clockwise, ???????? rotate counterclockwise
# # top becomes left, ???? becomes top
# # (t,l,r,?) == (l,t,b,r)

# def ??????????(top,left,right,bot):
#     return ???([sum([sum([sum([sum([sum([? for b1 in range(len(???)+t1-t2) if bot[b1] == ????[l2] and bot[b1+t2-??] == right[r1+l2-l1]]) for ?? in range(l1+2,min(???(left),l1+len(right)-r1))]) ??? l1 in range(len(left)-?) if top[t1]==left[l1]]) ??? t1 in range(t2-1)]) ??? t2 in range(2,len(???)) if top[t2]==right[r1]]) ??? r1 in range(len(right)-?)])

# def crosswordFormation(words):
#     return 2*???(numSquares(*p) for p in ????????????(words) if p[0] < p[?])