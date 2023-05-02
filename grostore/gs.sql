-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 24, 2022 at 04:48 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gs`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_delivered` (IN `o_id` INT)  BEGIN
	DELETE from order_details where order_details.order_id=o_id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `delivery_update` (IN `o_id` INT)  BEGIN
	update order_delivery set deliverd=1 WHERE order_delivery.order_id=o_id;
END$$

--
-- Functions
--
CREATE DEFINER=`root`@`localhost` FUNCTION `get_pname` (`p_id` INT) RETURNS VARCHAR(30) CHARSET utf8mb4 BEGIN
	DECLARE p_name varchar(30);
    select products.product_name from products WHERE products.product_id=p_id INTO p_name;
    return (p_name);
END$$

CREATE DEFINER=`root`@`localhost` FUNCTION `get_price_perunit` (`product_name` VARCHAR(30)) RETURNS INT(11) BEGIN
	DECLARE price_perunit int;
    select products.price_per_unit from products WHERE products.product_name=product_name INTO price_perunit;
    return (price_perunit);
END$$

CREATE DEFINER=`root`@`localhost` FUNCTION `unit_of_mes_names` (`uom_name` VARCHAR(30)) RETURNS VARCHAR(30) CHARSET utf8mb4 BEGIN
	DECLARE uom_id varchar(20);
    select uom.uom_id from uom WHERE uom.uom_name=uom_name INTO uom_id;
    return (uom_id);
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `order_delivery`
--

CREATE TABLE `order_delivery` (
  `order_id` int(11) NOT NULL,
  `deliverd` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_delivery`
--

INSERT INTO `order_delivery` (`order_id`, `deliverd`) VALUES
(8, 1),
(9, 1),
(10, 0),
(11, 1),
(12, 1),
(13, 1),
(14, 1),
(15, 1),
(16, 0);

-- --------------------------------------------------------

--
-- Table structure for table `order_details`
--

CREATE TABLE `order_details` (
  `order_id` int(11) NOT NULL,
  `customer_name` varchar(30) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `order_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_details`
--

INSERT INTO `order_details` (`order_id`, `customer_name`, `product_id`, `quantity`, `order_date`) VALUES
(10, 'maneesh', 6, 2, '2022-11-22'),
(16, 'mahesh', 10, 2, '2022-11-23');

--
-- Triggers `order_details`
--
DELIMITER $$
CREATE TRIGGER `add_to_delivery` AFTER INSERT ON `order_details` FOR EACH ROW begin
insert into order_delivery(order_id,deliverd) values (new.order_id,'0');
end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(30) NOT NULL,
  `uom_id` int(30) NOT NULL,
  `price_per_unit` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_name`, `uom_id`, `price_per_unit`) VALUES
(5, 'rice', 1, 25),
(6, 'moong dall', 2, 100),
(7, 'toothpaste', 2, 30),
(8, 'soap', 1, 35),
(9, 'banana', 2, 20),
(10, 'onions', 2, 50),
(11, 'apple', 2, 100),
(14, 'spinach', 1, 35),
(95, 'shampoo', 1, 200),
(96, 'milk', 1, 20);

-- --------------------------------------------------------

--
-- Table structure for table `uom`
--

CREATE TABLE `uom` (
  `uom_id` int(11) NOT NULL,
  `uom_name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `uom`
--

INSERT INTO `uom` (`uom_id`, `uom_name`) VALUES
(1, 'each'),
(2, 'kg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `order_details`
--
ALTER TABLE `order_details`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `uom_id` (`uom_id`);

--
-- Indexes for table `uom`
--
ALTER TABLE `uom`
  ADD PRIMARY KEY (`uom_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `order_details`
--
ALTER TABLE `order_details`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`uom_id`) REFERENCES `uom` (`uom_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
