# version1
# import os
# import os.path
# import pygame as py
# from pygame.locals import *
# import sys
# import random
# import tkinter as tk
# from tkinter import filedialog

# def pos_analysis(black_pos, max_size):
#     '''判断黑块的坐标是否超出显示范围'''
#     if 0 <= black_pos[0] <= max_size[0]:
#         x_in = True
#     else:
#         x_in = False

#     if 0 <= black_pos[1] <= max_size[1]:
#         y_in = True
#     else:
#         y_in = False
#     return x_in and y_in

# def in_area(mouse_pos, area_pos, size):
#     '''判断鼠标是否在区域里'''
#     if area_pos[0] <= mouse_pos[0] <= area_pos[0] + size[0] and \
#     area_pos[1] <= mouse_pos[1] <= area_pos[1] + size[1]:
#         return True
#     else:
#         return False

# def rerand(pos_slice, bg_slice, cheat=0):
#     '''重新打散'''
#     if not cheat:
#         pos_list = random.sample(pos_slice[1:], pdx*pdy-1)
#         picture_list = random.sample(bg_slice[:-1], pdx*pdy-1)
#     else:
#         pos_list = pos_slice[:-1]
#         picture_list = bg_slice[:-1]
#     draw_dict = {pos_list[index]:picture_list[index] for index in range (pdx*pdy-1)}
#     return draw_dict

# font_color = (150, 0, 150)
# line_color = (0, 0, 0)
# outside_line_color = (230, 159, 43)
# bg_color = (1, 158, 193)
# panel_color = (97, 134, 171)
# outside_panel_color = (230, 159, 43)

# SCREEN_SIZE = (800, 640)
# MAIN_WINDOW_SIZE = (640, 480)
# SET_PANEL_SIZE = (480, 360)
# puzzle_dim = (3, 3)

# DX, DY = (SCREEN_SIZE[0]-MAIN_WINDOW_SIZE[0])/2, (SCREEN_SIZE[1]-MAIN_WINDOW_SIZE[1])/2
# black_pos = (DX, DY)
# pdx ,pdy = puzzle_dim[0], puzzle_dim[1]
# bpx ,bpy = black_pos[0], black_pos[1]

# py.init()
# my_font = py.font.SysFont("隶书", 30)
# my_big_font = py.font.SysFont("隶书", 40)

# screen = py.display.set_mode(SCREEN_SIZE)
# bg = py.image.load(r'C:\Users\banana\Desktop\pygame\pikachu\dog.jpg').convert()
# game_win = my_font.render('恭喜,拼图完成!', True, font_color)

# set_image = my_font.render('选项', True, font_color)
# set_big_image = my_big_font.render('选项', True, font_color)
# set_image_size = set_image.get_size()
# set_pos = (MAIN_WINDOW_SIZE[0]+1.1*DX, MAIN_WINDOW_SIZE[1]+1.1*DY)

