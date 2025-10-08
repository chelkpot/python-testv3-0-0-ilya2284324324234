# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    a=int(input())
    hours = a // 3600 % 24
    minutes = (a // 60) % 60
    seconds = a % 60
    print(f"{hours}:{minutes:02d}:{seconds:02d}")


   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()