SELECT r.id, r.name,CAST (AVG(EXTRACT(YEAR FROM NOW()) - EXTRACT(YEAR FROM s.birthday)) AS INTEGER) AS avgAge
FROM rooms r JOIN students s ON r.id = s.room
GROUP BY r.id, r.name
ORDER BY avgAge 
LIMIT 5;
