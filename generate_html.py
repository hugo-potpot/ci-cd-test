import os

# Dossier contenant les images
image_folder = 'images'

# Liste des fichiers dans le dossier
images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# Génération du contenu HTML
html_content = '''<html>
<head>
    <title>Liste des images</title>
</head>
<body>
    <h1>Liste des images</h1>
    <ul>
'''

for image in images:
    html_content += f'        <li><img src="{image_folder}/{image}" alt="{image}" /></li>\n'

html_content += '''    </ul>
</body>
</html>
'''

# Écriture du contenu HTML dans un fichier
with open('index.html', 'w') as f:
    f.write(html_content)

print("Page HTML générée avec succès.")