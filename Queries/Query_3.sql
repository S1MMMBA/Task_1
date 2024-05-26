SELECT r.id, r.name, CAST (MAX(EXTRACT(YEAR FROM NOW()) - EXTRACT(YEAR FROM s.birthday)) -
					 MIN(EXTRACT(YEAR FROM NOW()) - EXTRACT(YEAR FROM s.birthday)) AS INTEGER) AS Diff
FROM rooms r JOIN students s
ON r.id = s.room
GROUP BY r.id,r.name
ORDER BY Diff DESC
LIMIT 5