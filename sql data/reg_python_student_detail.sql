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
-- Table structure for table `student_detail`
--

DROP TABLE IF EXISTS `student_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `student_detail` (
  `id` int(10) DEFAULT NULL,
  `First_Name` varchar(25) DEFAULT NULL,
  `Last_Name` varchar(25) DEFAULT NULL,
  `Fathers_Name` varchar(25) DEFAULT NULL,
  `Mothers_Name` varchar(25) DEFAULT NULL,
  `DOB` varchar(10) DEFAULT NULL,
  `Contact_No_self` varchar(12) DEFAULT NULL,
  `Contact_No_Parents` varchar(12) DEFAULT NULL,
  `Semester` int(3) DEFAULT NULL,
  `Course` varchar(8) DEFAULT NULL,
  `Branch` varchar(15) DEFAULT NULL,
  `Year` int(4) DEFAULT NULL,
  `College_Id` varchar(10) DEFAULT NULL,
  `Roll_No` varchar(15) DEFAULT NULL,
  `Enrollment_No` varchar(15) DEFAULT NULL,
  `Adderss_Of_Correspondence` varchar(250) DEFAULT NULL,
  `Permenent_Adderss` varchar(250) DEFAULT NULL,
  `Local_Gardain_In_Jhalawar_Jhalarapatan` varchar(250) DEFAULT NULL,
  `Type_Of_Payment` varchar(25) DEFAULT NULL,
  `Gender` varchar(7) DEFAULT NULL,
  `Original_Category` varchar(10) DEFAULT NULL,
  `Email` varchar(30) DEFAULT NULL,
  `Religon` varchar(10) DEFAULT NULL,
  `Blood_Group` varchar(5) DEFAULT NULL,
  `Marital_Status` varchar(10) DEFAULT NULL,
  `Cast` varchar(10) DEFAULT NULL,
  `Amount` int(10) DEFAULT NULL,
  `upi_challen_No` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_detail`
--

LOCK TABLES `student_detail` WRITE;
/*!40000 ALTER TABLE `student_detail` DISABLE KEYS */;
INSERT INTO `student_detail` VALUES (NULL,'Rakesh','kumawat','Ramgopal kumawat','Teeja devi','19/03/19','8503875941','9414518092',4,' B.tech ',' C S ',2019,'2016ucs033','2016ucs033','000000000000000','yes','yes','yes','DD','Male','OBC','rk@gmail.com','jj','jj','jjj','jjj',38500,'1100');
/*!40000 ALTER TABLE `student_detail` ENABLE KEYS */;
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
