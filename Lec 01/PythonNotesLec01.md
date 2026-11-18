# 目录
1. **核心概念：什么是条件语句？（Conditionals）**
2. **比较运算符（Comparison Operators）与布尔类型（bool）**
3. **条件控制三部曲：`if`、`elif`、`else` 的演进过程**
4. **逻辑运算符（Logical Operators）：`or` 与 `and` 的妙用**
5. **取模运算符 `%` 与“Pythonic”代码风格（以判断奇偶为例）**
6. **现代语法：`match...case` 模式匹配（Pattern Matching）**
7. **小白必看避坑指南（语法细节与高频错误）**

## 一、核心概念：什么是条件语句？（Conditionals）

* **生活比喻**：就像你走到一个十字路口，如果是红灯就停下，绿灯就通行。
* **程序中的作用**：让计算机能够**根据不同的情况做出不同的决策**（Make decisions），从而决定走哪一条逻辑分支（Control flow，控制流）。

## 二、比较运算符（Comparison Operators）与布尔类型（bool）

进行条件判断的前提是“提问”，在 Python 中我们通过**比较运算符**向计算机提问，计算机只会回答你两种结果：**`True`（真/对）** 或 **`False`（假/错）**。

### 1. 常见比较运算符一览表

| 运算符 |         英文名称         |           含义           |                示例                 |
| :----: | :----------------------: | :----------------------: | :---------------------------------: |
|  `>`   |       Greater than       |           大于           |      `5 > 3`（结果为 `True`）       |
|  `>=`  | Greater than or equal to |        大于或等于        |      `5 >= 5`（结果为 `True`）      |
|  `<`   |        Less than         |           小于           |      `2 < 4`（结果为 `True`）       |
|  `<=`  |  Less than or equal to   |        小于或等于        |     `3 <= 2`（结果为 `False`）      |
|  `==`  |         Equality         | **等于（比较是否相等）** |              `x == y`               |
|  `!=`  |       Not equal to       |        **不等于**        | `x != y`（`!` 读作 bang，表示“非”） |

> ⚠️ **超高频误区（新手必看）**：
> * 单等号 `=`：是**赋值（Assignment）**，表示把右边的值装进左边的变量里（如 `x = 1`）。
> * 双等号 `==`：是**判断相等（Equality）**，用来比较左右两边是否相同（如 `x == 1`）。

### 2. 布尔类型（Boolean / `bool`）
* Python 的一种基本数据类型（Data Type），取值**只有两种**：`True` 和 `False`（注意首字母必须大写！）。
* 这种结果非真即假的提问表达式，叫做**布尔表达式（Boolean Expression）**。

## 三、条件控制三部曲：`if`、`elif`、`else`

视频中通过一个比大小的程序 `compare.py`，生动展示了代码从“能跑”到“优雅”的三次进化。

### 版本 1：三个独立的 `if`（低效、啰嗦）
```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
```
* **问题所在**：这 3 个 `if` 是相互独立的。即使 `x < y` 已经是 `True`，程序依然会傻乎乎地再去问第 2 个和第 3 个问题，浪费了计算资源。

### 版本 2：引入 `elif`（互斥分支，效率提升）
* **`elif`** 是 **else if**（否则如果）的缩写。
```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
```
* **改进**：建立了**互斥关系（Mutually Exclusive）**。只要前面有一个条件满足（为 `True`），后面的所有 `elif` 会被直接跳过，程序立刻结束。

### 版本 3：引入 `else`（逻辑闭环，最优雅）
* **思考**：两个数比大小，如果既不小于、也不大于，那它们只能是相等的！根本不需要再问第三次。
* **`else`**（否则）：作为全能兜底（Catch-all），在前面所有条件都不满足时执行，后面**不写任何判断条件**。
```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```

## 四、逻辑运算符（Logical Operators）：`or` 与 `and`

当一个问题需要结合多个条件时，我们使用逻辑运算符。

### 1. `or`（或者）：只要满足其中一个即可
如果我们只想判断两数是否“不相等”：
* **初步写法**：
  ```python
  if x < y or x > y:
      print("x is not equal to y")
  else:
      print("x is equal to y")
  ```
* **更优写法（直接使用 `!=` 运算符）**：
  ```python
  if x != y:
      print("x is not equal to y")
  else:
      print("x is equal to y")
  ```
  *(注：也可以写成 `if x == y:` 并调换执行内容，效果完全一致。)*

