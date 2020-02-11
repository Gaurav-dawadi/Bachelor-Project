-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 14, 2019 at 08:48 AM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythonmysql`
--

-- --------------------------------------------------------

--
-- Table structure for table `students_profile`
--

CREATE TABLE `students_profile` (
  `id` int(11) NOT NULL,
  `rollno` varchar(15) NOT NULL,
  `name` varchar(55) DEFAULT NULL,
  `phone` varchar(55) DEFAULT NULL,
  `address` varchar(55) DEFAULT NULL,
  `department` varchar(55) DEFAULT NULL,
  `email` varchar(155) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students_profile`
--

INSERT INTO `students_profile` (`id`, `rollno`, `name`, `phone`, `address`, `department`, `email`) VALUES
(1, 'SEC072BEX001', 'Anupam Panta', '9845355888', 'Chitwan', 'Electronics', 'anupam.panta2010@gmail.com'),
(2, 'SEC072BEX014', 'Rishav Raj', '9860458383', 'Rautahat', 'Electronics', 'rishav.raj@sagarmatha.edu.np'),
(3, 'SEC072BEX009', 'Sadikshya Paudel', '9845622231', 'Kalanki', 'Electronics', 'sadumuna@gmail.com'),
(4, 'SEC072BEX007', 'Kushal Marasini', '9843641152', 'Banasthali', 'Electronics', 'kushal.marasini@sagarmatha.edu.np'),
(7, 'SEC072BEX006', 'Gaurab Dawadi', '9843715264', 'Khasi Bazar', 'Electronics', 'gaurab.dawadi@sagarmatha.edu.np'),
(10, 'SEC072BEX002', 'Bikash Dawadi', '9860136025', 'Shukukhola', 'Electronics', 'bikash10manutd@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `teachers_attendance`
--

CREATE TABLE `teachers_attendance` (
  `id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `entry` varchar(50) NOT NULL,
  `exit_time` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teachers_attendance`
--

INSERT INTO `teachers_attendance` (`id`, `teacher_id`, `entry`, `exit_time`, `date`) VALUES
(1, 666, '10:00:28.391476', '17:39:28.391476', '2019-07-31'),
(2, 101, '10:00:28.391476', '17:39:28.391476', '2019-07-31'),
(3, 666, '09:30:28.391476', '18:39:28.391476', '2019-08-01'),
(4, 666, '10:15:28.391476', '18:00:28.391476', '2019-08-02'),
(5, 666, '10:45:28.391476', '17:04:28.391476', '2019-08-03'),
(6, 101, '10:30:28.391476', '18:04:28.391476', '2019-08-03'),
(7, 666, '10:30:28.391476', '17:00:28.391476', '2019-08-04'),
(8, 101, '10:45:28.391476', '17:00:28.391476', '2019-08-04'),
(9, 101, '10:45:28.391476', '17:39:28.391476', '2019-08-05'),
(10, 101, '10:45:28.391476', '18:59:28.391476', '2019-08-06'),
(25, 666, '23:46:52.531415', '23:46:55.011430', '2019-08-07'),
(26, 666, '00:00:20.071186', '00:00:31.996801', '2019-08-08'),
(27, 666, '21:53:20.697560', '21:54:03.025828', '2019-08-09'),
(28, 666, '00:00:52.440197', '00:22:01.107203', '2019-08-10'),
(29, 666, '00:13:48.301253', '00:14:15.095691', '2019-08-11');

-- --------------------------------------------------------

--
-- Table structure for table `teachers_profile`
--

CREATE TABLE `teachers_profile` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `department` varchar(50) NOT NULL,
  `email` varchar(155) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teachers_profile`
--

INSERT INTO `teachers_profile` (`id`, `name`, `phone`, `address`, `department`, `email`) VALUES
(101, 'Bharat Bhatta', '9848474344', 'Baitadi', 'Electronics', 'bharat.bhatta@sagarmatha.edu.np'),
(102, 'Kamal Gautam', '9841482681', 'Butwal', 'Electronics', 'kamal.gautam@sagarmatha.edu.np'),
(103, 'Amit Khanal', '9851140652', 'Baneshwor', 'Electronics', 'amit@sagarmatha.edu.np'),
(104, 'Dil Bahadur Chettri', '9841562337', 'Kalanki', 'Electronics', 'dbc@sagarmatha.edu.np'),
(105, 'Arun Parajuli', '9841271076', 'Pepsicola', 'Civil', 'arun@sagarmatha.edu.np'),
(666, 'Anupam (Admin)', '9845355888', 'Address123', 'Faculty123', 'email123@mail123.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students_profile`
--
ALTER TABLE `students_profile`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `teachers_attendance`
--
ALTER TABLE `teachers_attendance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `teachers_profile`
--
ALTER TABLE `teachers_profile`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students_profile`
--
ALTER TABLE `students_profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `teachers_attendance`
--
ALTER TABLE `teachers_attendance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `teachers_profile`
--
ALTER TABLE `teachers_profile`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=123124;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
