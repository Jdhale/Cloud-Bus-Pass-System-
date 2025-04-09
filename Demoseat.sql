-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: demoseat
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `bus_location`
--

DROP TABLE IF EXISTS `bus_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bus_location` (
  `bus_id` int NOT NULL,
  `latitude` decimal(9,6) DEFAULT NULL,
  `longitude` decimal(9,6) DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`bus_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bus_location`
--

LOCK TABLES `bus_location` WRITE;
/*!40000 ALTER TABLE `bus_location` DISABLE KEYS */;
INSERT INTO `bus_location` VALUES (1,19.076000,72.877700,'2025-03-30 13:01:29');
/*!40000 ALTER TABLE `bus_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bus_passes`
--

DROP TABLE IF EXISTS `bus_passes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bus_passes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `route` varchar(100) NOT NULL,
  `validity` date NOT NULL,
  `issued_on` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bus_passes`
--

LOCK TABLES `bus_passes` WRITE;
/*!40000 ALTER TABLE `bus_passes` DISABLE KEYS */;
INSERT INTO `bus_passes` VALUES (1,'123456','Janhvi','Route A','2025-06-01','2025-03-28');
/*!40000 ALTER TABLE `bus_passes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emer_table`
--

DROP TABLE IF EXISTS `emer_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emer_table` (
  `seat_number` int NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`seat_number`),
  CONSTRAINT `emer_table_chk_1` CHECK ((`status` in (_utf8mb4'available',_utf8mb4'unavailable')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emer_table`
--

LOCK TABLES `emer_table` WRITE;
/*!40000 ALTER TABLE `emer_table` DISABLE KEYS */;
INSERT INTO `emer_table` VALUES (1,'available'),(2,'available'),(3,'available'),(4,'unavailable'),(5,'available');
/*!40000 ALTER TABLE `emer_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table0`
--

DROP TABLE IF EXISTS `table0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table0` (
  `seatno` int NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  `enroll` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`seatno`),
  CONSTRAINT `table0_chk_1` CHECK ((`status` in (_utf8mb4'available',_utf8mb4'seat booked')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table0`
--

LOCK TABLES `table0` WRITE;
/*!40000 ALTER TABLE `table0` DISABLE KEYS */;
INSERT INTO `table0` VALUES (1,'seat booked','ENR001'),(2,'available',NULL),(3,'available',NULL),(4,'seat booked','ENR001'),(5,'available',NULL);
/*!40000 ALTER TABLE `table0` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table1`
--

DROP TABLE IF EXISTS `table1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table1` (
  `seatno` int NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  `enroll` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`seatno`),
  CONSTRAINT `table1_chk_1` CHECK ((`status` in (_utf8mb4'available',_utf8mb4'seat booked')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table1`
--

LOCK TABLES `table1` WRITE;
/*!40000 ALTER TABLE `table1` DISABLE KEYS */;
INSERT INTO `table1` VALUES (1,'available',NULL),(2,'seat booked','ENR001'),(3,'available',NULL),(4,'seat booked','ENR001'),(5,'available',NULL);
/*!40000 ALTER TABLE `table1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table2`
--

DROP TABLE IF EXISTS `table2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table2` (
  `seatno` int NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  `enroll` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`seatno`),
  CONSTRAINT `table2_chk_1` CHECK ((`status` in (_utf8mb4'available',_utf8mb4'seat booked')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table2`
--

LOCK TABLES `table2` WRITE;
/*!40000 ALTER TABLE `table2` DISABLE KEYS */;
INSERT INTO `table2` VALUES (1,'seat booked','ENR002'),(2,'seat booked','ENR004'),(3,'available',NULL),(4,'available',NULL),(5,'seat booked','ENR001');
/*!40000 ALTER TABLE `table2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table3`
--

DROP TABLE IF EXISTS `table3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table3` (
  `seatno` int NOT NULL,
  `status` varchar(50) DEFAULT NULL,
  `enroll` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`seatno`),
  CONSTRAINT `table3_chk_1` CHECK ((`status` in (_utf8mb4'available',_utf8mb4'seat booked')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table3`
--

LOCK TABLES `table3` WRITE;
/*!40000 ALTER TABLE `table3` DISABLE KEYS */;
INSERT INTO `table3` VALUES (1,'available',NULL),(2,'seat booked','ENR003'),(3,'seat booked','ENR004'),(4,'available',NULL),(5,'available',NULL);
/*!40000 ALTER TABLE `table3` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-09 12:07:14
