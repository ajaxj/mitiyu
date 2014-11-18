CREATE DATABASE `bangchu8db` /*!40100 DEFAULT CHARACTER SET utf8 */;

DROP TABLE IF EXISTS `bangchu8db`.`categories`;
CREATE TABLE  `bangchu8db`.`categories` (
  `Id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `Name` varchar(45) NOT NULL COMMENT '分类类别名称',
  `Pinyin` varchar(45) NOT NULL COMMENT '字母',
  `ParentId` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '父母分类Id',
  `Depth` int(10) unsigned NOT NULL DEFAULT '1' COMMENT '深度，从1递增',
  `Status` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '状态：0禁用，1启用',
  `Priority` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '优先级，越大，同级显示的时候越靠前',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


http://www.xiangha.com/shicai/
http://www.cnblogs.com/jeffwongishandsome/archive/2010/10/26/1861633.html