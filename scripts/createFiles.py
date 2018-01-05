
def main():

    fileNames = ["088_ArrayConversion", "089_ArrayPreviousLess", "090_PairofShoes", "091_Combs", "092_StringsCrossover",
                 "093_CyclicString", "094_BeautifulText", "095_RunnersMeetings", "096_ChristmasTree", "097_FileNaming"]

    directory = "../arcade/python/arcade-theCore/11_SprintOfIntegration/"

    for name in fileNames:
        fullName = directory + name + ".py"
        print("Creating file " + fullName)
        f = open(fullName, "w+")
        f.close()


if __name__ == "__main__":
    main()
