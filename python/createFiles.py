
def main():

    fileNames = ["067_HouseNumbersSum", "068_AllLongestStrings", "069_HouseofCats", "070_AlphabetSubsequence", "071_MinimalNumberofCoins", "072_AddBorder",
                 "073_SwitchLights", "074_TimedReading", "075_ElectionsWinners", "076_IntegertoStringofFixedWidth", "077_AreSimilar", "078_AdaNumber", "079_ThreeSplit"]

    directory = "./python/arcade-theCore/09_WellOfIntegration/"

    for name in fileNames:
        fullName = directory + name + ".py"
        print("Creating file " + fullName)
        f = open(fullName, "w+")
        f.close()


if __name__ == "__main__":
    main()
