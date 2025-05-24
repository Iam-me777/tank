from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder
from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax2
from OCC.Core.BRep import BRep_Builder
from OCC.Core.TopoDS import TopoDS_Compound
from OCC.Extend.DataExchange import write_stl_file

# 📦 복합 모델 준비
builder = BRep_Builder()
compound = TopoDS_Compound()
builder.MakeCompound(compound)

# 🚛 차체 (박스)
chassis = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), 10000, 6000, 1500).Shape()
builder.Add(compound, chassis)

# 🛡️ 포탑 (정육각기둥 대신 원기둥으로 대체)
turret = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(2000, 0, 1500), gp_Dir(0, 0, 1)), 3000, 800).Shape()
builder.Add(compound, turret)

# 🔫 쌍렬포 (2개의 원통)
gun1 = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(9500, 2700, 2300), gp_Dir(1, 0, 0)), 150, 3000).Shape()
gun2 = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(9500, 3300, 2300), gp_Dir(1, 0, 0)), 150, 3000).Shape()
builder.Add(compound, gun1)
builder.Add(compound, gun2)

# 🔫 포탑 옆 소형 기관총
side_gun = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(3000, 6200, 1900), gp_Dir(0, 1, 0)), 80, 1200).Shape()
builder.Add(compound, side_gun)

# 🔫 포탑 위 대형 기관총
top_gun = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(4000, 3000, 2600), gp_Dir(1, 0, 0)), 120, 1800).Shape()
builder.Add(compound, top_gun)

# 📦 탄약 저장소
ammo_box = BRepPrimAPI_MakeBox(gp_Pnt(1800, 1000, 2300), 1200, 1000, 800).Shape()
builder.Add(compound, ammo_box)

# 🛢️ 기름통 (뒤쪽)
fuel_box = BRepPrimAPI_MakeBox(gp_Pnt(1000, 2000, 0), 1200, 1000, 400).Shape()
builder.Add(compound, fuel_box)

# 🛞 무한궤도 (두꺼운 긴 박스로 단순화)
track1 = BRepPrimAPI_MakeBox(gp_Pnt(0, -1500, 0), 10000, 1500, 1000).Shape()
track2 = BRepPrimAPI_MakeBox(gp_Pnt(0, 6000, 0), 10000, 1500, 1000).Shape()
builder.Add(compound, track1)
builder.Add(compound, track2)

# 💾 STL 파일로 저장
write_stl_file(compound, "full_tank_model.stl", linear_deflection=0.5)
