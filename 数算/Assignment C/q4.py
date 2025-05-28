v,a=map(int,input().split())
node=["v"+str(i) for i in range(v+1)]
dic1={i:0 for i in node}
dic2={i:[] for i in node}
for _ in range(a):
    f,t=map(int,input().split())
    dic1[node[t]]+=1
    dic2[node[f]].append(node[t])
vis=set()
cnt=0
ans=[]
while cnt<v:
    for i in range(1,v+1):
        if dic1[node[i]]==0 and node[i] not in vis:
            vis.add(node[i])
            ans.append(node[i])
            cnt+=1
            for nodes in dic2[node[i]]:
                dic1[nodes]-=1
            break
print(*ans)
