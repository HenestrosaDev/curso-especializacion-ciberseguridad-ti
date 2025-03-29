#!/bin/bash

# Archivo de entrada con las IPs únicas
input_file="unique_src_ips.txt"

# Archivo de salida con la geolocalización
output_file="geolocalized_ips.csv"

# Encabezado del archivo CSV
echo "IP,País" > "$output_file"

# Itera sobre cada IP en el archivo de entrada
while IFS= read -r ip; do
    # Obtiene la información de la IP de WHOIS y extrae el país
    country=$(whois "$ip" | grep -iE "country" | head -n 1 | awk '{print $2}')
    
    # Si no se encuentra el país, poner "Desconocido"
    country=${country:-Desconocido}

    # Guarda el contenido en el archivo CSV
    echo "$ip,$country" >> "$output_file"

    # Muestra el progreso en pantalla
    echo "Procesado: $ip -> $country"

    # Espera 1 segundo para evitar bloqueos de WHOIS
    sleep 1
done < "$input_file"

echo "✅ Proceso completado. Datos guardados en $output_file."