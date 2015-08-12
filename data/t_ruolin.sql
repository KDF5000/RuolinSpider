/*
MySQL Data Transfer
Source Host: localhost
Source Database: company
Target Host: localhost
Target Database: company
Date: 2015/8/12 15:41:17
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for t_ruolin
-- ----------------------------
DROP TABLE IF EXISTS `t_ruolin`;
CREATE TABLE `t_ruolin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL COMMENT '公司名',
  `addr` varchar(100) DEFAULT NULL,
  `comment_num` int(11) DEFAULT '0' COMMENT '评论数',
  `average_point` int(11) DEFAULT '0' COMMENT '平均分',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40480 DEFAULT CHARSET=utf8;
