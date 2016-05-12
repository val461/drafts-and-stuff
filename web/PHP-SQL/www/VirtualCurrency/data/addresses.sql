-- phpMyAdmin SQL Dump
-- version 4.3.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 03, 2015 at 09:00 PM
-- Server version: 10.0.14-MariaDB
-- PHP Version: 5.6.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `virtualcurrency`
--

-- --------------------------------------------------------

--
-- Table structure for table `addresses`
--

CREATE TABLE IF NOT EXISTS `addresses` (
  `id` int(10) unsigned NOT NULL,
  `amount` float NOT NULL DEFAULT '0',
  `secret` varchar(255) NOT NULL,
  `shares` int(11) NOT NULL DEFAULT '-1'
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `addresses`
--
DELETE FROM `addresses`;
INSERT INTO `addresses` (`id`, `amount`, `secret`, `shares`) VALUES
(1, 20, '7694f4a66316e53c8cdd9d9954bd611d', -1),
(2, 16, 'e1671797c52e15f763380b45e841ec32', -1),
(9, 12, '8a1e31ba29e83db758f41272e688db00', -1),
(10, 10, '9cbcac6391a48c9dac9eb674f6c7387b', 2),
(11, 10, '1b6d89d82f7d7bbf462d8a43760ea2c2', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addresses`
--
-- TABLE `addresses`
--  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addresses`
--
--ALTER TABLE `addresses`
--  MODIFY `id` int(10) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
