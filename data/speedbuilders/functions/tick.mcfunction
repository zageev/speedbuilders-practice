scoreboard players add ms stopwatch 05
execute if score ms stopwatch matches 100 run function speedbuilders:add_second
execute if score %isShowing status matches 0 if score %isEnabled loop matches 0 if blocks 4 11 4 10 17 10 4 2 4 all run function speedbuilders:build_finished
execute if score %isShowing status matches 0 if score %isEnabled loop matches 1 if blocks 4 11 4 10 17 10 4 2 4 all run function speedbuilders:loop_build_finished
kill @e[type=minecraft:item]