# quit_image = my_font.render('[X]', True, font_color)
# quit_big_image = my_big_font.render('[X]', True, font_color)
# quit_image_size = quit_image.get_size()
# quit_pos = (SCREEN_SIZE[0]/2+SET_PANEL_SIZE[0]/2-50, SCREEN_SIZE[1]/2-SET_PANEL_SIZE[1]/2)
# rerand_image = my_font.render('重新打散', True, font_color)
# rerand_big_image = my_big_font.render('重新打散', True, font_color)
# rerand_image_size = rerand_image.get_size()
# rerand_pos = (SCREEN_SIZE[0]/2-SET_PANEL_SIZE[0]/3, SCREEN_SIZE[1]/2-SET_PANEL_SIZE[1]/3)
# puzzle_dim_image = my_font.render('当前模式:%dx%d'%(pdx, pdy), True, font_color)
# puzzle_dim_big_image = my_big_font.render('当前模式:%dx%d'%(pdx, pdy), True, font_color)
# puzzle_dim_image_size = puzzle_dim_image.get_size()
# puzzle_dim_pos = (SCREEN_SIZE[0]/2-SET_PANEL_SIZE[0]/3, SCREEN_SIZE[1]/2-SET_PANEL_SIZE[1]/3+40)
# picture_change_image = my_font.render('更换图片', True, font_color)
# picture_change_big_image = my_big_font.render('更换图片', True, font_color)
# picture_change_image_size = picture_change_image.get_size()
# picture_change_pos = (SCREEN_SIZE[0]/2-SET_PANEL_SIZE[0]/3, SCREEN_SIZE[1]/2-SET_PANEL_SIZE[1]/3+2*40)
# cheat_image =  my_font.render('看看原图吧', True, font_color)
# cheat_big_image =  my_big_font.render('看原图????', True, font_color)
# cheat_image_size = picture_change_image.get_size()
# cheat_pos = (SCREEN_SIZE[0]/2-SET_PANEL_SIZE[0]/3, SCREEN_SIZE[1]/2-SET_PANEL_SIZE[1]/3+3*40)
# quit_game_image = my_font.render('退出游戏', True, font_color)
# quit_game_big_image = my_big_font.render('退出游戏', True, font_color)
# quit_game_image_size = quit_game_image.get_size()
# quit_game_pos = (SCREEN_SIZE[0]/2-SET_PANEL_SIZE[0]/3, SCREEN_SIZE[1]/2-SET_PANEL_SIZE[1]/3+4*40)

# set_panel = False
# set_surface = set_image
# quit_surface = quit_image
# rerand_surface = rerand_image
# puzzle_dim_surface = puzzle_dim_image
# picture_change_surface = picture_change_image
# cheat_surface = cheat_image
# quit_game_surface = quit_game_image

# MAIN_WINDOW_SIZE[0]+1.1*DX

# bg_transform = py.transform.scale(bg, MAIN_WINDOW_SIZE)
# bg_size = bg_transform.get_size()
# w, h = int(bg_size[0]/pdx), int(bg_size[1]/pdy)

# max_size = ((pdx-1)*w+DX, (pdy-1)*h+DY)
# is_win = False

# # 位置和图片分割点
# # bg_slice = {1:(0, 0),2:(w, 0),3:(2*w, 0),4:(0, h),5:(w, h),6:(2*w, h),7:(0, 2*h),8:(w, 2*h), 9:(2*w, 2*h)}
# pos_slice = [(x*w+DX, y*h+DY) for y in range(pdy) for x in range(pdx)]
# bg_slice = [(x*w, y*h) for y in range(pdy) for x in range(pdx)]

# # 选取总数-1个位置和图片
# draw_dict = rerand(pos_slice, bg_slice)

# while True:

#     for event in py.event.get():
#         if event.type == QUIT:
#             py.quit()
#             sys.exit()

#         elif event.type == KEYDOWN:
#             # 移动
#             if event.key == K_UP:
#                 if pos_analysis((bpx, bpy+h), max_size):
#                     draw_dict[(bpx, bpy)] = draw_dict[(bpx, bpy+h)]
#                     del draw_dict[(bpx, bpy+h)] 
                
#             elif event.key == K_DOWN:
#                 if pos_analysis((bpx, bpy-h), max_size):
#                     draw_dict[(bpx, bpy)] = draw_dict[(bpx, bpy-h)]
#                     del draw_dict[(bpx, bpy-h)] 

#             elif event.key == K_LEFT:
#                 if pos_analysis((bpx+w, bpy), max_size):
#                     draw_dict[(bpx, bpy)] = draw_dict[(bpx+w, bpy)]
#                     del draw_dict[(bpx+w, bpy)] 

#             elif event.key == K_RIGHT:
#                 if pos_analysis((bpx-w, bpy), max_size):
#                     draw_dict[(bpx, bpy)] = draw_dict[(bpx-w, bpy)]
#                     del draw_dict[(bpx-w, bpy)] 

#         elif event.type == MOUSEMOTION:
#             # 移动到选项,放大显示
#             if in_area(event.pos, set_pos, set_image_size):
#                 set_surface = set_big_image
#             else:
#                 set_surface = set_image

