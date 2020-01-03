import numpy as np

def importText(file_name, encoding="utf8"):
    array = []
    with open(file_name, "r", encoding=encoding) as infile:
        for line in infile:
            array.append(line.strip())
    return array

def writeText(name, array, encoding="utf8"):
    file = open(name, "w", encoding=encoding)
    for i in range(len(array)):
        file.write(str(array[i]) + "\n")
    file.close()

file_name = "nintendo ds"
path = "data/"

snes = importText(path+"html/"+file_name+".txt")

titles = []

for i in range(len(snes)):

    # If this is a row of text with a title in it
    if "|''[[" in snes[i]:

        # Get the start of the title
        startpoint = 0
        for j in range(len(snes[i])):
            if snes[i][j:j+5] == "|''[[":
                startpoint = j+5

        # Get the end of the title
        endpoint = 0
        for j in range(len(snes[i])):
            if snes[i][j:j+4] == "]]''":
                endpoint = j

        # Get the title
        title = snes[i][startpoint:endpoint]

        # Remove Japanese titles
        title = title.split("|")[0]

        # Remove (video game) metadata
        title = title.split("(")[0]
        title = title.split("#")[0]

        print(title)
        titles.append(title)

# Remove duplicate titles
titles = np.unique(titles)

writeText(path+"output/"+file_name+"_clean.txt", titles)