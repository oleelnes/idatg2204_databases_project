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
-- Table structure for table `authentication`
--

CREATE TABLE `authentication` (
  `role` varchar(30) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `username` varchar(30) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `password_hashed` varchar(52) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `salt` varchar(12) COLLATE utf8mb4_danish_ci DEFAULT NULL 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

INSERT INTO `authentication` (`role`, `username`, `password_hashed`, `salt`) VALUES
('customer', 'customer_user', 'fill_later', 'salt_fill_later'),
('customer rep', 'customer_rep_user', 'fill_later', 'salt_fill_later'),
('storekeeper', 'storekeeper_user', 'fill_later', 'salt_fill_later');

-----------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

INSERT INTO `customer` (`id`, `start_date`, `end_date`) VALUES 
('300000', '2020-09-09', '2025-10-10'), 
('300001', '2021-02-09', '2025-10-10'), 
('300002', '2010-03-09', '2025-10-10');

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `name` varchar(100) COLLATE utf8mb4_danish_ci NOT NULL,
  `employee_id` int(11) NOT NULL,
  `responsibility` varchar(255) COLLATE utf8mb4_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

INSERT INTO `department` (`name`, `employee_id`, `responsibility`) VALUES
('production', '500000', 'production manager'),
('production', '500001', 'production worker'),
('administration', '500002', 'general manager');

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

INSERT INTO `driver` (`id`, `transport_id`, `first_name`, `last_name`) VALUES
('400000', '900000', 'asgeir', 'olavsen');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `manufacturer_id` int(11) NOT NULL,
  `first_name` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL,
  `last_name` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

INSERT INTO `employee` (`id`, `manufacturer_id`, `first_name`, `last_name`) VALUES
('500000', '200000', 'tore', 'torsen'), 
('500001', '200000', 'peder', 'pedersen'),
('500002', '200000', 'ingvild', 'arnesen');

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

INSERT INTO `franchise` (`name`, `customer_id`, `price_up`, `address`) VALUES
('store ski', '300002', '20', 'storevegen 99');

-- --------------------------------------------------------

--
-- Table structure for table `manafacturer`
--

CREATE TABLE `manafacturer` (
  `id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

INSERT INTO `manufacturer` (`id`, `name`) VALUES
('200000', 'gjovik skifabrikk');

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

INSERT INTO `order` (`id`, `product_id`, `customer_id`, `ski_type`, `quantity`, `total_price`, `order_status`) VALUES 
('100000', '000001', '300000', 'skate', '50', '6150', 'new'), 
('100001', '000002', '300000', 'skate', '2', '200', 'skis available');

-- --------------------------------------------------------

--
-- Table structure for table `order_setting`
--

CREATE TABLE `order_setting` (
  `independent` int(11) NOT NULL,
  `store_info_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

INSERT INTO `order_setting` (`independent`, `store_info_id`) VALUES 
('0', '606060');

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
('000001', 'race pro', 'skate', '142', 'racing skies, minimum length', '1', '123', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('000002', 'race pro', 'skate', '147', 'racing skies, short length', '1', '123', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'), 
('000003', 'race pro', 'skate', '152', 'racing skies, short length', '1', '123', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('000004', 'race pro', 'skate', '157', 'racing skies, short length', '1', '123', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('000005', 'race pro', 'skate', '162', 'racing skies, short length', '1', '123', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('000006', 'race pro', 'skate', '167', 'racing skies, medium length', '1', '130', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('000007', 'race pro', 'skate', '172', 'racing skies, medium length', '1', '130', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('000008', 'race pro', 'skate', '177', 'racing skies, medium length', '1', '130', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('000009', 'race pro', 'skate', '182', 'racing skies, medium length', '1', '130', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('000010', 'race pro', 'skate', '187', 'racing skies, medium length', '1', '130', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('000011', 'race pro', 'skate', '192', 'racing skies, long length', '1', '140', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('000012', 'race pro', 'skate', '197', 'racing skies, long length', '1', '140', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('000013', 'race pro', 'skate', '202', 'racing skies, long length', '1', '140', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('000014', 'race pro', 'skate', '207', 'racing skies, maximum length', '1', '140', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg'),
('000015', 'race speed', 'skate', '142', 'racing skies for speed, minimum length', '1', '144', 'https://antonclub-res.cloudinary.com/image/upload/e_trim:0/c_fit,g_center,w_2048,h_2048/q_auto/bsg73pagn3vbkpe9wweu.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `production_plan`
--

CREATE TABLE `production_plan` (
  `week_number` int(11) NOT NULL,
  `manafacturer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

INSERT INTO `production_plan` (`week_number`, `manufacturer_id`) VALUES 
('1', '202020'), 
('2', '202021');

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

INSERT INTO `production_type` (`id`, `production_week_number`, `product_id`, `day`, `type`, `production_amount`) VALUES
('809090', '1', '001', '4', 'Skate', '100');

-- --------------------------------------------------------

--
-- Table structure for table `receive_shipment`
--

CREATE TABLE `receive_shipment` (
  `directly` int(11) NOT NULL,
  `store_info_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

INSERT INTO `receive_shipment` (`directly`, `store_info_id`) VALUES
('1', '606060');
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

INSERT INTO `shipment` (`id`, `order_id`, `store_franchise_name`, `address`, `scheduled_pickup_date`, `state`, `transport_name`, `driver_id`) VALUES
('7080800', '100000', 'best ski stores', 'heidalsvegen 3', '2022-04-20', 'in transit', 'heidis transport AS', '400000');

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

INSERT INTO `store` (`name`, `customer_id`, `address`, `price_up`) VALUES
('ski store 1', '300000', 'heidalsvegen 3', '30');

-- --------------------------------------------------------

--
-- Table structure for table `store_info`
--

CREATE TABLE `store_info` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

INSERT INTO `store_info` (`id`, `customer_id`) VALUES
('606060', '300000');

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

INSERT INTO `team_skier` (`first_name`, `last_name`, `customer_id`, `date_of_birth`, `club`, `number_of_skis`) VALUES
('arnulf', 'tangen', '300001', '1999-12-20', 'oslo ski club', '20');

-- --------------------------------------------------------

--
-- Table structure for table `transport`
--

CREATE TABLE `transport` (
  `id` int(11) NOT NULL,
  `shipment_id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_danish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_danish_ci;

INSERT INTO `transport` (`id`, `shipment_id`, `name`) VALUES
('900000', '700000', 'example name');

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
