-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 21, 2022 at 06:46 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `idatg2204_2022_group12`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--


CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `name` varchar(100) COLLATE utf8mb4_danish_ci NOT NULL,
  `employee_id` int(11) NOT NULL,
  `responsibility` varchar(255) COLLATE utf8mb4_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `driver`
--

CREATE TABLE `driver` (
  `id` int(11) NOT NULL,
  `transport_id` int(11) NOT NULL,
  `first_name` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `last_name` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `manafacturer_id` int(11) NOT NULL,
  `first_name` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `last_name` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `franchise`
--

CREATE TABLE `franchise` (
  `name` varchar(100) COLLATE utf8mb4_danish_ci NOT NULL,
  `customer_id` int(11) NOT NULL,
  `price_up` int(11) DEFAULT NULL,
  `address` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `manafacturer`
--

CREATE TABLE `manafacturer` (
  `id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `ski_type` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `total_price` int(11) DEFAULT NULL,
  `order_status` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `order_setting`
--

CREATE TABLE `order_setting` (
  `independent` int(11) NOT NULL,
  `store_info_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_danish_ci NOT NULL,
  `type` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  `description` varchar(255) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `in_production` tinyint(1) DEFAULT NULL,
  `MSRPP` int(11) DEFAULT NULL,
  `url_photo` varchar(255) COLLATE utf8mb4_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

INSERT INTO `product` (`id`, `model`, `type`, `size`, `description`, `in_production`, `MSRPP`, `url_photo`) VALUES
('001', 'Race Pro', 'Skate', '142', 'Racing skies, minimum length', '1', '123', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('002', 'Race Pro', 'Skate', '147', 'Racing skies, short length', '1', '123', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'), 
('003', 'Race Pro', 'Skate', '152', 'Racing skies, short length', '1', '123', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('004', 'Race Pro', 'Skate', '157', 'Racing skies, short length', '1', '123', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('005', 'Race Pro', 'Skate', '162', 'Racing skies, short length', '1', '123', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('006', 'Race Pro', 'Skate', '167', 'Racing skies, medium length', '1', '130', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('007', 'Race Pro', 'Skate', '172', 'Racing skies, medium length', '1', '130', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('008', 'Race Pro', 'Skate', '177', 'Racing skies, medium length', '1', '130', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('009', 'Race Pro', 'Skate', '182', 'Racing skies, medium length', '1', '130', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('010', 'Race Pro', 'Skate', '187', 'Racing skies, medium length', '1', '130', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('011', 'Race Pro', 'Skate', '192', 'Racing skies, long length', '1', '140', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('012', 'Race Pro', 'Skate', '197', 'Racing skies, long length', '1', '140', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('013', 'Race Pro', 'Skate', '202', 'Racing skies, long length', '1', '140', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('014', 'Race Pro', 'Skate', '207', 'Racing skies, maximum length', '1', '140', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('015', 'Race Speed', 'Skate', '142', 'Racing skies for speed, minimum length', '1', '144', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `production_plan`
--

CREATE TABLE `production_plan` (
  `week_number` int(11) NOT NULL,
  `manafacturer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `production_type`
--

CREATE TABLE `production_type` (
  `id` int(11) NOT NULL,
  `production_week_number` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `day` int(11) DEFAULT NULL,
  `type` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `production_amount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `receive_shipment`
--

CREATE TABLE `receive_shipment` (
  `directly` int(11) NOT NULL,
  `store_info_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `shipment`
--

CREATE TABLE `shipment` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `store_franchise_name` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `address` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `scheduled_pickup_date` date DEFAULT NULL,
  `state` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `transport_name` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `driver_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store`
--

CREATE TABLE `store` (
  `name` varchar(100) COLLATE utf8mb4_danish_ci NOT NULL,
  `customer_id` int(11) NOT NULL,
  `address` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `price_up` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `store_info`
--

CREATE TABLE `store_info` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `team_skier`
--

CREATE TABLE `team_skier` (
  `first_name` varchar(100) COLLATE utf8mb4_danish_ci NOT NULL,
  `last_name` varchar(100) COLLATE utf8mb4_danish_ci NOT NULL,
  `customer_id` int(11) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `club` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `number_of_skis` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transport`
--

CREATE TABLE `transport` (
  `id` int(11) NOT NULL,
  `shipment_id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`name`,`employee_id`),
  ADD KEY `fk_employee_id_department` (`employee_id`);

--
-- Indexes for table `driver`
--
ALTER TABLE `driver`
  ADD PRIMARY KEY (`id`,`transport_id`),
  ADD KEY `fk_transport_id_driver` (`transport_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`,`manafacturer_id`),
  ADD KEY `fk_manafacturer_id_employee` (`manafacturer_id`);

--
-- Indexes for table `franchise`
--
ALTER TABLE `franchise`
  ADD PRIMARY KEY (`name`,`customer_id`),
  ADD KEY `fk_customer_id` (`customer_id`);

--
-- Indexes for table `manafacturer`
--
ALTER TABLE `manafacturer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`id`,`product_id`,`customer_id`),
  ADD KEY `fk_product_id_order` (`product_id`),
  ADD KEY `fk_customer_id_order` (`customer_id`);

--
-- Indexes for table `order_setting`
--
ALTER TABLE `order_setting`
  ADD PRIMARY KEY (`independent`,`store_info_id`),
  ADD KEY `fk_store_info_id_order_setting` (`store_info_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `production_plan`
--
ALTER TABLE `production_plan`
  ADD PRIMARY KEY (`week_number`,`manafacturer_id`),
  ADD KEY `fk_manafacturer_id_production_plans` (`manafacturer_id`);

--
-- Indexes for table `production_type`
--
ALTER TABLE `production_type`
  ADD PRIMARY KEY (`id`,`production_week_number`,`product_id`),
  ADD KEY `fk_production_week_number_production_type` (`production_week_number`),
  ADD KEY `fk_product_id_production_type` (`product_id`);

--
-- Indexes for table `receive_shipment`
--
ALTER TABLE `receive_shipment`
  ADD PRIMARY KEY (`directly`,`store_info_id`),
  ADD KEY `fk_store_info_id_receive_shipment` (`store_info_id`);

--
-- Indexes for table `shipment`
--
ALTER TABLE `shipment`
  ADD PRIMARY KEY (`id`,`order_id`),
  ADD KEY `fk_order_id_shipment` (`order_id`);

--
-- Indexes for table `store`
--
ALTER TABLE `store`
  ADD PRIMARY KEY (`name`,`customer_id`),
  ADD KEY `fk_customer_id_store` (`customer_id`);

--
-- Indexes for table `store_info`
--
ALTER TABLE `store_info`
  ADD PRIMARY KEY (`id`,`customer_id`),
  ADD KEY `fk_customer_id_store_info` (`customer_id`);

--
-- Indexes for table `team_skier`
--
ALTER TABLE `team_skier`
  ADD PRIMARY KEY (`first_name`,`last_name`,`customer_id`),
  ADD KEY `fk_customer_id_team_skier` (`customer_id`);

--
-- Indexes for table `transport`
--
ALTER TABLE `transport`
  ADD PRIMARY KEY (`id`,`shipment_id`),
  ADD KEY `fk_shipment_id_transport` (`shipment_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `driver`
--
ALTER TABLE `driver`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `manafacturer`
--
ALTER TABLE `manafacturer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order_setting`
--
ALTER TABLE `order_setting`
  MODIFY `independent` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `production_type`
--
ALTER TABLE `production_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `receive_shipment`
--
ALTER TABLE `receive_shipment`
  MODIFY `directly` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `shipment`
--
ALTER TABLE `shipment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_info`
--
ALTER TABLE `store_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport`
--
ALTER TABLE `transport`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `department`
--
ALTER TABLE `department`
  ADD CONSTRAINT `fk_employee_id_department` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `driver`
--
ALTER TABLE `driver`
  ADD CONSTRAINT `fk_transport_id_driver` FOREIGN KEY (`transport_id`) REFERENCES `transport` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `fk_manafacturer_id_employee` FOREIGN KEY (`manafacturer_id`) REFERENCES `manafacturer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `franchise`
--
ALTER TABLE `franchise`
  ADD CONSTRAINT `fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `fk_customer_id_order` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_product_id_order` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);

--
-- Constraints for table `order_setting`
--
ALTER TABLE `order_setting`
  ADD CONSTRAINT `fk_store_info_id_order_setting` FOREIGN KEY (`store_info_id`) REFERENCES `store_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `production_plan`
--
ALTER TABLE `production_plan`
  ADD CONSTRAINT `fk_manafacturer_id_production_plans` FOREIGN KEY (`manafacturer_id`) REFERENCES `manafacturer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `production_type`
--
ALTER TABLE `production_type`
  ADD CONSTRAINT `fk_product_id_production_type` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_production_week_number_production_type` FOREIGN KEY (`production_week_number`) REFERENCES `production_plan` (`week_number`);

--
-- Constraints for table `receive_shipment`
--
ALTER TABLE `receive_shipment`
  ADD CONSTRAINT `fk_store_info_id_receive_shipment` FOREIGN KEY (`store_info_id`) REFERENCES `store_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `shipment`
--
ALTER TABLE `shipment`
  ADD CONSTRAINT `fk_order_id_shipment` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `store`
--
ALTER TABLE `store`
  ADD CONSTRAINT `fk_customer_id_store` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `store_info`
--
ALTER TABLE `store_info`
  ADD CONSTRAINT `fk_customer_id_store_info` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `team_skier`
--
ALTER TABLE `team_skier`
  ADD CONSTRAINT `fk_customer_id_team_skier` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `transport`
--
ALTER TABLE `transport`
  ADD CONSTRAINT `fk_shipment_id_transport` FOREIGN KEY (`shipment_id`) REFERENCES `shipment` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
