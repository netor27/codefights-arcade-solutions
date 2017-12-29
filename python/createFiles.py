
def main():

    fileNames = ["059_StringsConstruction", "060_IsSubstitutionCipher", "061_CreateAnagram", "062_ConstructSquare",
                 "063_NumbersGrouping", "064_DifferentSquares", "065_MostFrequentDigitSum", "066_NumberofClans"]

    directory = "./python/arcade-theCore/08_MirrorLake/"

    for name in fileNames:
        fullName = directory + name + ".py"
        print("Creating file " + fullName)
        f = open(fullName, "w+")
        f.close()


if __name__ == "__main__":
    main()
