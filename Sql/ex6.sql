SELECT 
    e.title AS event_title,
    COUNT(r.resource_id) AS total_resources
FROM Events e
JOIN Resources r
    ON e.event_id = r.event_id
GROUP BY e.event_id, e.title;