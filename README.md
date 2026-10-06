
# Clases de águila y python 

## de variables hasta estructura de datos 

# Git y GitHub — Comandos básicos

## Configuración

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```
```python
print("hola mundo")
def saludar()
    print("Saludando")
```

## Crear repositorio

```bash
git init
git status
```

## Guardar cambios

```bash
git add .
git commit -m "Descripción del cambio"
```

## Conectar con GitHub

```bash
git remote add origin https://github.com/usuario/proyecto.git
git branch -M main
git push -u origin main
```

## Actualizar repositorio

```bash
git pull
git push
```

## Clonar repositorio

```bash
git clone https://github.com/usuario/proyecto.git
cd proyecto
```

## Ramas

```bash
# Ver ramas
git branch

# Crear y cambiar de rama
git switch -c desarrollo

# Cambiar de rama
git switch main

# Fusionar rama
git merge desarrollo

# Subir rama
git push -u origin desarrollo
```

## Historial

```bash
git log --oneline
```

## Deshacer cambios

```bash
# Ver diferencias
git diff

# Restaurar archivo
git restore archivo.py

# Quitar archivo del staging
git restore --staged archivo.py
```

## Flujo básico

```bash
git pull
git status
git add .
git commit -m "Nuevo cambio"
git push
```

## Comandos principales

| Comando      | Función            |
| ------------ | ------------------ |
| `git init`   | Crear repositorio  |
| `git clone`  | Clonar repositorio |
| `git status` | Ver estado         |
| `git add .`  | Preparar cambios   |
| `git commit` | Guardar cambios    |
| `git push`   | Subir cambios      |
| `git pull`   | Descargar cambios  |
| `git branch` | Ver ramas          |
| `git switch` | Cambiar de rama    |
| `git merge`  | Fusionar ramas     |
| `git log`    | Ver historial      |
