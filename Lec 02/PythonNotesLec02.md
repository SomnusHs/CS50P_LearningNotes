# 目录

1. **为什么要用循环？（Why Loops?）**
2. **条件循环：`while` 循环与死循环**
3. **计数与遍历：`for` 循环与 `range()`**
4. **循环核心控制：`break`、`continue` 与输入验证**
5. **深入序列结构：列表（List）与索引（Index）**
6. **映射数据结构：字典（Dictionary）与键值对（Key-Value）**
7. **综合实战（Mario 案例）：嵌套循环（Nested Loops）与抽象化（Abstraction）**
8. **小白必背心法与高频避坑指南**

## 一、为什么要用循环？（Why Loops?）

课程由一个简单的任务开始：**让小猫叫三次（输出三次 `"meow"`）**。

### 最原始的写法（低效、无法扩展）

```python
print("meow")
print("meow")
print("meow")
```

* **问题所在**：
  1. **代码冗余**：如果猫要叫 50 次、1000 次，复制粘贴会把人逼疯。
  2. **维护极差**：如果突然要把猫叫改成狗叫（`"woof"`），你需要手动改动几百处。
* **核心哲学**：程序员的核心准则之一是 **DRY（Don't Repeat Yourself，不要重复自己）**。如果同一件事要做多次，就必须交给**循环（Loop）**。

## 二、条件循环：`while` 循环

`while` 的字面意思是“当……的时候”。只要后面的**布尔表达式（Boolean Expression）**结果为 `True`，它就会一直执行循环体内的代码。

### 1. 倒数计数法

```python
i = 3
while i != 0:
    print("meow")
    i = i - 1
```

* **运行逻辑**：
  1. `i = 3`，满足 `3 != 0`，打印 `meow`，`i` 变成 `2`；
  2. 满足 `2 != 0`，打印 `meow`，`i` 变成 `1`；
  3. 满足 `1 != 0`，打印 `meow`，`i` 变成 `0`；
  4. 遇到 `0 != 0` 为 `False`，循环结束。

### 2. 死循环（无限循环 / Infinite Loop）与强制终止

* 如果漏写了 `i = i - 1`，`i` 永远是 `3`，程序就会无限打印 `"meow"`。
* 💡 **紧急救命快捷键**：若程序陷入死循环，在终端（Terminal）按下 **`Ctrl + C`**（表示 Cancel/Interrupt，中断），强行停止程序。

### 3. 程序员的行业惯例：从 0 开始计数（0-indexed）

在计算机世界里，程序员更习惯**从 0 开始正向计数**，而不是从 1 开始：

```python
i = 0
while i < 3:
    print("meow")
    i += 1  # 等价于 i = i + 1
```

> ⚠️ **语法细节**：
>
> * `i += 1` 称为**增量赋值运算符（Augmented Assignment Operator）**。
> * Python 中**没有**像 C/Java/JS 中的 `i++` 或 `i--` 语法，请统一使用 `+= 1` 或 `-= 1`。

## 三、计数与遍历：`for` 循环与 `range()`

`while` 循环更适合“不知道具体要转多少次，只知道满足某个条件才停”的场景；而当你**明确知道要执行多少次**时，Python 推荐使用 **`for` 循环**。

### 1. 列表（List）与 `for` 循环的初遇

列表（List）是 Python 的基本复合数据类型，用**方括号 `[]`** 表示，里面存放用逗号分隔的数据：

```python
for i in [0, 1, 2]:
    print("meow")
```

* 每次循环，Python 都会依次把列表里的每一个值赋值给变量 `i`。

### 2. 批量生成数字神器：`range()` 函数

显然，我们不能手写一个包含 100 万个数字的列表。Python 提供了内置函数 `range()`：

```python
for i in range(3):
    print("meow")
```

* `range(3)` 会自动生成：`0, 1, 2`（包含 3 个数字，从 0 开始，到 3 截止，**左闭右开，不含 3**）。

### 3. Pythonic 习惯：下划线占位符 `_`（Dummy Variable）

如果循环变量（如上面的 `i`）只是为了控制次数，后续代码**根本用不到它**，地道的 Python 程序员会将其命名为一个**单下划线 `_`**：

```python
for _ in range(3):
    print("meow")
```

* 这在视觉上告诉其他阅读代码的人：“这个变量的值不重要，我只关心执行了 3 次”。

### 4. 语言彩蛋：字符串乘法（String Multiplication）

Python 允许将字符串和数字相乘：

```python
print("meow\n" * 3, end="")
```

* `"meow\n" * 3` 会直接产生 `"meow\nmeow\nmeow\n"`（`\n` 代表**换行符 / Newline**）。
* 结尾加上 `end=""` 是为了抵消 `print()` 默认自带的一次额外换行。
* *教授点评*：这种写法很酷炫，但在大型复杂程序中，`for` 循环往往具有更好的可读性（Readability）。

## 四、循环核心控制：`break`、`continue` 与输入验证

如何让用户输入一个合格的正整数？如果用户乱输入（负数、0），我们该怎么一直要求他重输，直到正确为止？

### 1. 经典范式：`while True` + `break`

```python
while True:
    n = int(input("What's n? "))
    if n > 0:
        break  # 只要 n > 0，立即跳出循环！

for _ in range(n):
    print("meow")
```

