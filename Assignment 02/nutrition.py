def main():
    # 1. 建立 FDA 官方 20 种水果的卡路里字典（键统一用小写，严格对应海报拼写）
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }

    # 2. 提示用户输入，并做清洗（去首尾空格 + 转小写）
    item = input("Item: ").strip().lower()

    # 3. 用成员运算符 in 直接查字典，存在才打印，不是水果则安静忽略
    if item in fruits:
        print(f"Calories: {fruits[item]}")


if __name__ == "__main__":
    main()