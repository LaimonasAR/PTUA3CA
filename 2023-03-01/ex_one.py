class Computer:

    def __init__(self, cost: int, core_count: int, proc_spd: int) -> None:
        self.cost = cost
        self.core_count = core_count
        self.proc_spd = proc_spd

    def get_speed_per_buck(self) -> float:
        return self.proc_spd / self.cost
    
    def get_core_count(self) -> int:
        return self.core_count
    
class Apple(Computer):

    def __init__(self, ram_amount: int, disk_size: int, dedicated_gpu: bool, cost: int, core_count: int, proc_spd: int) -> None:
        super().__init__(cost, core_count, proc_spd)
        self.ram_amount = ram_amount
        self.disk_size = disk_size
        self.dedicated_gpu = dedicated_gpu
    
    def get_score(self) -> float:
        ram_score = self.ram_amount * 0.2
        disk_score = self.disk_size * 0.3
        spd_perf_score = self.get_speed_per_buck() * 0.5
        return ram_score + disk_score + spd_perf_score
    
    def get_speed_per_buck(self) -> float:
        if self.core_count < 12:
            return super().get_speed_per_buck()
        return 1.5 * self.proc_spd / self.cost
    

mac_book_pro = Apple(ram_amount=16, disk_size= 512, dedicated_gpu=True, cost=5000, core_count=16, proc_spd=3500)

mac_book_pro = Apple(ram_amount=16, disk_size= 512, dedicated_gpu=True, cost=5000, core_count=16, proc_spd=3500)

mac_book_air = Apple(ram_amount=8, disk_size= 256, dedicated_gpu=False, cost=3000, core_count=8, proc_spd=3500)


print(f"Pro speed per buck {mac_book_pro.get_speed_per_buck()}")
print(f"Air speed per buck {mac_book_air.get_speed_per_buck()}")
print(f"Pro score {mac_book_pro.get_score()}")
print(f"Air score {mac_book_air.get_score()}")
