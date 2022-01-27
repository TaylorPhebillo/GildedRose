#!usr/local/bin/python3 
# # -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from copy import deepcopy


class GildedRoseTest(unittest.TestCase):
    def test_conjured(self):
        items = [
            Item("conjured", 1000, 50),
            Item("conjured", 100, 10)
            ]
        gilded_rose_new = GildedRose(deepcopy(items))
        for i in range(1, 500):
            gilded_rose_new.update_quality()
            self.assertEqual(gilded_rose_new.items[0].quality, max(50 - 2 * i, 0))
            self.assertEqual(gilded_rose_new.items[1].quality, max(10 - 2 * i, 0))

    def test_compare_sulfuras(self):
        # The new implementation changes the sell_in date for Sulfuras, the old does not- only the quality should match.
        items = [
            Item("Sulfuras, Hand of Ragnaros", 1000, 80),
            Item("Sulfuras, Hand of Ragnaros", 100, 80)
            ]
        gilded_rose_new = GildedRose(deepcopy(items))
        gilded_rose_old = GildedRose(items)
        for _ in range(500):
            gilded_rose_new.update_quality()
            gilded_rose_old.update_quality_old()
            self.assertEqual(len(gilded_rose_new.items), len(gilded_rose_old.items))
            for i in range(len(gilded_rose_old.items)):
                self.assertEqual(gilded_rose_old.items[i].quality, gilded_rose_new.items[i].quality)

    def test_compare_with_old(self):
        items = [
            Item("foo", 100, 3),
            Item("foo", 0, 3),
            Item("Aged Brie", 100, 10),
            Item("Aged Brie", 3, 1),
            Item("Backstage passes to a TAFKAL80ETC concert", 20, 12),
            ]
        gilded_rose_new = GildedRose(deepcopy(items))
        gilded_rose_old = GildedRose(items)
        for _ in range(500):
            gilded_rose_new.update_quality()
            gilded_rose_old.update_quality_old()
            self.assertEqual(gilded_rose_new, gilded_rose_old)
            self.assertEqual(gilded_rose_new.items, gilded_rose_old.items)
            for i in range(len(gilded_rose_old.items)):
                self.assertEqual(gilded_rose_old.items[i], gilded_rose_new.items[i])
        
if __name__ == '__main__':
    unittest.main()
