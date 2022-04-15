import random
import time


def create_road(grid, cr_3, cr_4):
    matrix = grid.matrix
    n = grid.rows
    m = grid.cols
    cross_3_prob = cr_3 / (n * m)
    cross_4_prob = cr_4 / (n * m)
    for i in range(n):
        for j in range(m):

            if i == 0 or j == 0 or i == n - 1 or j == m - 1 or matrix[i][j] != 0:
                continue

            if random.random() <= cross_3_prob:
                matrix[i][j] = 3
                matrix[i - 1][j] = 1
                matrix[i][j - 1] = 2
                matrix[i + 1][j] = 1
                matrix[i][j + 1] = 2

                erase = int(random.random() * 100)
                if erase < 25:
                    matrix[i + 1][j] = 0
                elif erase < 50:
                    matrix[i - 1][j] = 0
                elif erase < 75:
                    matrix[i][j - 1] = 0
                else:
                    matrix[i][j + 1] = 0

            if random.random() <= cross_4_prob:
                matrix[i][j] = 4
                matrix[i - 1][j] = 1
                matrix[i][j - 1] = 2
                matrix[i + 1][j] = 1
                matrix[i][j + 1] = 2

    queue = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                queue.append((i - 1, j, 1, -1, random.randint(3, 10)))
                queue.append((i + 1, j, 1, 1, random.randint(3, 10)))
            if matrix[i][j] == 2:
                queue.append((i, j - 1, 2, -1, random.randint(3, 10)))
                queue.append((i, j + 1, 2, 1, random.randint(3, 10)))

    while len(queue):
        x, y, z, k, cnt = queue[0]
        queue.pop(0)
        cnt -= 1

        if x < 0 or y < 0 or x > n - 1 or y > m - 1:
            continue

        if matrix[x][y] == 0:
            matrix[x][y] = z
            if cnt == 0:
                if z == 1:
                    z = 2
                else:
                    z = 1
                if random.randint(0, 2) == 0:
                    k = -1
                else:
                    k = 1
                cnt = random.randint(3, 10)

            if z == 1:
                x += k
            else:
                y += k
            queue.append((x, y, z, k, cnt))
            
    for i in range(n-1):
       for j in range(m-1):
          cnt=0
          a=i
          b=j
          while(a < n and b < m and matrix[a][b]>0 and matrix[a+1][b]>0):
             cnt+=1
             b+=1
          
          if(cnt>2):
             a=i
             b=j
             k=0
             flag=random.randint(0,2)
             while(k<cnt-2):
                if(flag==0):
                   matrix[a][b+1]=0
                   # print(a, b+1)
                else:
                   matrix[a+1][b+1]=0
                   # print(a+1, b+1)
                b+=1
                k+=1
                
          elif(cnt==2):
             cntv=0
             a=i
             b=j
             while(a < n and b < m and matrix[a][b]>0 and matrix[a][b+1]>0):
                cntv+=1
                a+=1
             
             if(cntv>2):
                a=i
                b=j
                k=0
                flag=random.randint(0,2)
                while(k<cntv-2):
                   if flag==0:
                      matrix[a+1][b]=0
                   else:
                      matrix[a+1][b+1]=0
                   a+=1
                   k+=1
             elif(cntv==2):
                if random.randint(0,4)==0:
                   matrix[i][j]=0
                elif random.randint(0,4)==1:
                   matrix[i][j+1]=0
                elif random.randint(0,4)==2:
                   matrix[i+1][j]=0
                else:
                   matrix[i+1][j+1]=0
             
             else:
                continue
          else:
             continue

    road = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                road.append((j, i, matrix[i][j]))

    for x, y, z in road:
        if z == 1:
            grid.put_vertical_road(x, y)
        elif z == 2:
            grid.put_horizontal_road(x, y)
        elif z == 3 or z == 4:
            grid.put_intersection(x, y)
        time.sleep(.01)

    grid.matrix = matrix
