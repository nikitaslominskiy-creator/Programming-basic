import math
from datetime import datetime
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
class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_val(self) -> float:
        return self.price * self.quantity

    def __repr__(self) -> str:
        return 

class Warehouse:
    def __init__(self):
        self.items: dict[str, Item] = {}
        self.history: list[dict] = []

    def _log_movement(self, action: str, name: str, quantity: int, status: str):
        self.history.append(
            {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S:"),
                "action" : action,
                "item_name" : name,
                "quantity" : quantity,
                "status" : status,
            }
        )

    def find(self, name: str) -> Item | None:
        return self.items.get(name)

    def add(self, name: str, price: float, quantity: int):
        if name in self.items:
            self.items[name].quantity += quantity
            self.items[name].price = price
        else:
            self.items[name] =  Item(name, price, quantity)

        self._log_movement("IN", name, quantity, "SUCCES")

    def remove(self, name: str, quantity: int):
        item = self.find(name)
        if item is None or item.quantity < quantity:
            self._log_movement("OUT", name, quantity, "FAILTURE")
            return False
        else:
            item.quantity -= quantity
            self._log_movement("OUT", name, quantity, "SUCCES")
            return True 

    def total_value(self)  -> float:
        return sum(item.total_val() for item in self.items.values())

    def low_stock(self, limit: int):
        for item in self.items :
            if item.quantity < limit:
                return [item.name]
        return

    def report(self) -> None:
        print("\n" + "=" * 60)
        print(f"{"CURRENT WREHOUSE INVENTORY":^60}")
        print("=" * 60)
        print(f"{"Item Name":<20} | {"Unit Price":>10} | {"Qty":>6} | {"Total Value":>10} |")
        print("-" * 60)

        for item in self.items.values():
            print(f"{item.name:<20} | {item.price:>10} | {item.quantity:>6} | {item.total_val():>10.2f}")

        print("-" * 60)
        print(f"{"Total Warhouse Value":<41} {self.total_value():>10.2f}")

    def item_history(self, name) -> None:
        records = [ record for record in self.history if record["item_name"] == name ]
        print(f"\n--- Movement History for '{name}' ---")
        if not records:
            print("No movement records found.")
            return

        for record in records:
            print(
                f"[{record['timestamp']}] Action: {record['action']:<3} | "
                f"Qty: {record['quantity']:>4} | Status: {record['status']}"
            )
        print("-" * 60)


        

wh = Warehouse()

wh.add("Laptop", 1200.0, 10)
wh.add("Mouse", 25.0, 50)
wh.add("Keyboard", 45.0, 30)
wh.add("Laptop", 1200.0, 5)
wh.report()
wh.remove("Laptop", 3)
wh.remove("Mouse", 45)
wh.remove("Laptop", 20)
wh.remove("Monitor", 10)
wh.report()
wh.item_history("Laptop")
wh.item_history("Mouse")





        