* **`while True`**：故意创建一个**死循环**。
* **`break` 关键字**：其作用是**立刻打断并跳出**当前包裹它的最内层循环。
* **`continue` 关键字**：放弃执行本次循环后续的代码，直接**重新回到循环开头**开始下一次判断。

### 2. 结合自定义函数：巧用 `return` 替代 `break`

在自定义函数中，`return` 具有天然跳出循环的威力：

```python
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n  # 既跳出了 while 循环，又把值返回了出去！

def meow(n):
    for _ in range(n):
        print("meow")

main()
```

## 五、深入序列结构：列表（List）

视频通过哈利波特（Hogwarts）学生名单的例子，逐步展开了数据结构教学。

### 1. 列表的定义与 0 索引（0-indexed）

```python
students = ["Hermione", "Harry", "Ron"]

print(students[0])  # Hermione (第 1 个元素)
print(students[1])  # Harry     (第 2 个元素)
print(students[2])  # Ron       (第 3 个元素)
```

### 2. 直接遍历元素（最推荐、最地道）

```python
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)
```

* 计算机依次取出列表中的每一个名字，赋给临时变量 `student` 并打印。

### 3. 按序号索引遍历：`len()` 与 `range()` 的组合技

如果你不仅想打印名字，还想打印他们的序号（1, 2, 3），可以使用 `len()`（Length，长度函数）：

```python
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])
```

* `len(students)` 结果是 `3`。
* `range(len(students))` 即 `range(3)`，生成 `0, 1, 2`。
* `i + 1` 让展示给人类看的序号从 1 开始。

## 六、映射数据结构：字典（Dictionary / `dict`）

当我们需要将两组数据关联起来时（例如：学生和所属学院），如果用两个独立的列表（`students` 和 `houses`），极易因位置对错产生混乱。这时候就需要**字典（Dictionary）**。

### 1. 字典的核心：键值对（Key-Value Pairs）

字典就像现实里的英汉词典：你查一个**单词（键 / Key）**，它会给你对应的**释义（值 / Value）**。

* 语法：使用**花括号 `{}`**，格式为 `键: 值`，项与项之间用逗号分隔。

```python
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
```

### 2. 通过键（Key）获取值（Value）

```python
print(students["Hermione"])  # 输出: Gryffindor
```

### 3. 遍历字典

> ⚠️ **关键概念**：用 `for` 循环直接遍历字典时，**变量获取到的是每个“键（Key）”**，而不是值！

```python
for student in students:
    # student 是键（名字），students[student] 是值（学院）
    print(student, students[student], sep=", ")
```

### 4. 进阶结构：字典列表（List of Dictionaries）

现实中的数据往往不止两个属性。如果一个学生既有**名字（name）**、**学院（house）**，还有**守护神（patronus）**呢？
我们可以创建一个**外层是列表，内层是字典**的复合结构：

```python
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
```

#### 知识点补充：`None` 关键字

* 德拉科·马尔福没有明确的守护神，Python 专门用 **`None`**（首字母必须大写）来表示**“空”、“无”或“缺失的值”（The absence of a value）**。

## 七、综合实战（Mario 案例）：嵌套循环与抽象化

课程最后以任天堂游戏《超级马里奥》中的砖块为例，展示了如何用循环从一维进化到二维。

### 目标 1：打印一列垂直砖块（Column）

```python
def print_column(height):
    for _ in range(height):
        print("#")
```

### 目标 2：打印一行水平砖块（Row）

```python
def print_row(width):
    print("?" * width)
```

### 目标 3：打印 $3 \times 3$ 的二维砖块方阵（Square / Grid）

#### 方法 A：嵌套循环（Nested Loops / 双重循环）

就像打字机打字一样：**外层循环负责“行”（纵向换行），内层循环负责“每一行里的每一块砖”（横向打印）**。

```python
def print_square(size):
    for i in range(size):          # 外层循环：遍历每一行
        for j in range(size):      # 内层循环：打印这一行里的每块砖
            print("#", end="")     # 打印砖块，但不要换行！
        print()                    # 这一行所有砖打印完毕，输出一个空 print() 负责换行

print_square(3)
```

#### 方法 B：利用字符串乘法简化

```python
def print_square(size):
    for i in range(size):
        print("#" * size)
```

#### 方法 C：工程最高境界——代码分解与抽象（Abstraction）

把“打印一行”的工作交给专门的子函数，主函数只负责调度：

```python
def print_square(size):
    for _ in range(size):
        print_row(size)  # 我不管一行怎么打，交给 print_row 去办！

def print_row(width):
    print("#" * width)
```

## 八、小白必背心法与高频避坑指南

1. **死循环排查**：写 `while` 循环时，第一件事检查**循环变量是否有朝向终止条件的更新语句**（如 `i += 1`）。
2. **区分括号的使用场景**：
   * 小括号 `()`：用于**调用函数**（如 `print()`、`range()`）。
   * 中括号 `[]`：用于**定义列表**（如 `[1, 2, 3]`）或**索引取值**（如 `students[0]`）。
   * 大括号 `{}`：用于**定义字典**（如 `{"name": "Harry"}`）。
3. **`break` 只能打断一层**：如果你的代码是双重嵌套循环，内层的 `break` 只能跳出内层循环，不能直接终止外层循环。
4. **抽象化思维（Abstraction）**：不要把所有复杂逻辑一股脑塞在一个函数里。像拼积木一样，把大问题拆成几个小函数（如 `print_square` 内部调用 `print_row`），这才是专业程序员的思考方式！