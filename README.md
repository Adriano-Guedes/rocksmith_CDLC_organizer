📌 Versão em Português

O script funciona da seguinte forma:
Criação das pastas → Ele cria uma pasta para cada artista definido na configuração do script.
Varredura de arquivos → O script percorre todas as pastas e subpastas, verificando se o nome de cada arquivo contém alguma correspondência com os nomes dos artistas definidos anteriormente.
Movimentação de arquivos → Se houver correspondência, o arquivo é movido para a pasta do respectivo artista.
Se nenhum artista compatível for encontrado, o arquivo será movido para uma pasta especial destinada às CDLCs sem artista definido.

Configuração (config.py):
BASE_PATH → Caminho onde todas as CDLCs estão armazenadas.
ARTISTS_FOLDERS → Lista com os nomes dos artistas, que serão usados tanto para criar as pastas quanto para comparar com os nomes dos arquivos.
Após definir essas configurações, basta executar o script no terminal e aguardar até que ele conclua a organização dos arquivos.



📌 English Version

The script works as follows:
Folder creation → It creates a folder for each artist defined in the script configuration.
File scanning → The script scans all folders and subfolders, checking if each file name matches any of the predefined artist names.
File sorting → If a match is found, the file is moved to the corresponding artist's folder. If no matching artist is found, the file is placed in a special folder for CDLCs without an assigned artist.

Configuration (config.py):
BASE_PATH → The directory where all CDLCs are stored.
ARTISTS_FOLDERS → A list of artist names, which will be used both for folder creation and file name comparison.
Once these settings are defined, simply run the script in the terminal and wait for it to complete the file organization process.
