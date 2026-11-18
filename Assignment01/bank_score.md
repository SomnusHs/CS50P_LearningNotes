### 🧐 找出隐藏的两个“致命 Bug”

#### 1. “以 hello 开头” $\neq$ “完全等于 hello”
* **题目原文**：*“If the greeting **starts with** 'hello'...”*（如果以 hello 开头）。
* **你的代码**：`if Greeting == "hello":`（这里要求**完全等于**）。
* **案发现场**：
  在《宋飞正传》里，经典的问候语往往是 **`"Hello, Newman"`** 或者现实中的 `"Hello there"`。
  * 经过清洗后，变量变成了 `"hello, newman"`；
  * 第一关 `Greeting == "hello"` 判定为 `False`；
  * 进入第二关：`Greeting[0] == "h"` 判定为 `True`，程序打印了 **`$20`**！
  * **结果**：明明人家热情地打了 `"Hello"`，却少拿了钱，银行被投诉了！

#### 2. 索引越界引发程序崩溃（`IndexError`）
* **案发现场**：
  如果用户什么都没敲，**直接按了回车（Enter）**，或者只敲了几个空格后回车。
  * 经过 `.strip()` 清洗后，`Greeting` 变成了一个**空字符串（`""`）**。
  * 走到第二行：`elif Greeting[0] == "h":`
  * 此时由于空字符串里面**根本没有第 0 个字符**，Python 会瞬间爆炸，弹出刺眼的红字：
    `IndexError: string index out of range`（索引越界错误）。


### 💡 规范细节（PEP 8 命名规范）

在 Python 中，有一个官方的代码风格指南叫 **PEP 8**：
* **普通变量名**推荐使用**纯小写**，多个单词用下划线连接（如 `greeting`、`user_greeting`）。
* **首字母大写的名字**（如 `Greeting`）在 Python 里通常特指**“类”（Class）**。所以建议把变量名改成纯小写的 `greeting`。


### ✨ 终极优化版代码

解决上面两个问题最好的武器，就是 Python 专有的字符串方法 **`.startswith()`**：
1. 它能正确匹配 `"hello, world"` 这种开头；
2. **最绝的是它具有“天然免疫”空字符串的特性**：即使字符串是空的，`.startswith("h")` 也只会安全地返回 `False`，而绝对**不会崩溃报 `IndexError`**！

```python
def main():
    # 1. 规范变量名为小写 greeting
    # 2. 提示词与 CS50 题目要求保持一致（通常要求为 "Greeting: "）
    greeting = input("Greeting: ").lower().strip()

    # 3. 使用 startswith 判断前缀
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
```

此外，更简洁的版本如下：
```python
def main():
    greeting = input("Greeting: ").lower().strip()

    # 语法：结果A if 条件1 else (结果B if 条件2 else 兜底结果C)
    print("$0" if greeting.startswith("hello") else ("$20" if greeting.startswith("h") else "$100"))

main()
```

此外，用list的版本如下：
```python
def main():
    greeting = input("Greeting: ").lower().strip()

    # 1. 用列表存储所有的规则（前缀, 对应的金额），按优先级顺序排列
    #    列表中每个元素是一个元组（Tuple / 类似小列表）
    rules = [
        ("hello", "$0"),
        ("h", "$20")
    ]

    # 2. 遍历列表中的每条规则
    for prefix, payout in rules:
        if greeting.startswith(prefix):
            print(payout)
            return  # 匹配到直接退出函数，不再继续比对

    # 3. 如果列表中所有规则都没命中，输出兜底的 $100
    print("$100")

main()
```