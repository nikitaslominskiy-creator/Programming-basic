import math
# 1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2*(self.width + self.height)

#     def is_squre(self):
#         if self.width == self.height:
#             return True
#         else:
#             return False

#     def scale(self, factor):
#         self.width *= factor
#         self.height *= factor

#     def describe(self) -> str:
#         area_val = int(self.area()) if self.area().is_integer() else self.area()
#         w_val = int(self.width) if self.width.is_integer() else self.width
#         h_val = int(self.height) if self.height.is_integer() else self.height
#         return f"Obdélník {w_val} × {h_val}, obsah {area_val}"


# rectangles = [
#     Rectangle(3, 4),
#     Rectangle(5, 5),
#     Rectangle(2.5, 8),
#     Rectangle(10, 2)
# ]

# 
# print("Seznam obdélníků:")
# for rect in rectangles:
#     print(rect.describe())

# max_rect = max(rectangles, key=lambda r: r.area())

# print("\nObdélník s největším obsahem:")
# print(f"{max_rect.describe()} (obsah: {max_rect.area()})")
# -----------------------------------------------------------
# 2
# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def length(self) -> float:
#         return math.sqrt(self.x**2 + self.y**2)

#     def add(self, other: 'Vector2D') -> 'Vector2D':
#         return Vector2D(self.x + other.x, self.y + other.y)

#     def scale(self, k: float) -> 'Vector2D':
#         return Vector2D(self.x * k, self.y * k)

#     def dot(self, other: 'Vector2D') -> float:
#         return self.x * other.x + self.y * other.y

#     def angle_to(self, other: 'Vector2D') -> float:
#         len_self = self.length()
#         len_other = other.length()
        
#         if len_self == 0 or len_other == 0:
#             raise ValueError("Nulový vektor nemá definovaný úhel.")
        
        
#         cos_theta = self.dot(other) / (len_self * len_other)
        
        
#         cos_theta = max(-1.0, min(1.0, cos_theta))
        
#         angle_rad = math.acos(cos_theta)
#         return math.degrees(angle_rad)

#     def __repr__(self) -> str:
#         return f"Vector2D({self.x}, {self.y})"




# v1 = Vector2D(3, 4)
# v2 = Vector2D(0, 5)

# print(f"Vektor v1: {v1}, délka: {v1.length()}")
# print(f"Vektor v2: {v2}, délka: {v2.length()}")
# print(f"Součet v1 + v2: {v1.add(v2)}")
# print(f"Vektor v1 zvětšený 2.5krát: {v1.scale(2.5)}")
# print(f"Skalární součin v1 · v2: {v1.dot(v2)}")
# print(f"Úhel mezi v1 a v2: {v1.angle_to(v2):.2f}°")
# -----------------------------------------------------------
# 3