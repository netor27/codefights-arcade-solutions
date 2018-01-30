
def main():

    fileNames = ["106_Sudoku"
,"107_Minesweeper"
,"108_Box Blur"
,"109_Contours Shifting"
,"110_Polygon Perimeter"
,"111_Gravitation"
,"112_Is Information Consistent"
,"113_Correct Nonogram"]

    directory = "arcade/python/arcade-theCore/13_WaterfallOfIntegration/"

    for name in fileNames:
        fullName = directory + name + ".py"
        print("Creating file " + fullName)
        f = open(fullName, "w+")
        f.close()


if __name__ == "__main__":
    main()
