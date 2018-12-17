def pu(m,n,a,b,c,oa,ans):
    """主体铺砖函数
    其中m、n、a、b为墙和砖的尺寸；
    c为墙体铺砖情况的记录
    oa为其中一个答案（one answer）
    ans为最终答案"""
    if (m*n)%(a*b)!=0:
        return ans
    else:
        if a==b:
            """单独判断正方形砖块"""
            if m%a==0 and n%a==0:
                """判断墙的长和宽能否整除砖的边长"""
                for i in range(m*n):
                    if c[i]==0:
                        e=[]
                        """每个e都是一块砖"""
                        if i+(b-1)*m+a-1<=m*n-1 and m-i%m>=a:
                            """判断这块砖会不会在下侧及右侧超出墙面"""
                            for k in range(b):
                                for j in range(i+k*m,i+k*m+a):
                                    c[j]=1
                                    e.append(j)
                                    """铺砖"""
                            oa.append(e)
                        if len(ans)==0:
                            ans.append(oa)
            else:
                return ans
        else:
            h=0
            """这是个布尔值"""
            for i in range(m*n):
                if c[i]==0 and h==0:
                    h=1
                    """改变布尔值，使得只对第一块找到的没铺上的砖进行操作"""
                    x=0
                    """这是个计数器"""
                    for w in range(b):
                        for q in range(i+w*m,i+w*m+a):
                            if q<m*n:
                                if c[q]==0:
                                    x+=1
                                    """横着铺，判断是不是一块砖所覆盖的区域都还没被铺上"""
                    e=[]
                    """每个e都是一块砖"""
                    if i+(b-1)*m+a-1<=m*n-1 and m-i%m>=a and x==a*b:
                        """判断这块砖会不会在下侧及右侧超出墙面，以及是不是满足上面的判断"""
                        for k in range(b):
                            for j in range(i+k*m,i+k*m+a):
                                c[j]=1
                                e.append(j)
                                """铺砖"""
                        oa.append(e)
                        """记录下每块砖"""
                        if 0 not in c:                      
                            ans.append(oa.copy())
                        else:
                            pu(m,n,a,b,c,oa,ans)
                        for k in range(b):
                            for j in range(i+k*m,i+k*m+a):
                                c[j]=0
                        del oa[-1]
                        """拆砖"""
                    y=0
                    """开始考虑竖着铺，一切同上"""
                    for w in range(a): 
                        for q in range(i+w*m,i+w*m+b):
                            if q<m*n:
                                if c[q]==0:
                                    y+=1
                    e=[]
                    if i+(a-1)*m+b-1<=m*n-1 and m-i%m>=b and y==a*b:
                        for k in range(a): 
                            for j in range(i+k*m,i+k*m+b):
                                c[j]=1
                                e.append(j)
                        oa.append(e)
                        if 0 not in c:
                            ans.append(oa.copy())
                        else:
                            pu(m,n,a,b,c,oa,ans)
                        for k in range(a):
                            for j in range(i+k*m,i+k*m+b):
                                c[j]=0
                        del oa[-1]
            return ans
def hua(m,n,a,b,ans):
    import turtle
    """开始生成墙面"""
    p=turtle.Pen()
    p.color("blue")
    turtle.hideturtle()
    p.penup()
    p.goto(-50,50)
    p.pendown()
    p.forward(m*30)
    p.penup()
    p.goto(-50,20)
    p.pendown()
    """画第一条横线"""
    for i in range(m*n):
        p.forward(5)
        p.write(i)
        p.forward(25)
        """给墙标号，画横线"""
        if (i+1)%m==0:
            """判断画完了一行，转去下一行"""
            p.penup()
            p.goto(-50,-30*(((i+1)//m)+1)+50)
            p.pendown()
    p.penup()
    p.goto(-50,50)
    p.pendown()
    p.right(90)
    """开始画竖线"""
    for i in range(m+1):
        p.forward(30*n)
        p.penup()
        p.goto(30*(i+1)-50,50)
        p.pendown()
    """开始画方案"""
    p.color("black")
    p.pensize(3)
    p.left(90)
    for i in ans:
        if (i[-1]-i[0])==(m*(b-1)+(a-1)):
            """判断这块砖是横着铺的"""
            p.penup()
            p.goto((i[0]%m)*30-50,-(i[0]//m*30)+50)
            p.pendown()
            p.forward(30*a)
            p.right(90)
            p.forward(30*b)
            p.right(90)
            p.forward(30*a)
            p.right(90)
            p.forward(30*b)
            p.right(90)
        else:
            """竖着的砖"""
            p.penup()
            p.goto((i[0]%m)*30-50,-(i[0]//m*30)+50)
            p.pendown()
            p.forward(30*b)
            p.right(90)
            p.forward(30*a)
            p.right(90)
            p.forward(30*b)
            p.right(90)
            p.forward(30*a)
            p.right(90)
    turtle.done()
def main():
    m=int(input("请输入墙的长度："))
    n=int(input("请输入墙的宽度："))
    a=int(input("请输入砖的长度："))
    b=int(input("请输入砖的宽度："))
    print("\n")
    c=[0]*m*n
    ans=[]
    
    pu(m,n,a,b,c,[],ans)
    print("一共有%d种方案"%(len(ans)))
    print("\n")
    for i in range(len(ans)):
        print("方案%d："%(i+1),ans[i])
        print('\n')
    if len(ans)!=0:
        s=int(input("请输入您选择的方案序号："))-1
        hua(m,n,a,b,ans[s])
    else:
        print("抱歉，该尺寸砖块无法铺满此墙壁")
if __name__=="__main__":
    main()
