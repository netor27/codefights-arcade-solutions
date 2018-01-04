
def main():

    fileNames = ["080_CharacterParity", "081_ReflectString", "082_NewNumeralSystem", "083_Cipher26",
                 "084_StolenLunch", "085_HigherVersion", "086_Decipher", "087_AlphanumericLess"]

    directory = "./python/arcade-theCore/10_LabOfTransformations/"

    for name in fileNames:
        fullName = directory + name + ".py"
        print("Creating file " + fullName)
        f = open(fullName, "w+")
        f.close()


if __name__ == "__main__":
    main()
