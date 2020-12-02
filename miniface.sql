-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2020 at 10:23 AM
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
  `published_at` datetime NOT NULL DEFAULT current_timestamp() COMMENT 'published time',
  `ownership` int(1) NOT NULL DEFAULT 0 COMMENT 'post ownership'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`author`, `title`, `content`, `published_at`, `ownership`) VALUES
('neel', 'password', 'encryption', '2020-11-25 18:27:25', 0),
('neel ', 'done', 'done', '2020-11-25 18:37:24', 0),
('sagar', 'mynewpost', 'uploaded', '2020-11-25 18:40:46', 0),
('sagar', 'ghbjnkm', 'cgvhbjnk', '2020-11-25 19:23:47', 0),
('pranshu', 'New Post', 'Hello World!', '2020-11-26 01:39:36', 0),
('pranshu', 'Private', 'Post', '2020-11-27 01:26:03', 0),
('pranshu', 'pvt', 'post', '2020-11-27 01:27:08', 0),
('pranshu', 'strictly', 'private', '2020-11-27 01:28:47', 0),
('pranshu', 'pranshu', 'kumar', '2020-11-27 01:30:27', 0),
('pranshu', 'akldaksld', 'ansdkjanad', '2020-11-27 01:38:37', 1);

-- --------------------------------------------------------

--
-- Table structure for table `relationship`
--

CREATE TABLE `relationship` (
  `user_one_id` int(11) NOT NULL,
  `user_two_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `action_user` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `relationship`
--

INSERT INTO `relationship` (`user_one_id`, `user_two_id`, `status`, `action_user`) VALUES
(1, 2, 0, 1),
(1, 3, 1, 3),
(1, 4, 1, 4),
(1, 5, 0, 5),
(1, 6, 3, 1),
(2, 3, 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `fname` varchar(50) DEFAULT NULL COMMENT 'user first name',
  `lname` varchar(50) DEFAULT NULL COMMENT 'user last name',
  `username` varchar(50) DEFAULT NULL COMMENT 'user username',
  `encrypt_pw` varchar(100) NOT NULL,
  `id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Table for users';

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`fname`, `lname`, `username`, `encrypt_pw`, `id`) VALUES
('s', 'b', 'sagar', 'gAAAAABfvkTMnXAS2mwipJ-2vp8OG-cnb4Q6FXvnDREMBqlPp1hqUJhUUmJQSJhw4AN8gRczaj3dD-TCfkwK_aDT02tnAMJrrg==', 1),
('p', 'k', 'pranshu', 'gAAAAABfvkTabcJilsTWXnz9cBZLOw93iMJhYzC7FoGK3bypm5F1Q6YUYgj4nlveMZ3aM-AXYU8LvEIrXm4SmpSUonMjCVnPrw==', 2),
('n', 'p', 'neel', 'gAAAAABfvkTold5hqT9Uz1FkCsPDkumKMaKJRCe7v0fJa-z-GV7hl9L19ZntUH5HcigYRqjUTJDFAljRUqeVzXuLNKTxnFDifQ==', 3),
('abcd', 'fgvbh', 'vv', 'gAAAAABfvqIOD-3qasrMXm5b-P-83u6rZ1Nq2rf3pMIUXWuTlxqBQzN1lNjIg1ME2VqxIh8_gwk7bVf2LgmYdjvOS0PIHSxwKQ==', 4);

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
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

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
