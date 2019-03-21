# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.
#
# Written by Di Peng and Eric Martin for COMP9021


from math import pi, hypot
import copy

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x:.2f}, {self.y:.2f})'

class Disk:
    # replace pass above with your code
    area = 0
    
    def __init__(self, *, centre = Point(0,0), radius = 0.00):
        self.centre = centre
        self.radius = radius
        self.area = pi * (radius ** 2)

    def __repr__(self):
        return f'Disk({self.centre}, {self.radius:.2f})'

    def change_radius(self, radius):
        self.radius = radius
        self.area = pi * (radius ** 2)
        
    def intersects(self, disk):
        return ((disk.centre.x - self.centre.x) ** 2 + (disk.centre.y - self.centre.y) ** 2) ** 0.5 <= (disk.radius + self.radius)

    def absorb(self, disk):
        new_disk = Disk()
        centre_to_centre = hypot(self.centre.x - disk.centre.x, self.centre.y - disk.centre.y)
        if centre_to_centre < abs(self.radius - disk.radius):
            if self.radius > disk.radius:
                return self
            else:
                return disk
        else:
            x_distance = ((centre_to_centre + self.radius - disk.radius) / 2)
            new_disk_radius = x_distance + disk.radius
            new_disk_x = (x_distance / centre_to_centre) * (self.centre.x - disk.centre.x) + disk.centre.x
            new_disk_y = (x_distance / centre_to_centre) * (self.centre.y - disk.centre.y) + disk.centre.y
        return Disk(centre = Point(new_disk_x,new_disk_y), radius = new_disk_radius)
