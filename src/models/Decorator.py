#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator
from ElementoMapa import ElementoMapa

class Decorator(Decorator, ElementoMapa):
    def __init__(self):
        self.activa = None

