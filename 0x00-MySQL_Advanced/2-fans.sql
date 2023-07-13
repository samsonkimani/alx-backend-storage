-- create a temporary table

CREATE TEMPORARY TABLE brand_ranking AS (
	SELECT origin, SUM(fans) as total_fans
	FROM metal_bands
	GROUP BY origin
	ORDER BY total_fans DESC
);

SELECT origin, total_fans FROM brand_ranking;
