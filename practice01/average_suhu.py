import random

data_suhu = [random.randint(60, 100) for _ in range(10)]
print("Data suhu:", data_suhu)

rata_rata = sum(data_suhu) / len(data_suhu)
print("rata-rata suhu:", rata_rata)
