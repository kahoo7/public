#   -*- coding:utf-8 -*-
#   Program name: PyCharmProject
#   @author: kahoo from SCNU
#   Time: 2020 03 05 10:57


class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        # 在任何情况下都不应重置最高得分
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1