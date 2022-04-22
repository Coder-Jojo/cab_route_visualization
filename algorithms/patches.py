from collections import deque as queue
pos_row = [-1,1,0,0]
pos_col = [0,0,1,-1]
def valid(vis,r,c,ar,row_size, col_size):
  if(r<0 or c<0 or r>=row_size or c>= col_size):
    return False
  if(ar[r][c] == 1):
    return False
  if(vis[r][c]):
    return False
  return True

def find_patch(ar,i,j,vis):
  patch_send = []
  q = queue()
  q.append((i,j))
  vis[i][j] = True
  while(len(q)>0):
    cell = q.popleft()
    patch_send.append((cell[0],cell[1]))

    for i in range(len(pos_row)):
      if valid(vis, cell[0]+pos_row[i], cell[1]+pos_col[i],ar, len(ar), len(ar[0])):
        q.append((cell[0]+pos_row[i], cell[1]+pos_col[i]))
        vis[cell[0]+pos_row[i]][cell[1]+pos_col[i]] = True
        patch_send.append((cell[0]+pos_row[i], cell[1]+pos_col[i],))

  #print(vis)
  patch_send = set(patch_send)
  return list(patch_send), vis

def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

def make_patch(ar):
    patches = []
    vis = []
    for i in range(len(ar)):
        temp = []
        for j in range(len(ar[0])):
            temp.append(False)
        vis.append(temp)
    
    for i in range(len(ar)):
        for j in range(len(ar[0])):
            if(vis[i][j] == False and ar[i][j]!= 1):
                z, vis_new = find_patch(ar,i,j,vis)
                patches.append(z)
                vis = vis_new

    return patches

