# -*- coding: utf-8 -*-
from dataclasses import dataclass
from collections import defaultdict
@dataclass
class Item:
    name: str
    sell_in: int
    quality: int

start_of_time = -float('inf')

@dataclass
class DailyItemChanges(object):
    quality_limits = [0,50]
    quality_delta = [(start_of_time, -1), (0,-2)]

item_changes = defaultdict(DailyItemChanges)

brie = DailyItemChanges()
brie.quality_delta = [(start_of_time, 1)]
item_changes["Aged Brie"] = brie

sulfuras = DailyItemChanges()
sulfuras.quality_limits = [80,80]
item_changes["Sulfuras, Hand of Ragnaros"] = sulfuras

backstage = DailyItemChanges()
backstage.quality_delta = [(start_of_time, 1), (-10, 2), (-5, 3), (0, -float('inf'))]
item_changes["Backstage passes to a TAFKAL80ETC concert"] = backstage

conjured = DailyItemChanges()
conjured.quality_delta = [(start_of_time, -2)]
item_changes["conjured"] = conjured

def update_item_quality(item):
    item_change = item_changes[item.name]
    print(item_change)
    item.sell_in -= 1
    quality_change = next((x[1] for x in reversed(item_change.quality_delta) if x[0] > item.sell_in), item_change.quality_delta[0][1])
    print(f"Quality change for {item} = {quality_change} via {item_change}, in particular {item_change.quality_delta}")
    item.quality += quality_change
    item.quality = max(min(item.quality, item_change.quality_limits[1]), item_change.quality_limits[0])
    print(f"Updated to {item}")
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

