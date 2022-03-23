import sys
x,y,w,h = map(int,sys.stdin.readline().split())

dx=w-x if x>=w/2 else x
dy=h-y if y>=h/2 else y
print(min(dx,dy))