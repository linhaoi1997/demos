-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: learning_logs_test
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `learning_logs_topic`
--

DROP TABLE IF EXISTS `learning_logs_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `learning_logs_topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(30) NOT NULL,
  `date_added` datetime(6) NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `learning_logs_topic_owner_id_67ecce32_fk_auth_user_id` (`owner_id`),
  CONSTRAINT `learning_logs_topic_owner_id_67ecce32_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learning_logs_topic`
--

LOCK TABLES `learning_logs_topic` WRITE;
/*!40000 ALTER TABLE `learning_logs_topic` DISABLE KEYS */;
INSERT INTO `learning_logs_topic` VALUES (1,'Chess','2019-12-13 05:49:26.323257',1),(2,'Rock Climbing','2019-12-13 05:49:53.620038',1),(3,'django注意的坑','2019-12-14 01:54:16.453415',1),(5,'test','2019-12-24 06:40:06.106470',1);
/*!40000 ALTER TABLE `learning_logs_topic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `learning_logs_entry`
--

DROP TABLE IF EXISTS `learning_logs_entry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `learning_logs_entry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `date_added` datetime(6) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `describe` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `learning_logs_entry_topic_id_83697a9a_fk_learning_logs_topic_id` (`topic_id`),
  CONSTRAINT `learning_logs_entry_topic_id_83697a9a_fk_learning_logs_topic_id` FOREIGN KEY (`topic_id`) REFERENCES `learning_logs_topic` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learning_logs_entry`
--

LOCK TABLES `learning_logs_entry` WRITE;
/*!40000 ALTER TABLE `learning_logs_entry` DISABLE KEYS */;
INSERT INTO `learning_logs_entry` VALUES (1,'The opening is the first part of the game ,roughly the first ten moves or so. In the opening, it\'s a good idea to do three things - bring out your bishops and knights, try to control the center of  the board, and castle your king','2019-12-13 14:24:05.792450',1,'describe'),(2,'In the opening phase of the game, it\'s important to bring out your bishops and knights. These pieces are powerful and maneuverable enough to play a significant role in the beginning moves of a game','2019-12-13 14:26:44.306346',1,''),(7,'使用国内镜像避免下载速度太慢的问题 \r\npip install -i https://pypi.tuna.tsinghua.edu.cn/simple gevent','2019-12-16 13:50:40.395332',3,'');
/*!40000 ALTER TABLE `learning_logs_entry` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-26 15:23:24
