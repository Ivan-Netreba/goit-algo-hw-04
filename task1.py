from pathlib import Path

def total_salary(path):
    try:
        with open (path, "r", encoding= "utf-8") as fh:
            lines = [el.strip() for el in fh.readlines()]
            total_salary = 0
            num_developers = len(lines)
            for line in lines:
                _, salary = line.split(",")
                total_salary += int(salary)
                averege_salary = total_salary / num_developers
        return (total_salary, averege_salary)
    
    except Exception as error:
        print(f"помилка при обробці файлу: {error}")
        return None

total, average = total_salary(r"E:/GitHub/goit-algo-hw-04/file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

