#   -*- coding:utf-8 -*-
#   Program name: PyCharmProject
#   @author: kahoo from SCNU
#   Time: 2020 02 10 16:29

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """ 初始化飞船并设置其初始位置 """
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship3.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # 开火标志
        self.fire = False

    def update(self):
        """ 根据移动标志调整飞船的位置 """
        # 向右移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        # 向左移动
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        # 扩展：向下移动
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_settings.ship_speed_factor
        # 扩展：向上移动
        if self.moving_up and self.rect.centery > 0:
            self.rect.centery -= self.ai_settings.ship_speed_factor

    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
