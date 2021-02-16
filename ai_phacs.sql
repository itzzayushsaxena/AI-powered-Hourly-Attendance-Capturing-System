-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 16, 2021 at 08:11 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ai_phacs`
--

-- --------------------------------------------------------

--
-- Table structure for table `assigned_subjects`
--

CREATE TABLE `assigned_subjects` (
  `teacher_id` int(3) NOT NULL,
  `subject_id` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `assigned_subjects`
--

INSERT INTO `assigned_subjects` (`teacher_id`, `subject_id`) VALUES
(4, 7),
(4, 9);

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL,
  `enroll_no` varchar(12) NOT NULL,
  `teacher_id` int(2) NOT NULL,
  `subject_id` int(2) NOT NULL,
  `session_id` int(2) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `day`
--

CREATE TABLE `day` (
  `day_id` int(1) NOT NULL,
  `day` varchar(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `day`
--

INSERT INTO `day` (`day_id`, `day`) VALUES
(1, 'Monday'),
(2, 'Tuesday'),
(3, 'Wednesday'),
(4, 'Thursday'),
(5, 'Friday');

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `depart_id` int(2) NOT NULL,
  `department` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`depart_id`, `department`) VALUES
(5, 'Chemical'),
(6, 'Civil'),
(7, 'Computer');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `reg_id` int(2) NOT NULL,
  `username` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `usertype` varchar(10) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`reg_id`, `username`, `date`, `usertype`, `password`) VALUES
(26, 'sudip', '2020-09-29', 'Admin', 'sudip'),
(27, 'bhavyesh', '2020-09-29', 'Admin', 'bhavyesh'),
(29, 'pradip', '2020-09-29', 'Admin', 'pradip'),
(31, 'teacher', '2020-10-04', 'Teacher', 'teacher');

-- --------------------------------------------------------

--
-- Table structure for table `session`
--

CREATE TABLE `session` (
  `session_id` int(2) NOT NULL,
  `session_time` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `enroll_no` varchar(12) NOT NULL,
  `name` varchar(60) NOT NULL,
  `email` varchar(40) NOT NULL,
  `dob` date NOT NULL,
  `gender` char(1) NOT NULL,
  `phone_no` varchar(10) NOT NULL,
  `address` text NOT NULL,
  `depart_id` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`enroll_no`, `name`, `email`, `dob`, `gender`, `phone_no`, `address`, `depart_id`) VALUES
('181230106017', 'Sudip', 'sudip@gmail.com', '1998-11-22', 'M', '1234592345', 'navsari\n\n\n\n', 6),
('181230106019', 'preet', 'preet@gmail.com', '1998-10-30', 'M', '1234123478', 'surat\n\n\n\n\n', 6),
('181230107002', 'ayush', 'ayush@gmail.com', '2000-07-23', 'M', '1234567890', '\n', 7),
('181230107024', 'jay', 'jay@gmail.com', '1999-11-22', 'M', '1234123412', 'navsari\n\n', 7);

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `subject_id` int(3) NOT NULL,
  `subject` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`subject_id`, `subject`) VALUES
(1, 'D.S.'),
(2, 'D.B.M.S'),
(3, 'MATH-1'),
(4, 'MATH-2'),
(5, 'MATH-3'),
(7, 'python with datascience'),
(8, 'A.D.A'),
(9, 'software Engineering'),
(10, 'E.S');

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `teacher_id` int(3) NOT NULL,
  `reg_id` int(2) NOT NULL,
  `name` varchar(60) NOT NULL,
  `email` varchar(40) NOT NULL,
  `dob` date DEFAULT NULL,
  `gender` char(1) NOT NULL,
  `address` text NOT NULL,
  `phone_no` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`teacher_id`, `reg_id`, `name`, `email`, `dob`, `gender`, `address`, `phone_no`) VALUES
(4, 31, 'sudip karmakar', 'sudip@gmail.com', '2000-01-01', 'M', 'navsari\n\n\n\n\n\n\n\n\n\n\n\n', '1234567890');

-- --------------------------------------------------------

--
-- Table structure for table `timetable`
--

CREATE TABLE `timetable` (
  `tt_id` int(2) NOT NULL,
  `depart_id` int(2) NOT NULL,
  `subject_id` int(2) NOT NULL,
  `teacher_id` int(2) NOT NULL,
  `session_id` int(2) NOT NULL,
  `day_id` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `assigned_subjects`
--
ALTER TABLE `assigned_subjects`
  ADD KEY `teacher_id` (`teacher_id`,`subject_id`),
  ADD KEY `subject_id` (`subject_id`);

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`attendance_id`),
  ADD KEY `enroll_no` (`enroll_no`,`teacher_id`,`subject_id`,`session_id`),
  ADD KEY `session_id` (`session_id`),
  ADD KEY `subject_id` (`subject_id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- Indexes for table `day`
--
ALTER TABLE `day`
  ADD PRIMARY KEY (`day_id`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`depart_id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`reg_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `session`
--
ALTER TABLE `session`
  ADD PRIMARY KEY (`session_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`enroll_no`),
  ADD KEY `depart_id` (`depart_id`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`subject_id`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`teacher_id`),
  ADD KEY `reg_id` (`reg_id`);

--
-- Indexes for table `timetable`
--
ALTER TABLE `timetable`
  ADD PRIMARY KEY (`tt_id`),
  ADD KEY `depart_id` (`depart_id`,`subject_id`,`teacher_id`,`session_id`,`day_id`),
  ADD KEY `day_id` (`day_id`),
  ADD KEY `session_id` (`session_id`),
  ADD KEY `subject_id` (`subject_id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `attendance_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `reg_id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `session`
--
ALTER TABLE `session`
  MODIFY `session_id` int(2) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `subject`
--
ALTER TABLE `subject`
  MODIFY `subject_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `teacher`
--
ALTER TABLE `teacher`
  MODIFY `teacher_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `timetable`
--
ALTER TABLE `timetable`
  MODIFY `tt_id` int(2) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `assigned_subjects`
--
ALTER TABLE `assigned_subjects`
  ADD CONSTRAINT `assigned_subjects_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `assigned_subjects_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
  ADD CONSTRAINT `attendance_ibfk_2` FOREIGN KEY (`session_id`) REFERENCES `session` (`session_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `attendance_ibfk_3` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `attendance_ibfk_4` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `attendance_ibfk_5` FOREIGN KEY (`enroll_no`) REFERENCES `student` (`enroll_no`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`depart_id`) REFERENCES `department` (`depart_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `teacher`
--
ALTER TABLE `teacher`
  ADD CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`reg_id`) REFERENCES `register` (`reg_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `timetable`
--
ALTER TABLE `timetable`
  ADD CONSTRAINT `timetable_ibfk_1` FOREIGN KEY (`day_id`) REFERENCES `day` (`day_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `timetable_ibfk_2` FOREIGN KEY (`depart_id`) REFERENCES `department` (`depart_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `timetable_ibfk_3` FOREIGN KEY (`session_id`) REFERENCES `session` (`session_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `timetable_ibfk_4` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `timetable_ibfk_5` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`teacher_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
