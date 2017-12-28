
def main():

    fileNames = ["043_IsPower", "044_IsSumofConsecutive2", "045_SquareDigitsSequence", "046_PagesNumberingWithInk",
                 "047_ComfortableNumbers", "048_WeakNumbers", "049_RectangleRotation", "050_CrosswordFormation"]

    directory = "./arcade-theCore/06_LabyrinthOfNestedLoops/"

    for name in fileNames:
        fullName = directory + name + ".py"
        print("Creating file " + fullName)
        f = open(fullName, "w+")
        f.close()


if __name__ == "__main__":
    main()
