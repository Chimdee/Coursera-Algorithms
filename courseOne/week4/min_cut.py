import random 

def min_cut(array, debug=False):

    while len(array) > 2:

        vertices = [u[0] for u in array]

        #pick random edge (u, v)
        u_idx = random.choice(list(range(len(vertices)))) #selecting vert1 [0:n-1]
        # u_idx =144
        u = vertices[u_idx] # [1:n]
        v = random.choice(array[u_idx][1:]) # [1:n]

        for n,j in enumerate(array):
            if v==j[0]:
                v_idx = n #[0,n-1]

        tmp_edges1 = array[u_idx]
        tmp_edges2 = array[v_idx]
        array = [i for i in array if i not in [array[u_idx], array[v_idx]] ]

        # print('\tafter removal:', len(array))

        vertices = [u[0] for u in array]
        if v in vertices:
            print(v, vertices)
            print(array[v_idx-1])
            raise ValueError

    
        #merge/contract (u,v) into sibgle vertex
        #new combined vertex
        array.append([u+"_"+v]) # appended as last item
        array[-1].extend(tmp_edges1[1:])
        array[-1].extend(tmp_edges2[1:])
        array[-1] = [i for i in array[-1] if i not in [u, v]] #removing self-loops

        # change edges to the new combined vertex
        for vert_ in array[:-1]: #for all old vertices
            if vert_[0] in array[-1][1:]: # a vertex in the edges of the new combined vertex
                for n,e in enumerate(vert_[1:]):
                    if e in [u,v]:
                        vert_[n+1] = u+'_'+v

    return len(array[0]) -1

mins= []
iter = 200
for i in range(iter):
    with open("kargerMinCut.txt", 'r') as file:
        list_ = [i.split('\t') for i in [f.rstrip() for f in file.readlines()]] 
    print(f'\r i ={i+1}/{iter}', end="")
    mins.append(min_cut(list_))
print(f'\nKarger mincut: {min(mins)}')