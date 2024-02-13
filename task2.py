from pathlib import Path

def get_cats_info(path):
    cats_inf = []
    try:
        with open (path, "r", encoding= "utf-8") as fh:
            cats = [el.strip() for el in fh.readlines()]
            for cat in cats:
                id, name, age = cat.split(",")
                cat_inf = {"id": id, "name": name, "age": age}
                cats_inf.append(cat_inf)
            return cats_inf
        
    except Exception as error:
        print(f"помилка при обробці файлу: {error}")
        return None

cats_info = get_cats_info(r"E:/GitHub/goit-algo-hw-04/cats.txt")
print(cats_info)