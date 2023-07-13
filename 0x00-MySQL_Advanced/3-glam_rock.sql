CREATE TEMPORARY TABLE glam_rock AS(
	SELECT band_name,
	2022 - COALESCE(CAST(SUBSTRING_INDEX(split, '-', 1) AS UNSIGNED), formed) AS lifespan
	FROM metal_bands
	WHERE FIND_IN_SET("Glam rock", style) > 0
);

SELECT band_name, lifespan FROM glam_rock ORDER BY lifespan DESC;
