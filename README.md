# ZKING v1.0 🚀

**Zking** es una herramienta de auditoría de seguridad y análisis de vulnerabilidades en línea de comandos (CLI) diseñada para escanear carpetas de proyectos, identificar patrones sospechosos (credenciales expuestas, tokens, llaves) y generar reportes automatizados utilizando Inteligencia Artificial local.

---

## 🔥 Características Principales

* **Escaneo Masivo:** Explora directorios de forma dinámica filtrando archivos por extensiones específicas (`.py`, `.txt`, `.log`) y omitiendo entornos virtuales (`venv/`).
* **Análisis con IA Local:** Integra un modelo local (`gemma4`) para analizar líneas sospechosas en tiempo real y aportar consejos de mitigación sin enviar datos a la nube.
* **Criptografía (Huella Digital):** Genera un Hash básico basado en el contenido ASCII de cada archivo para garantizar la integridad y el control de cambios (identificando el efecto avalancha).
* **Persistencia de Datos (Logs):** Automatiza la creación de un archivo de registro (`reporte_auditoria.txt`) donde respalda todas las alertas, hashes y consejos de la IA.
* **Arquitectura Modular:** Código limpio y ordenado separado en módulos especializados (`crypto`, `analyzer`, `scanner`, `ai_analyzer`).

---

## 🛠️ Tecnologías Utilizadas

* **Python 3** (Lógica principal, manejo de archivos y criptografía)
* **Ollama / Gemma4** (Motor de Inteligencia Artificial local)
* **Arch Linux** (Entorno de desarrollo y pruebas)
* **Git & GitHub** (Control de versiones)

---

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone [https://github.com/EsleiderMeza/Zking.git](https://github.com/EsleiderMeza/Zking.git)
cd Zking

### 2. Configurar el Entorno
Asegúrate de tener tu entorno virtual activo y las dependencias de tu IA local configuradas.

### 3. Ejecutar la Herramienta
python zking.py
