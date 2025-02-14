from GameObject import *;
from Const import *;

class TitleLogo(GameObject):
    def __init__(self, x, y, angle, sx, sy, state):
        super(TitleLogo, self).__init__(x, y, angle, sx, sy, state);
        TitleLogo.Font = pico2d.load_font('assets/Font/font.TTF', 50);
        self.name = "TitleLogo";
        self.state = True;
        self.has_image = True;
        self.logo = pico2d.load_image("assets/TitleScene/logo.png");
        pass;

    def update(self, time):
        pass;

    def render(self):
        #self.logo.draw_to_origin(self.transform.tx , self.transform.ty, self.logo.w, self.logo.h);
        self.logo.draw_to_origin( Const.WIN_WIDTH //3 , Const.WIN_HEIGHT //3 , self.transform.tx * self.transform.sx, self.transform.ty * self.transform.sy);
        TitleLogo.Font.draw( Const.WIN_WIDTH //3.5 , Const.WIN_HEIGHT //4, "PRESS SPACE TO START",(193, 11, 36));

        pass;