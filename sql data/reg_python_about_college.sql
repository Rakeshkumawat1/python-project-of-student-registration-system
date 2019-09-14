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
-- Table structure for table `about_college`
--

DROP TABLE IF EXISTS `about_college`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `about_college` (
  `undertaking` varchar(1500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `about_college`
--

LOCK TABLES `about_college` WRITE;
/*!40000 ALTER TABLE `about_college` DISABLE KEYS */;
INSERT INTO `about_college` VALUES ('I promise to abide by all the rules and regulations of the college and University in force presently as well\n as those that may be made / modified from time to time. I hereby also certify that entries made by me in this\n form are correct to the best of my knowledge and have deposited fee for the current semester by Challan/Receipt\n \n (1) I have carefully read and fully understood the law prohibiting ragging and the direction of the supreme \n     court and the Center/State Government in this regard \n (2) I have received a copy of the UGS/MHRD/AICTE Regulations on curbing the Menace of Ragging \n	in Higher Edication Institutions 2009, and have carefully gone through it. \n (3) I hereby undertake that \n    (i) I will not indulge in any behavior act that may come under the definition of ragging. \n    (ii) I will not participate in or abet or propagate ragging in any from. \n   (iii) I will not hurt anyone physically or psychologically or cause any other harm. \n (4) I hereby agree that if found guilty of any aspect of ragging, I may be punished as per \n    the provisions of the UGC/MHRD/AICTE Regulations mentioned above and/or as per the law in force. \n (5) I hereby affirm that I have not been expelled or debarred from admission by any institution.\n                      ');
/*!40000 ALTER TABLE `about_college` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-31 13:03:54
