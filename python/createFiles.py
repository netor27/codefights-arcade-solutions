
def main():

    fileNames = ["035_CreateArray"
    ,"036_ArrayReplace"
    ,"037_FirstReverseTry"
    ,"038_ConcatenateArrays"
    ,"039_RemoveArrayPart"
    ,"040_IsSmooth"
    ,"041_ReplaceMiddle"
    ,"042_MakeArrayConsecutive2"]

    directory = "./arcade-theCore/05_ListForestEdge/"

    for name in fileNames:
        fullName = directory + name + ".py"
        print("Creating file " + fullName)
        f = open(fullName,"w+")
        f.close()


if __name__ == "__main__":
    main()