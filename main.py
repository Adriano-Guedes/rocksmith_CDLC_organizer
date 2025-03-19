from pathlib import Path
from functions import *
from config import *

createdFoldersNames = createFolders(ARTISTS_FOLDERS, BASE_PATH)
scanDirectory(BASE_PATH, createdFoldersNames)
