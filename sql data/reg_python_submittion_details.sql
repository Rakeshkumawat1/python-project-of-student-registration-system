CREATE DATABASE  IF NOT EXISTS `reg_python` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `reg_python`;
-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: localhost    Database: reg_python
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `submittion_details`
--

DROP TABLE IF EXISTS `submittion_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `submittion_details` (
  `id` int(10) DEFAULT NULL,
  `Full_name` varchar(30) DEFAULT NULL,
  `Contact_No` varchar(12) DEFAULT NULL,
  `Branch` varchar(15) DEFAULT NULL,
  `clgid` varchar(10) DEFAULT NULL,
  `Upi` varchar(20) DEFAULT NULL,
  `Amount` int(10) DEFAULT NULL,
  `Date_Of_Submittion` varchar(10) DEFAULT NULL,
  `payment_option` varchar(30) DEFAULT NULL,
  `codsubid` int(3) DEFAULT NULL,
  `submittionid` varchar(10) DEFAULT NULL,
  `Date_Of_Confirmation` varchar(10) DEFAULT NULL,
  `Confirmed` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `submittion_details`
--

LOCK TABLES `submittion_details` WRITE;
/*!40000 ALTER TABLE `submittion_details` DISABLE KEYS */;
INSERT INTO `submittion_details` VALUES (1,'default','0','default','2016ucs000','default',0,'00-00-2019','default',111,'18GECJR111','00-00-2019','yes'),(NULL,'Rakesh','8503875941',' C S ','2016ucs033','1100',38500,'19/03/19','DD',112,'18GECJR112',NULL,NULL);
/*!40000 ALTER TABLE `submittion_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-31 13:03:55
