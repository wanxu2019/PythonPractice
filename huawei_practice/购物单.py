# -*- coding: utf-8 -*-
#  @Time        :    2018/9/4 23:41
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    购物单.py
#  @Place       :    dormitory

'''
思路：
主件与附件的信息应当存在一起，进行选择时也应当统筹考虑，附件不能独立地被选择，只能作为主件选择范围的一种增强。由于附件数量有限，最终选择范围如下：
（1）不选主件
（2）只选主件
（3）选主件+附件1
（4）选主件+附件2
（5）选主件+附件1+附件2
启示：
有依赖的背包问题遍历的一定是主件，附件不能独立参与遍历，动规的递推方程可以通过多次求值得到，以解决更加复杂的问题，不一定一步做完。
'''
while True:
    try:
        N, m = map(int, raw_input().split())
        main_components = [[0] * 3 for i in range(m)]
        imp = [[0] * 3 for i in range(m)]
        for i in range(m):
            t = map(int, raw_input().split())
            # 主件
            if t[2] == 0:
                main_components[i][0] = t[0]
                imp[i][0] = t[1]
            else:
                # 主件的第一个附件
                if main_components[t[2]-1][1] == 0:
                    main_components[t[2]-1][1] = t[0]
                    imp[t[2]-1][1] = t[1]
                # 主件的第二个附件
                else:
                    main_components[t[2]-1][2] = t[0]
                    imp[t[2]-1][2] = t[1]
        # 初始化处理结束后，main_components与imp中附件所在的位置其实是为空的，在后续遍历的时候相当于增加了若干个成本为0价值也为0的物品，对结果是无影响的

        # m:希望购买物品的数量
        # N:总钱数
        # 做动规时一般都声明size大一号的数组用以初始化
        profit=[[0]*(N+1) for i in range(m+1)]
        # 遍历m个物品
        for i in range(1,m+1):
            # 遍历1-N的能力
            for j in range(1,N+1):
                # 若能力能够买下第i个物品
                if j>=main_components[i-1][0]:
                    # 不买 VS 只买主件
                    profit[i][j]=max(profit[i-1][j],profit[i-1][j-main_components[i-1][0]]+main_components[i-1][0]*imp[i-1][0])
                    # VS 买主件+附件1
                    if main_components[i-1][1]!=0 and j>=main_components[i-1][0]+main_components[i-1][1]:
                        profit[i][j]=max(profit[i][j],profit[i-1][j-main_components[i-1][0]-main_components[i-1][1]]+main_components[i-1][0]*imp[i-1][0]+main_components[i-1][1]*imp[i-1][1])
                    # VS 买主件+附件2
                    if main_components[i-1][2]!=0 and j>=main_components[i-1][0]+main_components[i-1][2]:
                        profit[i][j]=max(profit[i][j],profit[i-1][j-main_components[i-1][0]-main_components[i-1][2]]+main_components[i-1][0]*imp[i-1][0]+main_components[i-1][2]*imp[i-1][2])
                    # VS 买主件+附件1+附件2
                    if main_components[i-1][1]!=0 and main_components[i-1][2]!=0 and j>=main_components[i-1][0]+main_components[i-1][1]+main_components[i-1][2]:
                        profit[i][j]=max(profit[i][j],profit[i-1][j-main_components[i-1][0]-main_components[i-1][1]-main_components[i-1][2]]+main_components[i-1][0]*imp[i-1][0]+main_components[i-1][1]*imp[i-1][1]+main_components[i-1][2]*imp[i-1][2])
                # 能力不够则不买
                else:
                    profit[i][j]=profit[i-1][j]
        print profit[m][N]
    except Exception,e:
        break
