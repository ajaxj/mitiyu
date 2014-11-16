/*
Navicat MySQL Data Transfer

Source Server         : 210.209.117.163
Source Server Version : 50537
Source Host           : 210.209.117.163:3306
Source Database       : wp

Target Server Type    : MYSQL
Target Server Version : 50537
File Encoding         : 65001

Date: 2014-11-16 23:44:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for wp_term_relationships
-- ----------------------------
DROP TABLE IF EXISTS `wp_term_relationships`;
CREATE TABLE `wp_term_relationships` (
  `object_id` bigint(20) unsigned NOT NULL DEFAULT '0',
  `term_taxonomy_id` bigint(20) unsigned NOT NULL DEFAULT '0',
  `term_order` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`object_id`,`term_taxonomy_id`),
  KEY `term_taxonomy_id` (`term_taxonomy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
