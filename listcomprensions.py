if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    output=[]
    abc=[]
    for i in range(x+1):
        for j in range(y+1):
            for m in range(z+1):
                if(i+j+m)!=n:
                    abc=[i,j,m]
                    output.append(abc)
print(output)
