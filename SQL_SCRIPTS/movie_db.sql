-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: moviedb
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `members`
--

CREATE DATABASE IF NOT EXISTS moviedb;
USE moviedb;

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members` (
  `id` int NOT NULL,
  `first_name` text,
  `last_name` text,
  `movie_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (1,'Adam','Smith',1),(2,'Rasi','Kumar',2),(3,'Susan','Davidson',5),(4,'Jenny','Adrianna',8),(7,'Adam','John',2),(8,'Hemn','Barzan',1),(9,'John','Sara',1),(11,'Maili','Li',1);
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--


DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `id` int DEFAULT NULL,
  `title` text,
  `category` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'ASSASSIN\'S CREED: EMBERS','Animations'),(2,'Real Steel(2012)','Animations'),(3,'Alvin and the Chipmunks','Animations'),(4,'The Adventures of Tin Tin','Animations'),(5,'Safe (2012)','Action'),(6,'Safe House(2012)','Action'),(7,'GIA','18+'),(8,'Deadline 2009','18+'),(9,'The Dirty Picture','18+'),(10,'Marley and me','Romance'),(11,'Matrix','Action');
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-06 13:07:51


/* in class code */
SELECT * FROM MOVIES;
SELECT * FROM MEMBERS;

SELECT * FROM MOVIES CROSS JOIN members;

SELECT members.first_name, members.last_name, movies.title
FROM members, movies
WHERE movies.ID = members.MOVIE_ID; -- INNER JOIN

-- LEFT OUTER JOIN
SELECT A.TITLE, B.FIRST_NAME, B.LAST_NAME
FROM movies AS A 
LEFT JOIN members AS B
ON B.MOVIE_ID = A.ID;


-- right outer JOIN
SELECT A.FIRST_NAME, A.LAST_NAME, B.TITLE
FROM members AS A 
RIGHT JOIN movies AS B
ON B.ID - A.MOVIE_ID;


