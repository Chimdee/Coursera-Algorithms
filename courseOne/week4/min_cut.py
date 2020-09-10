import random 

with open("kargerMinCut.txt", 'r') as file:
    list_ = [i.split('\t') for i in [f.rstrip() for f in file.readlines()]]

def min_cut(array, debug=False):

    while len(array) > 2:

        vertices = [u[0] for u in array]

        #pick random edge (u, v)
        u_idx = random.choice(list(range(len(vertices)))) #selecting vert1 [0:n-1]
        # u_idx =144
        u = vertices[u_idx] # [1:n]
        v = random.choice(array[u_idx][1:]) # [1:n]
        # v = '118'
        # print('v:', v, f'is in vertices: {v in vertices}')
        # if not v in vertices:
        #     print(array[u_idx])
        #     print(vertices)

        Flag="Error"
        for n,j in enumerate(array):
            # print(j[0])
            if v==j[0]:
                # print('vv:', j[0], n)
                v_idx = n #[0,n-1]
                Flag ='OK'

        if Flag=='Error':
            raise ValueError

        # print("vertices chosen:")
        # print(u, array[u_idx])
        # print(f'{v} is in removed: {v in removed}, is in vertices: {v in vertices}')
        # print(f'vertices v,v_idx: {v}, {v_idx}, {vertices}')
        # print(v, v_idx, array[v_idx])
        tmp_edges1 = array[u_idx]
        tmp_edges2 = array[v_idx]
        # print('\tbefore removal:', len(array))
        # print("array to be removed:")
        # print(array[u_idx])
        # print(array[v_idx])
        # array.remove(array[v_idx]) 
        # array.remove(array[u_idx])
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

        # print("combined vertex:", array[-1])
        # print("#"*100)
        # change edges to the new combined vertex
        #idx
        for vert_ in array[:-1]: #for all old vertices
            if vert_[0] in array[-1][1:]: # a vertex in the edges of the new combined vertex
                for n,e in enumerate(vert_[1:]):
                    if e in [u,v]:
                        # print("True:", e,n, vert_[1:][n], u+'_'+v)
                        vert_[n+1] = u+'_'+v
                        # print("True:", e,n, vert_[1:][n], u+'_'+v)

        
        # print("edges edited:", array[:4])
        # print("#"*100)
        # remove old vertices
        # print('\tbefore removal:', len(array))
        # print("array to be removed:")
        # print(array[u_idx])
        # print(array[v_idx])
        # array.remove(array[u_idx])
        # array.remove(array[v_idx]) 
        # print('\tafter removal:', len(array))
        # print("old removed:", array[:4])
        # print("#"*100) 
        
        if debug:
            # print(vertices[idx[0]], u_list)
            # print(vertices[idx[1]], v_list)
            # print(vertices[idx[0]], vertices[idx[1]], len(vertices), vertices)
            # print(array[idx[0]], array[idx[1]])
            print()

            # if len(array) < 198:
            break
        else:
            # print(len(array), len(array[0]), len(array[1]))
            pass
            # print("#"*100)

    return len(array[0])

mins= []
for i in range(500):
    with open("kargerMinCut.txt", 'r') as file:
        list_ = [i.split('\t') for i in [f.rstrip() for f in file.readlines()]] 
    print(f'\r i ={i+1}/200', end="")
    mins.append(min_cut(list_))
print()
print(min(mins))