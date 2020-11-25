-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 25, 2020 at 07:50 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `miniface`
--

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `author` varchar(50) DEFAULT NULL COMMENT 'author of the post',
  `title` varchar(100) DEFAULT NULL COMMENT 'title of the post',
  `content` varchar(500) DEFAULT NULL COMMENT 'content of the post',
  `published_at` datetime NOT NULL DEFAULT current_timestamp() COMMENT 'published time'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`author`, `title`, `content`, `published_at`) VALUES
('neel', 'password', 'encryption', '2020-11-25 18:27:25'),
('neel ', 'done', 'done', '2020-11-25 18:37:24'),
('sagar', 'mynewpost', 'uploaded', '2020-11-25 18:40:46'),
('sagar', 'ghbjnkm', 'cgvhbjnk', '2020-11-25 19:23:47');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `fname` varchar(50) DEFAULT NULL COMMENT 'user first name',
  `lname` varchar(50) DEFAULT NULL COMMENT 'user last name',
  `username` varchar(50) DEFAULT NULL COMMENT 'user username',
  `encrypt_pw` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Table for users';

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`fname`, `lname`, `username`, `encrypt_pw`) VALUES
('s', 'b', 'sagar', 'gAAAAABfvkTMnXAS2mwipJ-2vp8OG-cnb4Q6FXvnDREMBqlPp1hqUJhUUmJQSJhw4AN8gRczaj3dD-TCfkwK_aDT02tnAMJrrg=='),
('p', 'k', 'pranshu', 'gAAAAABfvkTabcJilsTWXnz9cBZLOw93iMJhYzC7FoGK3bypm5F1Q6YUYgj4nlveMZ3aM-AXYU8LvEIrXm4SmpSUonMjCVnPrw=='),
('n', 'p', 'neel', 'gAAAAABfvkTold5hqT9Uz1FkCsPDkumKMaKJRCe7v0fJa-z-GV7hl9L19ZntUH5HcigYRqjUTJDFAljRUqeVzXuLNKTxnFDifQ=='),
('abcd', 'fgvbh', 'vv', 'gAAAAABfvqIOD-3qasrMXm5b-P-83u6rZ1Nq2rf3pMIUXWuTlxqBQzN1lNjIg1ME2VqxIh8_gwk7bVf2LgmYdjvOS0PIHSxwKQ==');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD KEY `author_post` (`author`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD UNIQUE KEY `username` (`username`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `posts`
--
ALTER TABLE `posts`
  ADD CONSTRAINT `author_post` FOREIGN KEY (`author`) REFERENCES `users` (`username`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;