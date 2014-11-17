/*
Navicat MySQL Data Transfer

Source Server         : 210.209.117.163
Source Server Version : 50537
Source Host           : 210.209.117.163:3306
Source Database       : wp

Target Server Type    : MYSQL
Target Server Version : 50537
File Encoding         : 65001

Date: 2014-11-16 23:21:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for wp_postmeta
-- ----------------------------
DROP TABLE IF EXISTS `wp_postmeta`;
CREATE TABLE `wp_postmeta` (
  `meta_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `post_id` bigint(20) unsigned NOT NULL DEFAULT '0',
  `meta_key` varchar(255) DEFAULT NULL,
  `meta_value` longtext,
  PRIMARY KEY (`meta_id`),
  KEY `post_id` (`post_id`),
  KEY `meta_key` (`meta_key`)
) ENGINE=InnoDB AUTO_INCREMENT=19202 DEFAULT CHARSET=utf8;
