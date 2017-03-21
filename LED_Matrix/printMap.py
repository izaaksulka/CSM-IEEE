from colorGrid import colorGrid

# For linux the "COM3" will be something like
# "/dev/tty.usbserial"
grid = colorGrid( "COM6" )

grid.printInfo()
'''
grid.setTile( 4, 0, grid.GREEN )
grid.setTile( 4, 1, grid.GREEN )
grid.setTile( 4, 2, grid.GREEN )
grid.setTile( 4, 3, grid.BLUE )
grid.setTile( 4, 4, grid.GREEN )
grid.setTile( 4, 5, grid.GREEN )
grid.setTile( 4, 6, grid.BLUE )
grid.setTile( 4, 7, grid.GREEN )
'''
for x in range(8):
    for y in range(8):
        grid.setTile( x, y, y % 4 )
shouldClose = "no"
while shouldClose != "yes":
    
    shouldClose = input( "Exit? " )

grid.cleanup()
