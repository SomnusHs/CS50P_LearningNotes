def main():
  time = input("请输入时间（24 小时制，格式为 HH:MM）：").strip()
  precise_hours = convert(time)
  print(f"时间 {time} 对应的小时数为 {precise_hours}")
  if 7.0 <= precise_hours < 8.0:
    print("早餐时间")
  elif 12.0 <= precise_hours < 13.0:
    print("午餐时间")
  elif 18.0 <= precise_hours < 19.0:
    print("晚餐时间")

# 将 24 小时制的字符串形式时间转换为对应的小时数（浮点数）
def convert(time):
  fraction = time.split(":")
  hours = int(fraction[0])
  minutes = int(fraction[1])
  return float(hours + minutes / 60)


if __name__ == "__main__":
  main()