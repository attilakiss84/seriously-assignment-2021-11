-- Average waiting time per passenger
SELECT
    AVG(TIMEDIFF(entered_at, arrived_at)) AS average_waiting_time
FROM passenger_journeys
;

-- Average waiting time
SELECT
    AVG(TIMEDIFF(left_at, entered_at)) AS average_journey_time
FROM passenger_journeys
;

-- Distance covered by elevators
-- My goal would be to somehow attempt to balance the workload
SELECT
	elevator_id,
	SUM(ABS(floor_from - floor_to)) AS distance_covered
FROM elevator_moves
GROUP BY elevator_id
;

-- Move rate for passenger journeys
-- As an elevator algorithm developer would be to minimize this ratio
SELECT
    pj.elevator_id AS elevator_id,
    CASE
    	WHEN pj.passenger_distance_covered IS NULL THEN 0
    	ELSE pj.passenger_distance_covered / em.elevator_distance_covered
    END AS useful_distance_rate
FROM
    (
        SELECT
            elevator_id,
            SUM(ABS(floor_from - floor_to)) AS passenger_distance_covered
        FROM passenger_journeys
        GROUP BY elevator_id
    ) pj
    LEFT JOIN (
        SELECT
            elevator_id,
            SUM(ABS(floor_from - floor_to)) AS elevator_distance_covered
        FROM elevator_moves
        GROUP BY elevator_id
    ) em
        ON em.elevator_id = pj.elevator_id
;