#             if set_panel:
#                 if in_area(event.pos, quit_pos, quit_image_size):
#                     quit_surface = quit_big_image
#                 else:
#                     quit_surface = quit_image

#                 if in_area(event.pos, rerand_pos, rerand_image_size):
#                     rerand_surface = rerand_big_image
#                 else:
#                     rerand_surface = rerand_image

#                 if in_area(event.pos, puzzle_dim_pos, puzzle_dim_image_size):
#                     puzzle_dim_surface = puzzle_dim_big_image
#                 else:
#                     puzzle_dim_surface = puzzle_dim_image

#                 if in_area(event.pos, picture_change_pos, picture_change_image_size):
#                     picture_change_surface = picture_change_big_image
#                 else:
#                     picture_change_surface = picture_change_image

#                 if in_area(event.pos, cheat_pos, cheat_image_size):
#                     cheat_surface = cheat_big_image
#                 else:
#                     cheat_surface = cheat_image

#                 if in_area(event.pos, quit_game_pos, quit_game_image_size):
#                     quit_game_surface = quit_game_big_image
#                 else:
#                     quit_game_surface = quit_game_image

#         elif event.type == MOUSEBUTTONDOWN:
#             # 设置相关
#             if set_surface == set_big_image and not set_panel:
#                 set_panel = True

#             if set_panel:
#                 if in_area(event.pos, quit_pos, quit_image_size):
#                     # 退出
#                     set_panel = False

#                 elif in_area(event.pos, rerand_pos, rerand_image_size):
#                     # 重新打散
#                     draw_dict = rerand(pos_slice, bg_slice)

#                 elif in_area(event.pos, puzzle_dim_pos, puzzle_dim_image_size):
#                     # 修改拼图维度
#                     pdx += 1 ;pdy += 1
#                     if pdx > 6:
#                         pdx = 3 ;pdy = 3
#                     puzzle_dim_image = my_font.render('当前模式:%dx%d'%(pdx, pdy), True, font_color)
#                     puzzle_dim_big_image = my_big_font.render('当前模式:%dx%d'%(pdx, pdy), True, font_color)
#                     # 使得puzzle_dim能实时改变
#                     puzzle_dim_surface = puzzle_dim_big_image
#                     w, h = int(bg_size[0]/pdx), int(bg_size[1]/pdy)
#                     max_size = ((pdx-1)*w+DX, (pdy-1)*h+DY)
#                     pos_slice = [(x*w+DX, y*h+DY) for y in range(pdy) for x in range(pdx)]
#                     bg_slice = [(x*w, y*h) for y in range(pdy) for x in range(pdx)]
#                     draw_dict = rerand(pos_slice, bg_slice)

#                 elif in_area(event.pos, picture_change_pos, picture_change_image_size):
#                     # 修改图片
#                     tk_window = tk.Tk()
#                     bg_path = filedialog.askopenfile()
#                     tk_window.destroy()
#                     bg = py.image.load(bg_path).convert()
#                     bg_transform = py.transform.scale(bg, MAIN_WINDOW_SIZE)
#                     set_panel = False
#                     draw_dict = rerand(pos_slice, bg_slice)

#                 elif in_area(event.pos, cheat_pos, cheat_image_size):
#                     # 看原图
#                     draw_dict = rerand(pos_slice, bg_slice, 1)

#                 elif in_area(event.pos, quit_game_pos, quit_game_image_size):
#                     # 退出
#                     py.quit()
#                     sys.exit()
                    
#     # 黑块,通过比较和bg_slice的区别找出
#     for pos in pos_slice:
#         if pos not in draw_dict.keys():
#             black_pos = pos
#             bpx ,bpy = black_pos[0], black_pos[1]
#             break
    
#     screen.fill(bg_color)

#     # 显示所有图片,外框线
#     # screen.blit(bg, (0, 0), (w, 2*h, w, h))
#     py.draw.rect(screen, outside_line_color, (DX, DY, MAIN_WINDOW_SIZE[0], MAIN_WINDOW_SIZE[1]), 5)
#     for pos, picture in draw_dict.items():
#         screen.blit(bg_transform, pos, (picture[0], picture[1], w, h))
#     # 显示黑块
#     py.draw.rect(screen, (0,0,0), (bpx ,bpy, w, h))

