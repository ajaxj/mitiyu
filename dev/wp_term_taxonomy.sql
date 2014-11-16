/*
Navicat MySQL Data Transfer

Source Server         : 210.209.117.163
Source Server Version : 50537
Source Host           : 210.209.117.163:3306
Source Database       : wp

Target Server Type    : MYSQL
Target Server Version : 50537
File Encoding         : 65001

Date: 2014-11-16 23:44:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for wp_term_taxonomy
-- ----------------------------
DROP TABLE IF EXISTS `wp_term_taxonomy`;
CREATE TABLE `wp_term_taxonomy` (
  `term_taxonomy_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `term_id` bigint(20) unsigned NOT NULL DEFAULT '0',
  `taxonomy` varchar(32) NOT NULL DEFAULT '',
  `description` longtext NOT NULL,
  `parent` bigint(20) unsigned NOT NULL DEFAULT '0',
  `count` bigint(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`term_taxonomy_id`),
  UNIQUE KEY `term_id_taxonomy` (`term_id`,`taxonomy`),
  KEY `taxonomy` (`taxonomy`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8;
