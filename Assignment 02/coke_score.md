### 📝 先顺手纠正几个英文拼写小细节
* 代码里写的 `demonstrations` 在英文里是“示威/演示”的意思，硬币“面额”应该是 **`denominations`**；
* `remiander` 拼写颠倒了，应该是 **`remainder`**（余额/余数）；
* 另外，一瓶可乐是 **50 美分（cents）**，不是 50 美元（dollars）哦（一罐可乐 50 美元也太贵啦哈哈 😄）。


### 🐛 一、捉虫现场：为什么这段代码跑不起来？

#### 1. 老朋友“变量重名覆盖”又来了（Variable Shadowing）
Look at line 1 & line 8：
```python
demonstrations = input("Enter your coins: ")  # 存了用户的输入，比如 "25"
...
for demonstrations in rules:  # ⚠️ 又用了同名的 demonstrations！
```
循环一启动，**用户辛辛苦苦输入的 `"25"` 瞬间被抹杀**，变成了列表里的第一个字典 `{"demonstration": "5", ...}`！

#### 2. 拿“列表”当“字典”查（直接崩溃 `TypeError`）
看第 9 行：
```python
if demonstrations == rules["demonstration"]:
```
* `rules` 外面是方括号 `[]`，它是一个**列表（List）**，里面装了 3 个字典；
* 你不能拿字符串 `"demonstration"` 去查一个列表（列表只能用数字序号 `rules[0]` 去取）。Python 会直接报错崩溃：
  `TypeError: list indices must be integers or slices, not str`

#### 3. 【最核心的思维误区】把“动态持续投币”写死成了“一次性查表”
你想用字典把 `5 -> 还差 45`、`10 -> 还差 40`、`25 -> 还差 25` 全部提前算好写死。
* **思考一下**：现实中的自动售货机，别人难道只投**一枚**硬币就结束吗？
* 如果我先投 `10` 分（剩 40），再投 `25` 分（剩 15），再投 `10` 分（剩 5），最后投 `10` 分（需要找零 5 分）——**用户可能投 2 次、3 次甚至 10 次硬币！** 提前算好余数根本没法应对多次累加！


### 🧠 二、正确的思维模型：自动售货机是怎么工作的？

别去提前背“还差多少钱”，售货机的大脑其实超级简单，只需要**一个记录欠款的变量 + 一个 `while` 循环**：

1. **开机设定价格**：欠款 `amount_due = 50`（一开始还差 50 美分）。
2. **只要还欠着钱（`while amount_due > 0:`），就一直循环**：
   * 在屏幕上显示当前还欠多少：`Amount Due: 50`
   * 请用户投入一枚硬币：`coin = int(input("Insert Coin: "))`
   * 检查这枚硬币是不是合法面额（`25`、`10`、`5` 之一）：
     * **合法**：直接从欠款里扣掉它！`amount_due -= coin`
     * **不合法**（比如投入了 `30` 或 `1`）：机器不认，**什么都不扣**，直接进入下一轮循环再次提示 `Amount Due`！
3. **跳出循环（此时 `amount_due <= 0`）**：
   * 说明钱已经投够了（或者投超了，变成负数了，比如 `-15` 代表多投了 15 美分）。
   * 取绝对值输出找零：`Change Owed: 15`！


### ✨ 三、优化后的标准满分代码

#### 版本一：最纯粹、清晰的 Pythonic 写法（可直接通过 CS50 `check50`）

```python
def main():
    # 1. 初始待付金额为 50 美分，合法面额存入列表
    amount_due = 50
    valid_coins = [25, 10, 5]

    # 2. 只要还欠钱（大于 0），就一直要求投币
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        # 3. 检查是否为机器认可的面额（用成员运算符 in）
        if coin in valid_coins:
            amount_due -= coin  # 等价于 amount_due = amount_due - coin

    # 4. 走出循环说明欠款 <= 0，使用 abs() 取绝对值算出找零
    # 例如 amount_due 为 -15，abs(-15) 就是 15；为 0 时就是 0
    print(f"Change Owed: {abs(amount_due)}")


if __name__ == "__main__":
    main()
```

#### 💡 两个实用新小知识：
1. **`abs()` 函数（Absolute Value）**：数学里的**绝对值**。如果还差 `10` 分时用户投了 `25` 分，`10 - 25 = -15`。`abs(-15)` 会立刻把负号去掉，得到找零 `15`！
2. **用 `in` 代替多个 `or`**：`if coin in [25, 10, 5]:` 比 `if coin == 25 or coin == 10 or coin == 5:` 简洁优雅十倍！

#### 版本二：结合第 3 讲《异常》的“防手滑崩溃加强版”（选学）
如果在本地玩，万一用户不小心输了字母 `"abc"`，`int()` 会直接报 `ValueError`。加上你之前学过的 `try...except` 就无懈可击了：

```python
def main():
    amount_due = 50
    valid_coins = [25, 10, 5]

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            # 输错了字母？跳过这一轮，继续提示投币！
            continue

        if coin in valid_coins:
            amount_due -= coin

    print(f"Change Owed: {abs(amount_due)}")


if __name__ == "__main__":
    main()
```


### 📌 送给你的日常避坑铁律
以后写 `for` 循环时，养成一个**单复数区分**的铁习惯：
* 装很多东西的列表用**复数**（如 `rules`、`coins`、`students`）；
* 循环里每次取出来的单个东西用**单数**（如 `for rule in rules:`、`for coin in coins:`）；
* 这样你永远不会再犯“循环变量不小心把外面的用户输入覆盖掉”的错啦！