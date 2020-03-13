#   -*- coding:utf-8 -*-
#   Program name: PyCharmProject
#   @author: kahoo from SCNU
#   Time: 2020 02 10 16:07


class Settings:
    """ 存储《Alien Invasion》的所有类 """

    def __init__(self):
        """ 初始化游戏的静态设置 """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (246, 246, 246)  # 游戏背景：白色

        # 飞船设置
        self.ship_speed_factor = 1.0
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)  # 子弹颜色：黑色
        self.bullet_allowed = 50
        self.bullet_distance = 5

        # 外星人设置
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 12
        self.fleet_direction = 1  # fleet_direction为1表示向右移，为-1表示向左移
        self.alien_points = 50

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1

        # 外星人点数提高速度
        self.score_scale = 1.5

        self.initailize_dynamic_settings()

    def increase_speed(self):
        """ 提高速度设置和外星人点数 """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def initailize_dynamic_settings(self):
        """ 初始化随游戏进行而变化的设置 """
        self.ship_speed_factor = 1.0
        self.bullet_speed_factor = 4
        self.alien_speed_factor = 0.5

        self.fleet_direction = 1  # fleet_direction为1表示向右移，为-1表示向左移

        # 记分
        self.alien_points = 50
