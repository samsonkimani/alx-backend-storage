-- create a temporary table

CREATE TEMPORARY TABLE brand_ranking AS (
	SELECT origin, SUM(fans) as nb_fans
	FROM metal_bands
	GROUP BY origin
	ORDER BY nb_fans DESC
);

SELECT origin, nb_fans FROM brand_ranking;
