用pygame实现拼图

操作方式:w/上,a/左,s/下,d/右

实现逻辑:
1.整体思路
首先调节图片大小，之后根据图片拼图的规格如：3*3，4*4等来确定每个格子的大小。
计算出将图片绘制位置和图片编号（用以判断是否拼对）绘制图片。

2.移动方式
判定未绘制的褐色方块的移动来完成整体移动

3.更换图片
使用tkinter