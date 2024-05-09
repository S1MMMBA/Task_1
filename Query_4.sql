SELECT sub.id,sub.name
FROM (
		SELECT r.id,r.name,COUNT(DISTINCT s.sex) AS quantity
		FROM rooms r JOIN students s
		ON r.id = s.room
		GROUP BY r.id,r.name
	 ) AS sub
WHERE quantity = 2

