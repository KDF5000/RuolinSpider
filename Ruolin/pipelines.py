# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb.cursors
from scrapy import log

class RuolinPipeline(object):
    def __init__(self):
        self.db_pool = adbapi.ConnectionPool('MySQLdb', db='company', user='root', passwd='root123', host='localhost', cursorclass=MySQLdb.cursors.DictCursor, charset='utf8', use_unicode=True)

    def process_item(self, item, spider):
        query = self.db_pool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tx, item):
        tx.execute("select * from t_ruolin where name=%s", (item['name'],))
        article = tx.fetchone()
        if article:
            if article['addr'] is None:
                tx.execute("update t_ruolin set addr=%s where id=%s", (item['addr'], article['id']))
            log.msg("Item already stored in db:%s" % item, level=log.DEBUG)
        else:
            tx.execute("insert into t_ruolin(name, comment_num, addr, average_point) values(%s, %s, %s, %s)",
                       (item['name'], item['comment_num'], item['addr'], item['average_point']))

    def handle_error(self, e):
        log.msg(e, log.ERROR)
