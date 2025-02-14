from Const import *;
from ConfigParser import ConfigParser as Parser;
import pico2d;
from typing import List;


class Tile:
    IMGSForTILE:List[pico2d.Image] = [];
    WIDTH:int = 0;
    HEIGHT:int = 0;
    LOAD:bool = False;

    def __init__(self, type, x:int, y:int):
        self.tile_type = type;
        self.x = x;
        self.y = y;
        if False == Tile.LOAD :
            parser = Parser();
            parser.parse("config.ini");
            Tile.WIDTH = parser.get_int("TILE_WIDTH");
            Tile.HEIGHT = parser.get_int("TILE_HEIGHT");

            for idx in range(1, 33):
                Tile.IMGSForTILE.append( pico2d.load_image( 'assets/Tile/tile ({0}).png'.format( str(idx) ) ) );

            del parser;

            Tile.LOAD = True;

    def set_tile(self, type):
        self.type = type;

    def get_tile(self):
        return Tile.IMGSForTILE[self.tile_type];

    def render(self):
        pass;

    def update(self, time):
        pass;

if __name__ == "__main__" :
    pico2d.open_canvas();
    tile = Tile(1, 2 , 3);
    print("{0}, {1}, {2}".format(tile.tile_type, tile.x, tile.y))

    print("시작");