#     # 区分方块的网格线
#     for i in range(1, pdx):
#         py.draw.aaline(screen, line_color, (i*w+DX, 0+DY), (i*w+DX, pdy*h+DY))
#     for j in range(1, pdy):
#         py.draw.aaline(screen, line_color, (0+DX, j*h+DY), (pdx*w+DX, j*h+DY))

#     # 选项面板
#     screen.blit(set_surface, set_pos)
#     if set_panel:
#         py.draw.rect(screen, panel_color, (SCREEN_SIZE[0]/2-SET_PANEL_SIZE[0]/2, SCREEN_SIZE[1]/2-SET_PANEL_SIZE[1]/2, SET_PANEL_SIZE[0], SET_PANEL_SIZE[1]))
#         py.draw.rect(screen, outside_panel_color, (SCREEN_SIZE[0]/2-SET_PANEL_SIZE[0]/2, SCREEN_SIZE[1]/2-SET_PANEL_SIZE[1]/2, SET_PANEL_SIZE[0], SET_PANEL_SIZE[1]),5)
#         screen.blit(quit_surface, quit_pos)
#         screen.blit(rerand_surface, rerand_pos)
#         screen.blit(puzzle_dim_surface, puzzle_dim_pos)
#         screen.blit(picture_change_surface, picture_change_pos)
#         screen.blit(cheat_surface, cheat_pos)
#         screen.blit(quit_game_surface, quit_game_pos)

#     # 胜利条件
#     for pos, picture in draw_dict.items():
#         if pos[0]-DX != picture[0] or pos[1]-DY != picture[1]:
#             is_win = False
#             break
#     else:
#         is_win = True

#     if is_win and not set_panel:
#         screen.blit(game_win, (MAIN_WINDOW_SIZE[0]/2, MAIN_WINDOW_SIZE[1]/2))

#     py.display.update()




# version2
import os
import os.path
import pygame as py
from pygame.locals import *
import sys
import random
import tkinter as tk
from tkinter import filedialog

SCREEN_SIZE = (800, 640)
MAIN_WINDOW_SIZE = (640, 480)
SET_PANEL_SIZE = (480, 360)
puzzle_dim = (3, 3)

color = {
        'font_color':(150, 0, 150),
        'line_color':(0, 0, 0),
        'outside_line_color':(230, 159, 43),
        'bg_color':(1, 158, 193),
        'panel_color':(97, 134, 171),
        'outside_panel_color':(230, 159, 43),
        }

DX, DY = (SCREEN_SIZE[0]-MAIN_WINDOW_SIZE[0])/2, (SCREEN_SIZE[1]-MAIN_WINDOW_SIZE[1])/2
black_pos = (DX, DY)
pdx ,pdy = puzzle_dim[0], puzzle_dim[1]
bpx ,bpy = black_pos[0], black_pos[1]

py.init()
my_font = py.font.SysFont("隶书", 30)
my_big_font = py.font.SysFont("隶书", 40)
screen = py.display.set_mode(SCREEN_SIZE)

def pos_analysis(black_pos, max_size):
    '''判断黑块的坐标是否超出显示范围'''
    if 0 <= black_pos[0] <= max_size[0]:
        x_in = True
    else:
        x_in = False

    if 0 <= black_pos[1] <= max_size[1]:
        y_in = True
    else:
        y_in = False
    return x_in and y_in

def rerand(pos_slice, bg_slice, cheat=0):
    '''重新打散'''
    if not cheat:
        pos_list = random.sample(pos_slice[1:], pdx*pdy-1)
        picture_list = random.sample(bg_slice[:-1], pdx*pdy-1)
    else:
        pos_list = pos_slice[:-1]
        picture_list = bg_slice[:-1]
    draw_dict = {pos_list[index]:picture_list[index] for index in range (pdx*pdy-1)}
    return draw_dict

