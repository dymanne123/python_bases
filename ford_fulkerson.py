def FordFulkerson(G,s,t):
    Gr=G
    f={}
    while True:
        aug_path=search_aug_path(Gr,s,t)
        if aug_path==None:
            break
        aug_flow=cf_path(Gr,aug_path)

        for k in range(len(aug_path)-1):
            u,v=aug_path[k],aug_path(k+1)
            if v in neighbours(u):
                f[u][v]+=aug_flow
                cf[u][v],cf[v][u]=c[u][v]-f[u][v],f[u][v]
            else:
                f[v][u]-=aug_flow
                cf[v][u],cf[u][v]=c[v][u]-f[v][u],f[v][u]

