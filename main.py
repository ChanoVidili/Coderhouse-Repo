# git config --global user.name "Chano Vidili"   // Para configurar tu nombre de usuario en git
# git config --global user.email "chanovidili@gmail.com"   // Para configurar tu email en git
# git config --list
# :q    // Para salir de ese menú de listado de configuraciones
# git config user.name      // Para verlo y así con cq otro.

# Working area --git add--> Stage area -- git commit -m "Comentario" --> Repository

# git init      // Crear repositorio vacío
# git status    // 
# git add main.py  || git add .  (para agregar todos los archivos que esten en la working area: Untracked)
# git log       // Para listar los cambios que hemos hecho en el repo. Desde el más reciente hasta el último

# git remote add origin https:://github.com/chanovidili/Coderhouse-Repo.git
#               // Para linkear el repositorio remoto con el local que ya teníamos.
# git branch -M main    // Cada vez que github cree una rama que llame master la cambie por main (recomendación de github)

# …or create a new repository on the command line
# echo "# Prueba" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/ChanoVidili/Prueba.git
# git push -u origin main

# git push      // Luego solo git push sin origin para subir al main del repo

def imprimir_hola():
    print("HOLA")
