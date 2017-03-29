
# Generates the commands for the algorithm we're going to use
# I totally over-programmed this
from collections import deque

FILE_LOCATION = "../Robot_OS/moveCommands.txt"

def writeGrid( fileName ):
    moveCommands = open( fileName, 'w' )

    # Move into the inner square that excludes the cache tiles
    moveCommands.write( "FWD 1.4\nPAUSE 2.0\nROT 0.0\nPAUSE 2.0\n" )

    for row in range(5):
        for col in range(4):
            # Move forward one foot,
            # so we move and stop on each tile
            moveCommands.write( "FWD 1.0\nPAUSE 2.0\n" )
        
        #TURN_ANGLE = "90.0\n"

        # On even rows, we need to turn left to turn upwards
        # On odd rows, we need to turn right
        if row % 2 == 0:
            secondTurn = "ROT 180.0\nPAUSE 2.0\n"
        else:
            secondTurn = "ROT 0.0\nPAUSE 2.0\n"

        firstTurn = "ROT 90.0\nPAUSE 2.0\n"

        # We don't want to turn up on the last row
        if row != 4:
            moveCommands.write( firstTurn )
            moveCommands.write( "FWD 1.0\nPAUSE 2.0\n" )
            moveCommands.write( secondTurn )

    moveCommands.close()

def writeRadial( fileName ):
    moveCommands = open( fileName, 'w' )

    moveCommands.write( "FWD 1.4\nPAUSE 2.0\n" )
    moveCommands.write( "FWD 1.4\nPAUSE 2.0\n" )
    moveCommands.write( "ROT 0.0\nPAUSE 2.0\n" )

    for i in range(3):
        moveCommands.write( "FWD 1.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWT 2.0\nPAUSE 2.0\n" )

    moveCommands.write( "FWD -2.0\nPAUSE 2.0\n" )
    moveCommands.write( "ROT -90.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWD 1.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWT 2.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWD -2.0\nPAUSE 2.0\n" )

    for i in range(3):
        moveCommands.write( "FWD -1.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWD -2.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWT 2.0\nPAUSE 2.0\n" )
    moveCommands.write( "ROT 0.0\nPAUSE 2.0\n" )

    moveCommands.write( "FWD 1.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWT 2.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWD -2.0\nPAUSE 2.0\n" )

    for i in range(3):
        moveCommands.write( "FWD -1.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWD -2.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWT 2.0\nPAUSE 2.0\n" )
    moveCommands.write( "ROT 0.0\nPAUSE 2.0\n" )

    moveCommands.write( "FWD 1.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWT 2.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWD -2.0\nPAUSE 2.0\n" )

    for i in range(3):
        moveCommands.write( "FWD -1.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWD -2.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWT 2.0\nPAUSE 2.0\n" )
    moveCommands.write( "ROT 90.0\nPAUSE 2.0\n" )

    moveCommands.write( "FWD 1.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWT 2.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWD -2.0\nPAUSE 2.0\n" )

    for i in range(3):
        moveCommands.write( "FWD -1.0\nPAUSE 2.0\n" )

    moveCommands.write( "FWD -2.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWT 2.0\nPAUSE 2.0\n" )
    moveCommands.write( "ROT 180.0\nPAUSE 2.0\n" )

    moveCommands.write( "FWD 1.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWT 2.0\nPAUSE 2.0\n" )

    moveCommands.write( "FWD -0.25\nPAUSE 2.0\n" )
    moveCommands.write( "ROT 270\nPAUSE 2.0\n" )

    moveCommands.write( "FWD 1.0\nPAUSE 2.0\n" )
    moveCommands.write( "FWT 2.0\nPAUSE 2.0\n" )

    moveCommands.close()

def printAlgo( fileName ):
    fin = open( fileName, 'r' )
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

#writeGrid( FILE_LOCATION )
writeRadial( FILE_LOCATION )
printAlgo( FILE_LOCATION )