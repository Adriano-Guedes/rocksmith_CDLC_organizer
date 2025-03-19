from pathlib import Path
from typing import List
import re
import unicodedata
import shutil
from config import *

baseMainPath = BASE_PATH
unknownArtistPath = BASE_PATH + "/UnknownArtist"


def scanDirectory(path: str, nameExistingFolders: List[str]):
    folder = Path(path)
    for f in folder.iterdir():
        if(f.is_dir()):
            scanDirectory(path + '/' + f.name, nameExistingFolders)
        elif(f.is_file() and f.name.endswith(".psarc")):
            artistFound = False
            for fold in nameExistingFolders:
                if(fileNameMathFolderName(f.name, fold)):
                    moveToFolder(path + '/' + f.name, baseMainPath + '/' + fold)
                    artistFound = True
            if artistFound == False:
                moveToFolder(path + '/' + f.name, unknownArtistPath)


def fileNameMathFolderName(fileName, folderName):
    fileName = removeAccents(fileName)
    pattern = r"\s*".join([re.escape(c) + r"\s*[._,-]*" for c in folderName.lower()])
    return bool(re.search(pattern, fileName, re.IGNORECASE))

def transformTextToCaptalizeAndJoin(text: str) -> str:
    cleanText = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    words = cleanText.split()
    capitalizedWords = [word.capitalize() for word in words]
    return ''.join(capitalizedWords)

def removeAccents(text: str) -> str:
    normalizedText = unicodedata.normalize('NFD', text)
    
    unaccentedText = ''.join(
        c for c in normalizedText if unicodedata.category(c) != 'Mn'
    )
    
    return unaccentedText

def moveToFolder(strFilePath: str, strFolderPath: str):
    filePath = Path(strFilePath)
    folderPath = Path(strFolderPath)
    
    if filePath.exists() and folderPath.exists():
        if not (folderPath / filePath.name).exists():
            shutil.move(filePath, folderPath)
            print(f"   -File moved successfully")

def createFolders(foldersNames: List[str], foldersCreationPath: str):
    formatedFoldersNames = []

    unknownArtistPath = Path(foldersCreationPath) / "UnknownArtist"
    if not unknownArtistPath.exists():
        Path(unknownArtistPath).mkdir(parents=True)

    for name in foldersNames:
        formatedFolderName = transformTextToCaptalizeAndJoin(name)
        newDir = Path(foldersCreationPath) / formatedFolderName
        if not newDir.exists():
            Path(newDir).mkdir(parents=True)
        formatedFoldersNames.append(formatedFolderName)
    return formatedFoldersNames