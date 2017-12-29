
def main():

    fileNames = ["051_EncloseInBrackets",
                 "052_ProperNounCorrection",
                 "053_IsTandemRepeat",
                 "054_IsCaseInsensitivePalindrome",
                 "055_FindEmailDomain",
                 "056_HTMLEndTagByStartTag",
                 "057_IsMAC48Address",
                 "058_IsUnstablePair"]

    directory = "./python/arcade-theCore/07_BookMarket/"

    for name in fileNames:
        fullName = directory + name + ".py"
        print("Creating file " + fullName)
        f = open(fullName, "w+")
        f.close()


if __name__ == "__main__":
    main()
