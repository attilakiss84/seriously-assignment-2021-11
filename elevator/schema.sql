DROP TABLE IF EXISTS `elevators`;
CREATE TABLE `elevators` (
  `id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `elevators_UN` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `elevator_moves`;
CREATE TABLE `elevator_moves` (
  `elevator_id` smallint unsigned NOT NULL,
  `floor_from` smallint NOT NULL,
  `departed_at` datetime NOT NULL,
  `floor_to` smallint NOT NULL,
  `arrived_at` datetime NOT NULL,
  `people_in` smallint unsigned NOT NULL DEFAULT '0',
  `people_out` smallint unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`elevator_id`,`depart_at`),
  CONSTRAINT `elevator_moves_FK` FOREIGN KEY (`elevator_id`) REFERENCES `elevators` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `passenger_journeys`;
CREATE TABLE `passenger_journeys` (
  `elevator_id` smallint unsigned NOT NULL,
  `arrived_at` datetime NOT NULL,
  `entered_at` datetime NOT NULL,
  `left_at` datetime NOT NULL,
  `floor_from` smallint NOT NULL,
  `floor_to` smallint NOT NULL,
  KEY `passenger_journeys_FK` (`elevator_id`),
  CONSTRAINT `passenger_journeys_FK` FOREIGN KEY (`elevator_id`) REFERENCES `elevators` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