class Option_type():
    '''定义设置栏'''
    def __init__(self, string, pos):
        self.pos = pos
        self.image = my_font.render(string, True, color['font_color'])
        self.big_image = my_big_font.render(string, True, color['font_color'])
        self.image_size = self.image.get_size()

        self.surface = self.image

    def in_area(self, mouse_pos):
        '''判断鼠标是否在区域里'''
        if self.pos[0] <= mouse_pos[0] <= self.pos[0] + self.image_size[0] and \
        self.pos[1] <= mouse_pos[1] <= self.pos[1] + self.image_size[1]:
            self.surface = self.big_image
            return True
        else:
            self.surface = self.image
            return False

    def draw(self, screen):
        screen.blit(self.surface, self.pos)


bg = py.image.load(r'C:\Users\banana\Desktop\pygame\pikachu\dog.jpg').convert()
game_win = my_font.render('恭喜,拼图完成!', True, color['font_color'])

outside_option = Option_type('选项', (MAIN_WINDOW_SIZE[0]+1.1*DX, MAIN_WINDOW_SIZE[1]+1.1*DY))

inside_option_string = ['[X]', '重新打散', '当前模式:%dx%d'%(pdx, pdy),'更换图片', '看看原图吧', '退出游戏']
inside_option = []
inside_option_pos = (SCREEN_SIZE[0]/2-SET_PANEL_SIZE[0]/3, SCREEN_SIZE[1]/2-SET_PANEL_SIZE[1]/3)

tem_counter = 0
for element in inside_option_string:
    if element == '[X]':
        inside_option.append(Option_type(element, (SCREEN_SIZE[0]/2+SET_PANEL_SIZE[0]/2-50, SCREEN_SIZE[1]/2-SET_PANEL_SIZE[1]/2)))
    else:
        inside_option.append(Option_type(element, (inside_option_pos[0], inside_option_pos[0]+tem_counter*40)))
        tem_counter += 1


set_panel = False

bg_transform = py.transform.scale(bg, MAIN_WINDOW_SIZE)
bg_size = bg_transform.get_size()
w, h = int(bg_size[0]/pdx), int(bg_size[1]/pdy)

max_size = ((pdx-1)*w+DX, (pdy-1)*h+DY)
is_win = False

# 位置和图片分割点
# bg_slice = {1:(0, 0),2:(w, 0),3:(2*w, 0),4:(0, h),5:(w, h),6:(2*w, h),7:(0, 2*h),8:(w, 2*h), 9:(2*w, 2*h)}
pos_slice = [(x*w+DX, y*h+DY) for y in range(pdy) for x in range(pdx)]
bg_slice = [(x*w, y*h) for y in range(pdy) for x in range(pdx)]
# 选取总数-1个位置和图片
draw_dict = rerand(pos_slice, bg_slice)

