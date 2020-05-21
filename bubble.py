# 定义一个列表
# 比大小
# 注意排序次数
# 注意对比次数
bubble = [45, 32, 8, 33, 12, 22]
# 得出排序次数
for i in range(1, len(bubble)):
    print("这是第", i, "次排序")
    # 对比的次数
    for j in range(len(bubble) - i):
        print("对比了", j + 1, "次")
        # 判断哪个更大，交换发生在对比的时候，所以和排序次数没有任何关系
        if bubble[j] > bubble[j + 1]:
            # 如果第一个数字比第二个数字大，就交换
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]
print(bubble)

# # 将bubble[0]赋值给temp，temp=bubble[0]，bubble[0]也等于bubble[0]
# temp = bubble[0]
# # 将bubble[1]赋值给bubble[0]，temp=bubble[0]，bubble[0]等于bubble[1]，bubble[1]还等于bubble[1]
# bubble[0] = bubble[1]
# # temp=bubble[0]，bubble[0]等于bubble[1]，bubble[1]等于bubble[0]
# bubble[1] = temp
