import bpy
from math import acos, sin , atan2 , pi, asin
import os

def getAvgNorm():
    normals = [f.normal for f in bpy.context.active_object.data.polygons if f.select]
    avg = [0,0,0]
    for n in normals:
        for i in range(3): avg[i] += n[i]
    for i in range(3): avg[i] = avg[i]
    mag = (avg[0]**2 + avg[1]**2 + avg[2]**2)**0.5
    print(f"mag: {mag}")
    return avg[0]/mag, avg[1]/mag, avg[2]/mag
 

os.system("clear")
print("*"*40)
#set object mode to confirm selection
bpy.ops.object.mode_set(mode="OBJECT")
bpy.context.object.rotation_euler = 0,0,0
norm = getAvgNorm()
print(norm)

print("-"*40)
bpy.context.object.rotation_mode = "AXIS_ANGLE"
bpy.context.object.rotation_axis_angle[3] = 1 - (1 - norm[2])/2
bpy.context.object.rotation_axis_angle[1] = norm[0]/2
bpy.context.object.rotation_axis_angle[2] = norm[1]/2
bpy.context.object.rotation_axis_angle[0] = pi
bpy.ops.object.transform_apply(rotation=True)
print("#"*40)

bpy.ops.object.mode_set(mode="EDIT")
