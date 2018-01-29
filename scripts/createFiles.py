
def main():

    fileNames = ["098_ExtractMatrixColumn"
,"099_AreIsomorphic"
,"100_ReverseOnDiagonals"
,"101_SwapDiagonals"
,"102_CrossingSum"
,"103_DrawRectangle"
,"104_VolleyballPositions"
,"105_StarRotation"]

    directory = "arcade/python/arcade-theCore/12_ListBackwoods/"

    for name in fileNames:
        fullName = directory + name + ".py"
        print("Creating file " + fullName)
        f = open(fullName, "w+")
        f.close()


if __name__ == "__main__":
    main()
