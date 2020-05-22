sx,sy,tx,ty=map(int,input().split())

ans=[]

#sの上->tの左 ↑→
sx1=sx
sy1=sy+1
tx1=tx-1
ty1=ty
ans.append('U')
ans.extend(['U']*(ty1-sy1))
ans.extend(['R']*(tx1-sx1))
ans.append('R')

#tの下->sの右  ↓←
sx2=sx+1
sy2=sy
tx2=tx
ty2=ty-1
ans.append('D')
ans.extend(['D']*(ty2-sy2))
ans.extend(['L']*(tx2-sx2))
ans.append('L')

#sの下->tの右 ↓→↑←
sx3=sx
sy3=sy-1
tx3=tx+1
ty3=ty
ans.append('D')
ans.extend(['R']*(tx3-sx3))
ans.extend(['U']*(ty3-sy3))
ans.append('L')

#tの上->sの左 ↑←↓→
sx4=sx-1
sy4=sy
tx4=tx
ty4=ty+1
ans.append('U')
ans.extend(['L']*(tx4-sx4))
ans.extend(['D']*(ty4-sy4))
ans.append('R')

print(''.join(ans))
