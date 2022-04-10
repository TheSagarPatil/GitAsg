-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2022 at 07:33 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `app1`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user`
--

CREATE TABLE `tbl_user` (
  `PHONE_NUMBER` varchar(24) NOT NULL,
  `PASSWORD` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_user`
--

INSERT INTO `tbl_user` (`PHONE_NUMBER`, `PASSWORD`) VALUES
('1234', '*4AD47E08DAE2BD4F0977EED5D23DC901359DF617'),
('12345', '*4AD47E08DAE2BD4F0977EED5D23DC901359DF617'),
('1235', '*4AD47E08DAE2BD4F0977EED5D23DC901359DF617'),
('1236', '*4AD47E08DAE2BD4F0977EED5D23DC901359DF617'),
('1237', '*00A51F3F48415C7D4E8908980D443C29C69B60C9');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user_roles`
--

CREATE TABLE `tbl_user_roles` (
  `ROLE` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_user_roles`
--

INSERT INTO `tbl_user_roles` (`ROLE`) VALUES
('DELETE'),
('READ'),
('SOMETHING'),
('UPDATE');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user_userroles`
--

CREATE TABLE `tbl_user_userroles` (
  `PHONE_NUMBER` varchar(24) NOT NULL,
  `ROLE` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_user_userroles`
--

INSERT INTO `tbl_user_userroles` (`PHONE_NUMBER`, `ROLE`) VALUES
('1234', 'UPDATE'),
('1234', 'READ'),
('12345', 'READ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_user`
--
ALTER TABLE `tbl_user`
  ADD PRIMARY KEY (`PHONE_NUMBER`);

--
-- Indexes for table `tbl_user_roles`
--
ALTER TABLE `tbl_user_roles`
  ADD PRIMARY KEY (`ROLE`);

--
-- Indexes for table `tbl_user_userroles`
--
ALTER TABLE `tbl_user_userroles`
  ADD KEY `PHONE_NUMBER` (`PHONE_NUMBER`),
  ADD KEY `FK_role` (`ROLE`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbl_user_userroles`
--
ALTER TABLE `tbl_user_userroles`
  ADD CONSTRAINT `FK_role` FOREIGN KEY (`ROLE`) REFERENCES `tbl_user_roles` (`ROLE`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tbl_user_userroles_ibfk_1` FOREIGN KEY (`PHONE_NUMBER`) REFERENCES `tbl_user` (`PHONE_NUMBER`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
