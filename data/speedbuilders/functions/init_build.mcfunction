setblock 4 1 4 minecraft:structure_block{mode:"LOAD"}
data modify block 4 1 4 {} merge from entity @s Item.tag.structure_data
setblock 4 2 4 minecraft:redstone_block
kill @s