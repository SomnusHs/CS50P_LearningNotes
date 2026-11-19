这是针对 CS50P 第二周 **`nutrition.py`** 的标准满分参考答案（已严格核对美国 FDA 官方水果海报的 20 种水果拼写、卡路里数值及 CS50P 测试格式，可直接通过 `check50` 检测）：

```python
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
```


### 💡 核心亮点与防坑解析（保姆级复盘）

1. **输入/输出完全符合题目规范**：
   * 输入提示语为 `Item: `，输出格式为 `Calories: 130`；如果输入非水果（如 `Tomato`），因为条件不成立且没有 `else`，程序会直接安静退出，不输出任何多余空行。
2. **直接 `if item in fruits:`，千万别画蛇添足写 `for` 循环！**
   * 很多做这道题的初学者喜欢多此一举地写一个 `for fruit in fruits:` 去一个一个比对。
   * **字典（Dictionary）最大的威力就是“瞬间直达”**（O(1) 查找速度）：写 `if item in fruits:`，Python 内部一眨眼就能判断它是不是字典里的键，既干净又高效，还能防止在循环里不小心写出多余的 `print()` 导致测试失败。
3. **复习拓展（结合你之前学过的 `.get()` 写法）**：
   如果不用 `in` 先检查，也可以用我们前面在 `extensions.py` 聊过的字典 `.get()` 方法来避免 `KeyError`：
   ```python
   calories = fruits.get(item)
   if calories is not None:  # 只要不是 None，说明在字典里找到了！
       print(f"Calories: {calories}")
   ```
   *(注：这种写法同样完全正确，而且只需查询一次字典。现阶段两种写法你都可以熟练掌握！)*