
# Generates the commands for the algorithm we're going to use
# I totally over-programmed this

moveCommands = open( "moveCommands.txt", 'w' )

# Move into the inner square that excludes the cache tiles
moveCommands.write( "FWD 1.4\nROT -45.0\n" )

for row in range(5):
    for col in range(5):
        # Move forward one foot,
        # so we move and stop on each tile
        moveCommands.write( "FWD 1.0\n" )
    
    TURN_ANGLE = "90.0\n"

    # On even rows, we need to turn left to turn upwards
    # On odd rows, we need to turn right
    if row % 2 == 0:
        output = "ROT " + TURN_ANGLE
    else:
        output = "ROT -" + TURN_ANGLE

    # We don't want to turn up on the last row
    if row != 4:
        moveCommands.write( output )
        moveCommands.write( "FWD 1.0\n" )
        moveCommands.write( output )

moveCommands.close()
