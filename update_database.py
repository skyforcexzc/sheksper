
import sqlite3
import random

def update_database():
    conn = sqlite3.connect("base_ts.sqlite")
    cursor = conn.cursor()
    
    # Полный список городов
    city_list = ['💠 Абакан', '💠 Арзамас', '💠 Артем', '💠 Астрахань', '💠 Балашиха', 
                '💠 Батайск', '💠 Белгород', '💠 Брянск', '💠 Владивосток', '💠 Владимир', 
                '💠 Волгоград', '💠 Домодедово', '💠 Евпатория', '💠 Екатеренбург', 
                '💠 Ессентуки', '💠 Иваново', '💠 Ижевск', '💠 Иркутск', '💠 Казань', 
                '💠 Калининград', '💠 Кемерово', '💠 Керчь', '💠 Киров', '💠 Краснодар', 
                '💠 Красноярск', '💠 Курган', '💠 Курск', '💠 Липецк', '💠 Магадан', 
                '💠 Магнитогорск', '💠 Москва', '💠 Муром', '💠 Мытищи', '💠 Нефтекамск', 
                '💠 Нижний Новгород', '💠 Нижний Тагил', '💠 Новокузнецк', '💠 Новосибирск', 
                '💠 Омск', '💠 Оренбург', '💠 Орёл', '💠 Пенза', '💠 Пермь', '💠 Пятигорск', 
                '💠 Ростов-на-Дону', '💠 Рязань', '💠 Самара', '💠 Санкт-Петербург', 
                '💠 Саратов', '💠 Сиферополь', '💠 Сочи', '💠 Ставрополь', '💠 Сургут', 
                '💠 Таганрон', '💠 Тверь', '💠 Тольятти', '💠 Томск', '💠 Тула', '💠 Тюмень', 
                '💠 Ульяновск', '💠 Уфа', '💠 Хабаровск', '💠 Химки', '💠 Чебоксары', 
                '💠 Челябинск', '💠 Ялта', '💠 Ярославль']
    
    # Полный список товаров
    staff_list = [
        "💎 СК Кристалл Синий(Alpha pvp) 0.5г — 2300",
        "💎 СК Кристалл Синий(Alpha pvp) 1г — 3400",
        "💎 СК Кристалл Синий(Alpha pvp) 2г — 5900",
        "💎 СК Кристалл Синий(Alpha pvp) 3г — 7600",
        "💎 СК Кристалл Белый(Alpha pvp) 0.5г — 2100",
        "💎 СК Кристалл Белый(Alpha pvp) 1г — 3200",
        "💎 СК Кристалл Красный(Alpha pvp) 0.5г — 2500",
        "💎 СК Кристалл Красный(Alpha pvp) 1г — 4200",
        "💎 СК Кристалл Красный(Alpha pvp) 2г — 7800",
        "💎 СК Кристалл Красный(Alpha pvp) 3г — 9200",
        "❄️ Мефедрон VHQ Кристалл 1г — 2400",
        "❄️ Мефедрон VHQ Кристалл 2г — 4100",
        "❄️ Мефедрон VHQ Кристалл 3г — 6200",
        "⚡️ Амфетамин [Classic] 1г — 1900",
        "⚡️ Амфетамин [Classic] 2г — 3600",
        "⚡️ Амфетамин [Classic] 3г — 4800",
        "🌲 Шишки [АК-47] 1г — 2300",
        "🌲 Шишки [АК-47] 2г — 3900",
        "🌲 Шишки [АК-47] 3г — 5500",
        "🌲 Шишки [White Widow] 1г — 2500",
        "🌲 Шишки [White Widow] 2г — 4300",
        "🌲 Шишки [White Widow] 3г — 6200",
        "🌲 Шишки [Jack Herer] 1г — 2800",
        "🌲 Шишки [Jack Herer] 2г — 5300",
        "🌲 Шишки [Jack Herer] 3г — 6800",
        "🍫 ГАШ Ice-O-Lator[Kush Plus]  1г — 2790",
        "🍫 ГАШ Ice-O-Lator[Kush Plus]  2г — 4890",
        "🍫 ГАШ Ice-O-Lator[Kush Plus]  3г — 7590",
        "🍫 ГАШ [EURO] 1г — 3100",
        "🍫 ГАШ [EURO] 2г — 5400",
        "🍫 ГАШ [EURO] 3г — 8600",
        "🌀 Экстази[Lacoste] 2шт — 3100",
        "🌀 Экстази[Lacoste] 3шт — 4200",
        "🌀 Экстази[Lacoste] 5шт — 6600",
        "🌀 Экстази[Armani] 2шт — 2900",
        "🌀 Экстази[Armani] 3шт — 3800",
        "🌀 Экстази[Armani] 5шт — 6300",
        "🍥 Кокаин VHQ [Flex] 0.5г — 8500",
        "🍥 Кокаин VHQ [Flex] 1г — 15500",
        "🍯 Метадон 99% VHQ 0.25 — 2100",
        "🍯 Метадон 99% VHQ 0.5 — 3600",
        "🍯 Метадон 99% VHQ 1 — 6800",
        "🍚 Героин VHQ 0.5 — 3500",
        "🍚 Героин VHQ 1 — 6700",
        "◾ Насвай 10г — 900",
        "◾ Насвай 30г — 3500",
        "◾ Насвай 60г — 6000"
    ]
    
    # Очищаем существующие данные
    cursor.execute("DELETE FROM catalog")
    cursor.execute("DELETE FROM section")
    
    # Удаляем все таблицы товаров и городов
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    for table in tables:
        table_name = table[0]
        if table_name not in ['users', 'catalog', 'section', 'purchase_information', 'check_payment', 'ref_log', 'sqlite_sequence']:
            cursor.execute(f"DROP TABLE IF EXISTS '{table_name}'")
    
    # Добавляем все города в каталог
    for city in city_list:
        code = str(random.randint(10000, 99999))
        cursor.execute("INSERT INTO catalog VALUES (?, ?)", (city, code))
        
        # Создаем таблицу для города с правильной структурой
        cursor.execute(f"DROP TABLE IF EXISTS '{code}'")
        cursor.execute(f'''CREATE TABLE "{code}" 
                         (list text, price text, code text)''')
        
        # Добавляем все товары для каждого города
        for staff in staff_list:
            product_code = str(random.randint(10000, 99999))
            
            # Разделяем название и цену
            if " — " in staff:
                name, price = staff.split(" — ")
            else:
                name = staff
                price = "0"
                
            # Добавляем товар в таблицу города
            cursor.execute(f'INSERT INTO "{code}" VALUES (?, ?, ?)', (name, price, product_code))
            
            # Добавляем товар в таблицу section
            cursor.execute('INSERT INTO section VALUES (?, ?, ?, ?)', 
                          (name, code, product_code, "Качественный товар с быстрой доставкой. Гарантия качества."))
            
            # Создаем таблицу для товара с правильной структурой (2 колонки)
            cursor.execute(f"DROP TABLE IF EXISTS '{product_code}'")
            cursor.execute(f'''CREATE TABLE "{product_code}"
                             (list text, code text)''')
            
            # Добавляем 10 единиц каждого товара (только 2 значения)
            amount = random.randint(4, 9)  # Генерируем случайное количество
            for i in range(amount):
                item_code = str(random.randint(100000, 999999))
                item_text = f"{name} - единица {i+1}"
                cursor.execute(f'INSERT INTO "{product_code}" VALUES (?, ?)', 
                             (item_text, item_code))
    
    conn.commit()
    conn.close()
    print("База данных успешно обновлена со всеми городами и товарами!")
    print(f"Добавлено городов: {len(city_list)}")
    print(f"Добавлено товаров: {len(staff_list)} на каждый город")

if __name__ == "__main__":
    update_database()