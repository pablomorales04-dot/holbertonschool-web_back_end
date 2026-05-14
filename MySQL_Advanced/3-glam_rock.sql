-- Script que lista todas las bandas con Glam rock como su estilo principal
-- Calculando la longevidad hasta el año 2024
SELECT band_name, (IFNULL(split, 2024) - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;


