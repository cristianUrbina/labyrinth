import pygame

global initial_coords_data
initial_coords_data=[]
f = open('data/maps/initial_coords.txt','r')
data = f.read()
f.close()
for i_coords in data.split('\n'):
    try:
        i_x,i_y=i_coords.split(',')
        initial_coords_data.append((int(i_x),int(i_y)))
    except:
        pass

class gameMap(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.mapPixels = []
        for i in range(width):
            self.mapPixels.append([])
            for j in range(height):
                self.mapPixels[i].append("EMPTY")
    def setObject(self,coords,e_type):
        self.mapPixels[coords[0]][coords[1]]=e_type
    def getObject(self, coords):
        return self.mapPixels[coords[0]][coords[1]]
    def setMapPixels(self,path,p_width,p_height):
        global initial_coords_data
        initial_coords = False
        img = pygame.image.load('data/maps/' + path + '.jpg')
        for y in range(img.get_height()):
            for x in range(img.get_width()):
                color = img.get_at((x,y))
                color = (color[0],color[1],color[2])
                if color == (0,0,0):
                    self.mapPixels[x][y] = "WALL"
                elif color == (254,0,0):
                    self.mapPixels[x][y] = "WIN"
                else:
                    self.mapPixels[x][y] = "AIR"
        return initial_coords_data[int(path[-1])-1]
    def collition(self,coords,p_width,p_height):
        upper_left_corner = coords
        upper_right_corner = (coords[0]+p_width,coords[1])
        lower_left_corner = (coords[0],coords[1]+p_height)
        lower_right_corner = (coords[0]+p_width,coords[1]+p_height)
        if(self.mapPixels[upper_left_corner[0]][upper_left_corner[1]]=="WALL"):
            return True
        if(self.mapPixels[upper_right_corner[0]][upper_right_corner[1]]=="WALL"):
            return True
        if(self.mapPixels[lower_left_corner[0]][lower_left_corner[1]]=="WALL"):
            return True
        if(self.mapPixels[lower_right_corner[0]][lower_right_corner[1]]=="WALL"):
            return True
        return False
    def winner(self,coords,p_width,p_height):
        upper_left_corner = coords
        upper_right_corner = (coords[0]+p_width,coords[1])
        lower_left_corner = (coords[0],coords[1]+p_height)
        lower_right_corner = (coords[0]+p_width,coords[1]+p_height)
        if(self.mapPixels[upper_left_corner[0]][upper_left_corner[1]]=="WIN"):
            return True
        if(self.mapPixels[upper_right_corner[0]][upper_right_corner[1]]=="WIN"):
            return True
        if(self.mapPixels[lower_left_corner[0]][lower_left_corner[1]]=="WIN"):
            return True
        if(self.mapPixels[lower_right_corner[0]][lower_right_corner[1]]=="WIN"):
            return True
        return False
