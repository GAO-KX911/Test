def choose_extinguihser(polarity, boiling_point):
    if polarity > 4 or boiling_point > 70:
        return "AR泡沫"
    elif polarity < 4 and boiling_point < 70:
        return "AF泡沫"
    elif polarity < 4 and boiling_point >= 70:
        return "AF泡沫 或 AR泡沫"
    else:
        return "无法判断，请检查输入的值"



if __name__ == "__main__":
    print("=====灭火剂判断程序=====")
    print("输入exit退出程序。\n")
    while True:
        polarity_input = input("请输入极性值：")
        if polarity_input.strip().lower() == "exit":
            print("程序已退出")
            break


        boiling_input = input("请输入沸点（摄氏度）：")
        if boiling_input.strip().lower() == "exit":
            print("程序已退出")
            break

        try:
            polarity = float(polarity_input)
            boiling_point = float(boiling_input)
            result = choose_extinguihser(polarity, boiling_point)
            print(f"\n推荐使用的灭火剂类型为：{result}\n")
        except ValueError:
            print("输入错误！！！")