### 2. `and`（并且 / 与）：必须同时满足所有条件
视频中用成绩评级程序 `grade.py` 演示了 `and` 的使用与简化：

* **写法 A（常规使用 `and`）**：
  ```python
  score = int(input("Score: "))
  
  if score >= 90 and score <= 100:
      print("Grade: A")
  elif score >= 80 and score < 90:
      print("Grade: B")
  elif score >= 70 and score < 80:
      print("Grade: C")
  elif score >= 60 and score < 70:
      print("Grade: D")
  else:
      print("Grade: F")
  ```

* **写法 B（Python 独有的链式比较，Chained Comparisons）**：
  像数学课一样连续书写：
  
  ```python
  if 90 <= score <= 100:
      print("Grade: A")
  elif 80 <= score < 90:
      print("Grade: B")
  # ...依此类推
  ```
  
* **写法 C（最高效的逻辑简化）**：
  由于条件是**自上而下**依次判断的，如果一个人没有进入 `>= 90` 的分支，说明他的分数**一定小于 90**，因此下一行无需再判断 `< 90`！
  
  ```python
  if score >= 90:
      print("Grade: A")
  elif score >= 80:
      print("Grade: B")
  elif score >= 70:
      print("Grade: C")
  elif score >= 60:
      print("Grade: D")
  else:
      print("Grade: F")
  ```

## 五、取模运算符 `%` 与自定义布尔函数

视频中通过判断数字奇偶（Parity）的程序 `parity.py`，讲到了非常实用的算术技巧和编程思想。

### 1. 取模运算符（Modulo Operator / `%`）
* **作用**：求两个数相除后的**余数（Remainder）**。
* **奇偶性定义**：
  * **偶数（Even）**：能被 2 整除，即余数为 0：`n % 2 == 0`
  * **奇数（Odd）**：除以 2 余 1：`n % 2 != 0`

### 2. 自定义返回布尔值的函数：三种层级的写法

我们可以自己写一个名为 `is_even` 的函数，来判断是否为偶数：

#### ① 初学者写法（容易理解）
```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

#### ② 单行三元表达式写法（Ternary Conditional）
```python
def is_even(n):
    return True if n % 2 == 0 else False
```

#### ③ 终极“Pythonic”写法（最优雅、最地道）
* **底层原理**：`n % 2 == 0` 本身就是一个布尔表达式，计算后就是 `True` 或 `False`。因此，**直接把这个表达式的结果返回即可**！
```python
def is_even(n):
    return (n % 2 == 0)
```

主程序调用时非常直观，就像在读英语：
```python
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

main()
```

## 六、现代语法：`match...case` 模式匹配（Pattern Matching）

这是 Python 3.10 引入的新特性（相当于其他语言里的 `switch...case`），专门用于处理**多个固定值匹配**的场景。视频中使用哈利波特学院分配程序 `house.py` 作演示。

### 1. 基本写法
```python
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # 下划线表示通配符，即“其他所有名字”
        print("Who?")
```

### 2. 合并情况（使用竖线 `|` 表示“或”）
可以将同一学院的人物合并在同一个 `case` 中，极大减少重复代码：
```python
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```
* **`_`（通配符 / Wildcard）**：等同于传统 `if` 结构中的 `else`，负责兜底。
* **特点**：Python 的 `match` 执行完匹配的分支就会自动退出，**不需要**像 C/Java 那样写 `break` 语句。

## 七、小白避坑指南（关键细节与高频错误）

1. **冒号（Colon `:`）千万不能漏**
   * 凡是带有分界、引出下一段代码的语句行（如 `if`、`elif`、`else`、`def`、`match`、`case`），**行尾都必须有英文字符冒号 `:`**。
2. **强制缩进（Indentation）**
   * Python 不用大括号 `{}` 来圈定代码块，完全依靠**缩进**（通常为 4 个空格或一次 Tab 键）。
   * 属于某个分支的代码必须向右缩进对齐，缩进错误会直接引发 `IndentationError`。
3. **分清“全是 `if`”与“`if...elif...else`”的区别**
   * 在成绩打分等递进区间中，如果全用 `if`，输入 `95` 会同时满足 `>=90`、`>=80`、`>=70`、`>=60`，导致屏幕打印出 `A B C D` 连串错误输出。需要互斥的分支务必使用 `elif`。
