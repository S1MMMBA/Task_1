SELECT r.name,COUNT(s.id)
FROM rooms r LEFT JOIN students s
ON r.id = s.room
GROUP BY r.name