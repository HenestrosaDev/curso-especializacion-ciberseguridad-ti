#!/bin/bash

LOG_FILE="/Users/macbook/Projects/Educacion/curso-especializacion-ciberseguridad-ti/bastionado_de_redes_y_sistemas/u7/tarea/archivos/2_analisis_de_datos/logs/access.log"

# Lista de herramientas a buscar
TOOLS=(
    "Nmap Scripting Engine"
    "Mozilla/5.0 (Hydra)"
    "sqlmap/1.5.2#stable (http://sqlmap.org)"
)

# Iterar sobre cada herramienta y procesar el log
for TOOL in "${TOOLS[@]}"; do
    echo -e "\n==== Endpoints escaneados por $TOOL ===="
    grep "$TOOL" "$LOG_FILE" | awk -F'"' '{print $2}' | sort | uniq -c | sort -nr
done