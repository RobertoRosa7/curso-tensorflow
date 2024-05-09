# -*- coding: utf-8 -*-

class ProfileCollection:
    def __init__(self) -> None:
        self.total_registers=None
        self.total_positive = None
        self.total_negative=None
        self.total_score_negative=None
        self.total_score_positive=None
        self.mean_feeling=None
        self.std_feeling=None
        self.chart=None

    def set_total_registers(self, value):
        self.total_registers = value
        return self
    
    def set_total_positive(self, value):
        self.total_positive = value
        return self
    def set_total_negative(self, value):
        self.total_negative = value
        return self
    def set_total_score_negetive(self, value):
        self.total_score_negative = value
        return self
    def set_total_score_positive(self, value):
        self.total_score_positive = value
        return self
    def set_mean_feeling(self, value):
        self.mean_feeling = value
        return self
    def set_std_feeling(self, value):
        self.std_feeling = value
        return self
    def set_chart(self, value):
        self.chart = value
        return self
    