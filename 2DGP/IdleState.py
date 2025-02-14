from StateMachine import *;

from Player import *;
from Graphic import *;

class IdleStateForPlayer(StateMachine):
    def __init__(self, player):
        #print("idle");
        self.player = player;
        self.player.animation_state = self.player.dir+ 2;
        self.Fx ,self.Fy = 0,0;
        self.timer = 0;

        self.animation_state = 0;

        self.player.set_velocity(self.Fx, self.Fy);
        return;

    def update(self, time):
        self.timer += time;
        self.player.physx.set_force(0,0);
        #self.player.physx.set_velocity(0,0);
        if self.timer>0.225:
            self.animation_state= (self.animation_state+1)%4;
            self.timer=0;
        
        # 공중에 있는 상태이면 
        return;
    
    def render(self):
        from Const import Const;
        if(self.player.m_dir == Const.direction_R) : self.renderForRight();
        else: self.renderForLeft();

        return;
    def renderForRight(self):
        from Player import Player;
        if self.player.hit_component.can_hitted() :
            Player.IMGSForIdleR[self.animation_state].clip_composite_draw(0,0,
                               Player.IMGSForIdleR[self.animation_state].w,
                               Player.IMGSForIdleR[self.animation_state].h,
                               0,'',
                               self.player.transform.tx-GameObject.Cam.camera_offset_x,
                               self.player.transform.ty-GameObject.Cam.camera_offset_y,
                               );
        else :
            Player.IMGSForIdleRAlpha[self.animation_state].clip_composite_draw(0,0,
                               Player.IMGSForIdleR[self.animation_state].w,
                               Player.IMGSForIdleR[self.animation_state].h,
                               0,'',
                               self.player.transform.tx-GameObject.Cam.camera_offset_x,
                               self.player.transform.ty-GameObject.Cam.camera_offset_y,
                               );

    def renderForLeft(self):
        from Player import Player;
        if self.player.hit_component.can_hitted() :
            Player.IMGSForIdleL[self.animation_state].clip_composite_draw(0,0,
                           Player.IMGSForIdleL[self.animation_state].w,
                           Player.IMGSForIdleL[self.animation_state].h,
                           0,'',
                           self.player.transform.tx-GameObject.Cam.camera_offset_x,
                           self.player.transform.ty-GameObject.Cam.camera_offset_y,
                           );
        else :
            Player.IMGSForIdleLAlpha[self.animation_state].clip_composite_draw(0,0,
                           Player.IMGSForIdleL[self.animation_state].w,
                           Player.IMGSForIdleL[self.animation_state].h,
                           0,'',
                           self.player.transform.tx-GameObject.Cam.camera_offset_x,
                           self.player.transform.ty-GameObject.Cam.camera_offset_y,
                           );


    def exit(self):
        
        pass;




