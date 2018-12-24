
def main():

    fileNames = [
"155_PipesGame",
"156_Game2048",
"157_SnakeGame",
"158_TetrisGame",
"159_PyraminxPuzzle",
"160_LinesGame",
"161_Fractal",
"162_TimeASCIIRepresentation",]

    directory = "arcade/python/arcade-theCore/19_CliffsOfPain/"

    for name in fileNames:
        fullName = directory + name + ".py"
        print("Creating file " + fullName)
        f = open(fullName, "w+")
        f.close()


if __name__ == "__main__":
    main()
