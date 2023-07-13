-- creating an sql file to that gets the lifetime of a band
CREATE TEMPORARY TABLE glam_rock_bands AS (
  SELECT band_name, 2022 - formed AS lifespan
  FROM metal_bands
  WHERE FIND_IN_SET('Glam rock', style) > 0
);

-- Select and display the rankings
SELECT band_name, lifespan
FROM glam_rock_bands
ORDER BY lifespan DESC
