#!/usr/bin/env python3
# by Tigran Gevorkian

# GPLv3
# This programm is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Softeare Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is disrtibuted in the hope that it will be useful,but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import pygame , os , sys

# Переменные
worldx = 960
worldy= 720
fps = 40 #частота кадров
ani = 4 #циклы анимации
main = True


# Объекты

class Player(pygame.sprite.Sprite):
    #персонаж сам
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # type: ignore (тут тоже надо 2 подчеркивания
        self.images = []

        img = pygame.image.load(os.path.join('images', 'hero1.png'))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()


# Настройка

pygame.display.set_caption("First Game / Newtonioapple")
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
player = Player() #создать спрайт
player.rect.x = 0 #x
player.rect.y = 0 #y
player_list = pygame.sprite.Group()
player_list.add(player)

# Главный Цикл
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord("q"):
                pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

world.fill(255, 255, 255) # type: ignore
player_list.draw(world)
pygame.display.update()
clock.tick(fps)

