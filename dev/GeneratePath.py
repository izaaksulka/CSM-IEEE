
# Generates the commands for the algorithm we're going to use
# I totally over-programmed this
from collections import deque

FILE_LOCATION = "../Robot_OS/moveCommands.txt"
moveCommands = open( FILE_LOCATION, 'w' )

# Move into the inner square that excludes the cache tiles
moveCommands.write( "FWD 1.4\nROT -45.0\nPAUSE 2.0\n" )

for row in range(5):
    for col in range(5):
        # Move forward one foot,
        # so we move and stop on each tile
        moveCommands.write( "FWD 1.0\nPAUSE 2.0\n" )
    
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
        moveCommands.write( "FWD 1.0\nPAUSE 2.0\n" )
        moveCommands.write( output )

moveCommands.close()

fin = open( FILE_LOCATION, 'r' )
contents = fin.read()
print( contents )
fin.close()

instructions = deque( [] )
for instruction in contents.split("\n"):
    if len( instruction ) != 0:
        cmd, duration = instruction.split()
        duration = float( duration )
        instructions.append( (cmd, duration) )

print( instructions )
print()
print( len( instructions ) )

while instructions:
    print( instructions.popleft() )