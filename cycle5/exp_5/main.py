import graphics.rectangle as rect
import graphics.circle as circ
import graphics.graphics_3d.cuboid as cub
import graphics.graphics_3d.sphere as sphr

lenrec=int(input("enter the length of the rectangle:"))
breadthrec=int(input("enter the breadth of rectangle:"))
print("rectangle area:",rect.area(lenrec,breadthrec))
print("perimeter of rectangle:",rect.perimeter(lenrec,breadthrec))

radi=int(input("enter the radius of the circle:"))
print("circle perimeter:",circ.perimeter(radi))
print("circle area:",circ.area(radi))

len=int(input("enter the length of the cuboid: "))
bred=int(input("enter the breadth of the cuboid:"))
height=int(input("enter the height of the cuboid"))
print("cuboid volume:",cub.volume(len,bred,height))
print("cuboid surface area:",cub.surface_area(len,bred,height))

radius=int(input("enter the radius of the sphere: "))
print("sphere volume:",sphr.volume(radius))
print("sphere surface area:",sphr.surface_area(radius))
