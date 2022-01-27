# -*- coding: utf-8 -*-
from dataclasses import dataclass
from collections import defaultdict
@dataclass
# Yeah, we angered the goblin, but it's API compatible and goblins are dumb, so we're probably fine.
class Item:
    name: str
    sell_in: int
    quality: int

start_of_time = float('inf')

@dataclass
class DailyItemChanges(object):
    quality_limits = [0,50]
    # TODO: Make quality delta entries a more sensible object/named tuple, instead of magic tuple
    # Starting at this many days until the sell_in date, update the quality by this much
    # format (sell_in limit, quality change)
    quality_delta = [(0, -2), (start_of_time, -1)]

item_changes = defaultdict(DailyItemChanges)

brie = DailyItemChanges()
brie.quality_delta = [(0, 2), (start_of_time, 1)]
item_changes["Aged Brie"] = brie

sulfuras = DailyItemChanges()
sulfuras.quality_limits = [80,80]
item_changes["Sulfuras, Hand of Ragnaros"] = sulfuras

backstage = DailyItemChanges()
backstage.quality_delta = [(0, -float('inf')), (5, 3), (10, 2), (start_of_time, 1)]
item_changes["Backstage passes to a TAFKAL80ETC concert"] = backstage

conjured = DailyItemChanges()
conjured.quality_delta = [(start_of_time, -2)]
item_changes["conjured"] = conjured

def update_item_quality(item):
    item_change = item_changes[item.name]
    item.sell_in -= 1
    quality_change = next((x[1] for x in item_change.quality_delta if x[0] > item.sell_in), item_change.quality_delta[0][1])
    item.quality += quality_change
    item.quality = max(min(item.quality, item_change.quality_limits[1]), item_change.quality_limits[0])
    return item

@dataclass
class GildedRose(object):
    items: [Item]

    def update_quality(self):
        self.items = [update_item_quality(item) for item in self.items]

    def update_quality_old(self):
        for item in self.items:

            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

