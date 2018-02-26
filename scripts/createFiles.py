
def main():

    fileNames = ["122_BishopandPawn"
,"123_ChessKnightMoves"
,"124_BishopDiagonal"
,"125_WhoseTurn"
,"126_ChessBishopDream"
,"127_ChessTriangle"
,"128_AmazonCheckmate"
,"129_PawnRace"]

    directory = "arcade/python/arcade-theCore/15_ChessTavern/"

    for name in fileNames:
        fullName = directory + name + ".py"
        print("Creating file " + fullName)
        f = open(fullName, "w+")
        f.close()


if __name__ == "__main__":
    main()
