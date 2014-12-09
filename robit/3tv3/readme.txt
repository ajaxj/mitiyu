3tv3
http://www.guobianyu.com/





CREATE TABLE `zhuzhu_mv` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cateen` varchar(45) DEFAULT NULL COMMENT '分类英文',
  `catecn` varchar(45) DEFAULT NULL COMMENT '分类中文',
  `url` varchar(200) DEFAULT NULL COMMENT '远程地址',
  `title` varchar(100) DEFAULT NULL COMMENT '片名',
  `banben` varchar(45) DEFAULT NULL COMMENT '版本',
  `arts` varchar(200) DEFAULT NULL COMMENT '演员',
  `lang` varchar(45) DEFAULT NULL COMMENT '语言',
  `location` varchar(45) DEFAULT NULL COMMENT '地区',
  `pubdate` varchar(45) DEFAULT NULL COMMENT '发布时间',
  `content` text COMMENT '介绍',
  `list` text COMMENT '地址列表',
  `status` tinyint(3) unsigned DEFAULT '0' COMMENT '状态0初始1抓取补全2修正',
  `img` varchar(255) DEFAULT NULL COMMENT '图片地址',
  `pubyear` varchar(45) DEFAULT NULL COMMENT '出品年',
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15963 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='zhuzhu mv'


CREATE TABLE `suku_mv` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cateen` varchar(45) DEFAULT NULL COMMENT '分类英文',
  `catecn` varchar(45) DEFAULT NULL COMMENT '分类中文',
  `url` varchar(200) DEFAULT NULL COMMENT '远程地址',
  `title` varchar(100) DEFAULT NULL COMMENT '片名',
  `banben` varchar(45) DEFAULT NULL COMMENT '版本',
  `arts` varchar(200) DEFAULT NULL COMMENT '演员',
  `location` varchar(45) DEFAULT NULL COMMENT '地区',
  `pubdate` varchar(45) DEFAULT NULL COMMENT '发布时间',
  `content` text COMMENT '介绍',
  `list` text COMMENT '地址列表',
  `status` tinyint(3) unsigned DEFAULT '0' COMMENT '状态0初始1抓取补全2修正',
  `img` varchar(100) DEFAULT NULL COMMENT '图片地址',
  `pubyear` varchar(45) DEFAULT NULL COMMENT '出品年',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5335 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='suku mv'
