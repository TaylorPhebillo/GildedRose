#!usr/local/bin/python3 
# # -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from copy import deepcopy


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [
            #Item("foo", 0, 3),
            #Item("Aged Brie", 100, 10),
            Item("Backstage passes to a TAFKAL80ETC concert", 20, 12),
            #Item("Sulfuras, Hand of Ragnaros", 80, 100)
            ]
        for _ in range(500):
            gilded_rose_new = GildedRose(deepcopy(items))
            gilded_rose_new.update_quality()
            gilded_rose_old = GildedRose(items)
            gilded_rose_old.update_quality_old()
            self.assertEqual(gilded_rose_new, gilded_rose_old)
            self.assertEqual(gilded_rose_new.items, gilded_rose_old.items)
            for i in range(len(gilded_rose_old.items)):
                self.assertEqual(gilded_rose_old.items[i], gilded_rose_new.items[i])
        
if __name__ == '__main__':
    unittest.main()