while True:

    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            # 移动
            if event.key == K_UP:
                if pos_analysis((bpx, bpy+h), max_size):
                    draw_dict[(bpx, bpy)] = draw_dict[(bpx, bpy+h)]
                    del draw_dict[(bpx, bpy+h)] 
                
            elif event.key == K_DOWN:
                if pos_analysis((bpx, bpy-h), max_size):
                    draw_dict[(bpx, bpy)] = draw_dict[(bpx, bpy-h)]
                    del draw_dict[(bpx, bpy-h)] 

            elif event.key == K_LEFT:
                if pos_analysis((bpx+w, bpy), max_size):
                    draw_dict[(bpx, bpy)] = draw_dict[(bpx+w, bpy)]
                    del draw_dict[(bpx+w, bpy)] 

            elif event.key == K_RIGHT:
                if pos_analysis((bpx-w, bpy), max_size):
                    draw_dict[(bpx, bpy)] = draw_dict[(bpx-w, bpy)]
                    del draw_dict[(bpx-w, bpy)] 


        elif event.type == MOUSEMOTION:
            # 移动到选项,放大显示
            if outside_option.in_area(event.pos):
                pass

            elif set_panel:
                for element in inside_option:
                    if element.in_area(event.pos):
                        pass

        elif event.type == MOUSEBUTTONDOWN:
            # 设置相关
            if outside_option.in_area(event.pos) and not set_panel:
                set_panel = True

            if set_panel:
                if inside_option[0].in_area(event.pos):
                    # 退出
                    set_panel = False

                elif inside_option[1].in_area(event.pos):
                    # 重新打散
                    draw_dict = rerand(pos_slice, bg_slice)

                elif inside_option[2].in_area(event.pos):
                    # 修改拼图维度
                    pdx += 1 ;pdy += 1
                    if pdx > 6:
                        pdx = 3 ;pdy = 3
                    temp_pos = inside_option[2].pos
                    inside_option[2] = Option_type('当前模式:%dx%d'%(pdx, pdy), temp_pos)
                    inside_option[2].draw(screen)

                    w, h = int(bg_size[0]/pdx), int(bg_size[1]/pdy)
                    max_size = ((pdx-1)*w+DX, (pdy-1)*h+DY)
                    pos_slice = [(x*w+DX, y*h+DY) for y in range(pdy) for x in range(pdx)]
                    bg_slice = [(x*w, y*h) for y in range(pdy) for x in range(pdx)]
                    draw_dict = rerand(pos_slice, bg_slice)

                elif inside_option[3].in_area(event.pos):
                    # 修改图片
                    tk_window = tk.Tk()
                    bg_path = filedialog.askopenfile()
                    tk_window.destroy()
                    if bg_path:
                        bg = py.image.load(bg_path).convert()
                        bg_transform = py.transform.scale(bg, MAIN_WINDOW_SIZE)
                        set_panel = False
                        draw_dict = rerand(pos_slice, bg_slice)

                elif inside_option[4].in_area(event.pos):
                    # 看原图
                    draw_dict = rerand(pos_slice, bg_slice, 1)

                elif inside_option[5].in_area(event.pos):
                    # 退出
                    py.quit()
                    sys.exit()
                    
    # 黑块,通过比较和bg_slice的区别找出
    for pos in pos_slice:
        if pos not in draw_dict.keys():
            black_pos = pos
            bpx ,bpy = black_pos[0], black_pos[1]
            break
    
    screen.fill(color['bg_color'])

    # 显示所有图片,外框线
    # screen.blit(bg, (0, 0), (w, 2*h, w, h))
    py.draw.rect(screen, color['outside_line_color'], (DX, DY, MAIN_WINDOW_SIZE[0], MAIN_WINDOW_SIZE[1]), 5)
    for pos, picture in draw_dict.items():
        screen.blit(bg_transform, pos, (picture[0], picture[1], w, h))
    # 显示黑块
    py.draw.rect(screen, (0,0,0), (bpx ,bpy, w, h))

    # 区分方块的网格线
    for i in range(1, pdx):
        py.draw.aaline(screen, color['line_color'], (i*w+DX, 0+DY), (i*w+DX, pdy*h+DY))
    for j in range(1, pdy):
        py.draw.aaline(screen, color['line_color'], (0+DX, j*h+DY), (pdx*w+DX, j*h+DY))

    # 选项面板
    outside_option.draw(screen)
    if set_panel:
        py.draw.rect(screen, color['panel_color'], (SCREEN_SIZE[0]/2-SET_PANEL_SIZE[0]/2, SCREEN_SIZE[1]/2-SET_PANEL_SIZE[1]/2, SET_PANEL_SIZE[0], SET_PANEL_SIZE[1]))
        py.draw.rect(screen, color['outside_panel_color'], (SCREEN_SIZE[0]/2-SET_PANEL_SIZE[0]/2, SCREEN_SIZE[1]/2-SET_PANEL_SIZE[1]/2, SET_PANEL_SIZE[0], SET_PANEL_SIZE[1]),5)
        for element in inside_option:
            element.draw(screen)

    # 胜利条件
    for pos, picture in draw_dict.items():
        if pos[0]-DX != picture[0] or pos[1]-DY != picture[1]:
            is_win = False
            break
    else:
        is_win = True

    if is_win and not set_panel:
        screen.blit(game_win, (MAIN_WINDOW_SIZE[0]/2, MAIN_WINDOW_SIZE[1]/2))

    py.display.update()
