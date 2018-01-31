
def main():

    fileNames = [
        "114_ShuffledArray", "115_SortbyHeight", "116_SortByLength", "117_BoxesPacking", "118_MaximumSum", "119_RowsRearranging", "120_DigitDifferenceSort", "121_UniqueDigitProducts"
    ]

    directory = "arcade/python/arcade-theCore/14_SortingOutpost/"

    for name in fileNames:
        fullName = directory + name + ".py"
        print("Creating file " + fullName)
        f = open(fullName, "w+")
        f.close()


if __name__ == "__main__":
    main()
