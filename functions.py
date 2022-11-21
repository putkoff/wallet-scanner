import os
import os.path
import requests
import json
import time
import datetime
import math
import gc
import sys
def int_time_it(sec):
    hrs_1 = float(sec/float(3600))
    hrs = int(hrs_1)
    mins_1 = float(hrs_1-hrs)*float(60)
    mins = int(mins_1)
    secs = float(mins_1-mins)*(float(60))
    return hrs,mins,secs
def get_c(i):
    c = ','
    if i == 0:
        c = ''
    return c
def try_it_i(x,i):
    try:

        x = x[str(i)]
        return True
    except:
        return False
def json_it(x):
    x = json.loads(str(x).replace("'",'"'))
    return x
def up_low(txt):
    up = str(txt).upper()
    low = str(txt).lower()
    return up,low
def change_glob(x,v):
    globals()[x] = v
def prev_fold():
    x = os.path.abspath(__file__)
    x = str(x).replace(slash+str(x).split(slash)[-1],'')
    return x
def home_it():
    x = os.path.abspath(__file__)
   
    slash = '\\'
    if '/' in str(x):
        slash = '/'
    x = str(x).replace(slash+str(x).split(slash)[-1],'')
    change_glob('slash',slash)
    change_glob('home',x)
    return slash,x
def reques_timer():
    import datetime
    now = datetime.datetime.now().timestamp()
    i = (float(now) - float(reader('last.txt')))
    if float(i) < float(0.3):
        return (float(0.35) - float(i)), now
    return 0, now
def wall_call(add,B_L,B_G):
    link = wall_sup(add,B_L,B_G)
    JS = sites(link)
    js = JS["result"]
    return js
def first_last(js,X):
    Y = X
    try:
        W = js[0]
        F = W['timeStamp']
        B_L = W['blockNumber']
        W = js[-1]
        L = W['timeStamp']
        B_G = W['blockNumber']   
        Y = F,L,B_L,B_G
        if X !=0:
            if int(X[3]) == int(B_G) :
                return Y,1
            else:
                return Y,0
    except:
        return Y,-1
def reader_B(file):
    with open(file, 'r',encoding='UTF-8') as f:
        text = f.read()
        return text
def reader(file):
    with open(file, 'r') as f:
        text = f.read()
        return text
def pen_B(paper, place):
    
    with open(place, 'w',encoding='UTF-8') as f:
        f.write(str(paper))
        f.close()
        return
def pen(paper, place):
    with open(place, 'w') as f:
        f.write(str(paper))
        f.close()
        return
def sites(A):
    U = [A]
    for url in U:
        X = str(U[0])
        i,now = reques_timer()
        time.sleep(i)
        r = requests.get(X)
        pen(str(now),'last.txt')
        PS = r.text
        pen(str(PS),'recent.txt')
        JS = json.loads(PS)
    return JS
def keys():
    key = '4VK8PEWQN4TU4T5AV5ZRZGGPFD52N2HTM1'
    return key
def block(A):
    key = keys()
    U = 'https://api.'+str(scanners)+'/api?module=block&action=getblocknobytime&timestamp='+str(A)+'&closest=before&apikey='+str(key)    
    JS = sites(U)
    Bl = JS['result']
    return Bl
def exists_js(file):
    try:
        f = reader_B(file)
        if f !='':
            try:
                A = projs(f)
                
                return A
            except IOError:
                print('json not formed')
        else:
            f = '[]'
            return f
    except IOError:
        pen('[]',file)
        return json.loads('[]')
def exists(file):
    try:
        f = reader_B(file)
    except IOError:
        pen('',file)
        return ''
def countem(js,num_track,num_wall,add_js):
    js = json.loads(str(js).replace("'",'"'))
    #print(js)
    i = 2
    i_st = 0
    tot = 0
    count = 0
    tot_count = 0
    num = countit(js,',')
    add_new = ''
    while i_st != num:
        new = js[i_st]
        tot = int(tot) + int(new)
        i_st = i_st + 1
    print(tot,' total nodes')
    while int(i) < int(300):
        i_2 = int(0)
        while str(i) in js:
            new = js[i_2]
            if int(new) == int(i):
                if i_2 == 0:
                    bef_js = '['
                    bef_add_js = '['
                else:
                    bef_js = js[:int(int(i_2))]
                    bef_add_js = add_js[:int(int(i_2))]
                count = count + 1
                if count == int(0):
                    add_new = str(add_new) + '\n"' +str(add_js[i_2])+'"'
                else:
                    add_new = str(add_new) + '\n,"' +str(add_js[i_2])+'"'
                
                aft_js = js[int(int(i_2)+int(1)):]
                aft_add_js = add_js[int(int(i_2)+int(1)):]
                js = str(str(bef_js).replace(']',',') + str(aft_js).replace('[','')).replace(' ','').replace('[,','[').replace("'",'"').replace(',]',']')
                
                js = json_it(js)
                add_js = str(str(bef_add_js).replace(']',',') + str(aft_add_js).replace('[','')).replace(' ','').replace('[,','[').replace("'",'"')
                add_js = add_js.replace(',]',']')
                xx = str(add_js[:-1])
                pen(xx,'js.txt')
                add_js = json_it(xx+']')
                #print(js)
                i_guage = int(str(count).replace('0',''))
                if int(i) < int(20):
                    i_comp = int(int(count)/int(100))
                else:
                    i_comp = int(int(count)/int(10))
                    print(i, i_2)
                if i_guage == i_comp:
                    print(i,'addr',count)
                tot_count = tot_count + count
                
                if i_2 != int(0) and i_2 != tot:
                    i_2 = i_2 - 1
            else:
                i_2 = i_2 + 1
        if count > 0:
            #print(tot_count)
            num_track = str(num_track).replace('{,','{').replace('[,','[').replace('[\n,','[\n') + ',"'+str(i)+'":{"walls":"'+str(count)+'","perc":"'+str(round(float(int(count)/int(num_wall))*float(100),2))+'%","adds":['+add_new+'\n]}\n'
            pen(num_track,'num_track.txt')
            add_new = ''
            count = int(0)
            #print(num_track)
        i = i + 1
    count = countit(add_js,',')
    add_new = str(add_js).replace('[','\n').replace(']','').replace("'",'"').replace(' ','').replace(',','\n,')
    num_track = str(num_track)[1:]
    num_track = '{'+'"'+str('1')+'":{"walls":"'+str(count)+'","perc":"'+str(round(float(int(count)/int(num_wall))*float(100),2))+'%","adds":['+add_new+']}\n,'+str(num_track).replace('{,','{').replace('[\n,','[\n').replace('[,','[')+'\n}'
    pen(num_track,'num_track.txt')
    return js,num_track

def create_link(x,y):
    return str(x)+str(slash)+str(y)
def dirs_main():
    path = home
    # Check current working directory.
    retval = os.getcwd()
    print ("Current working directory %s" % retval)
    # Now change the directory
    os.chdir(path)
    # Check current working directory.
    retval = os.getcwd()
    print("Directory changed successfully %s" % retval)
    #print("Directory '% s' created" % directory)
    return
def dirs_A(fname):
    path = str(fname)
    print(path)
    # Check current working directory.
    retval = os.getcwd()
    print ("Current working directory %s" % retval)
    # Now change the directory
    os.chdir(path)
    # Check current working directory.
    retval = os.getcwd()
    print("Directory changed successfully %s" % retval)
    #print("Directory '% s' created" % directory)
    return 
def check_dirs(fname):
    path = str(fname)
    isFile = os.path.isdir(path)
    return isFile 
def change_dir(f):
    path = create_link(home,str(f))
    retval = os.getcwd()
    print ("Current working directory %s" % retval)
    os.chdir(path)
    retval = os.getcwd()
    print("Directory changed successfully %s" % retval)
    return path
def mkdirs(f):
    import os  
    directory = f
    parent_dir = home
    path = os.path.join(parent_dir, directory)  
    os.mkdir(path)  
    print("Directory '% s' created" % directory)
    return path
def dirs_B(U):   
    parent_dir = U
    path = os.chdir(parent_dir)
    os.chdir(str(path))
    print(path)
    return path
def get_ti():
    import datetime
    T_S = datetime.datetime.now().timestamp()
    pen(str(T_S),'last.txt')
    T_S_D = str(datetime.datetime.now())[0:10]
    day = int(int(T_S) - int(86400))
    B_L = block(day)
    B_G = block(int(T_S))
    
    TS = '{"TS":["'+str(T_S)+'","'+str(T_S_D)+'","'+str(B_L)+'","'+str(B_G)+'"]}'
    pen(TS, 'T_S_pow.py')
    return B_L,B_G,T_S,T_S_D,day
def tryit_js(js):
    try:
        js = projs(str(js))
        return js
    except:
        return 0
def tryit(A,N):
    try:
        tr = A[N]
        
        return 0, N
    except:
        N = N - 1
        return -1, N
def countit(array,delim):
    array_count = str(array)
    len_count_A = len(array_count)
    array_short = array_count.replace(delim,"")
    len_count_B = len(array_short)
    arr_num = len_count_A - len_count_B
    arr_num = arr_num
    return arr_num
def count_js(B):
    N = 0
    M = 0
    while M != -1:
        M,L_B = tryit(B,N)
        N = N + 1
    L_B = L_B - 1
    return L_B
def find_place(js,str_js):
    str_js = str(str_js).lower()
    found = int(0)
    i = int(0)
    js = projs_B(js)
    num = int(countit(js,','))+int(1)
    while i != int(num) and found != int(1):
        if str(str_js) == js[i]:
            found = int(1)
        else:
            i = int(i) + int(1)
    if found == int(0):
        return 'none'
    else:
        return i
#def sites(A):
#    U = [A]
#    for url in U:
#        X = str(U[0])
#        r = requests.get(X)
#        PS = r.text
#        JS = json.loads(PS)
#    return JS
def supply(add,Ad_pa):
    key = keys()
    CONT_SUP = 'http://api.'+scanners+'/api?module=account&action=tokenbalance&contractaddress='+str(add).lower()+'&address='+str(Ad_pa).lower()+'&tag=latest&apikey='+key
    return  CONT_SUP
def wall_sup(Ad_pa,B_L,B_G):
    key = keys()
    WALL_TR = 'http://api.'+scanners+'/api?module=account&action=tokentx&address='+str(Ad_pa)+'&startblock='+str(B_L)+'&endblock='+str(B_G)+'&sort=asc&apikey='+key
    return WALL_TR
def tok_sup(Ad_pa):
    key = keys()
    TOK_LP = 'https://api-cn.'+scanners+'/api?module=stats&action=tokensupply&contractaddress=' + str(Ad_pa).lower() + '&apikey='+key
    return TOK_LP
def meth_id(x):
    key = keys()
    meth_id = 'https://api.'+scanners+'/api?module=proxy&action=eth_getTransactionReceipt&txhash='+str(x)+'&apikey='+key
    return meth_id
def JS_prep(J):
    import gc
    gc.collect()
    J = str(J).replace(' ','').replace("'",'"').replace(']','').replace('[','').replace('}{','},{').replace('or"s','ors').replace('[,','[').replace('None','')
    if str(J) != ' ' and str(J) != '' and str(J) != '[]'and str(J) != '{}':
        J = str(J)
        L = int(len(J))
        i = int(-1)
        N,M = tryit(J,i)
        if int(N) == int(0):
            while (int(N) - int(L)) != int(0):
                if J[i] == '' or J[i] == ',' or J[i] == ']' or J[i] == ' ':
                    J = J[:-1]
                    #L = int(len(J))
                    
                    N = timer(N)
                else:
                    N = int(L)
        L = int(len(J))
        i = int(0)
        N,M = tryit(J,i)
        if int(N) == int(0):
            while (int(N) - int(L)) !=int(0):
                if J[i] == '' or J[i] == ',' or J[i] == ']' or J[i] == ' ':
                    J = J[1:]
                    #L = int(len(J))
                    N = timer(N)
                else:
                    N = int(L)
    return J
def JS_prep_B(A):
    A = str(A).replace(' ','').replace("'",'"').replace(',}','}').replace('{,','{').replace('}{','},{').replace('or"s','ors').replace('[,','[').replace('None','').replace('}','').replace('{','').replace(']','').replace('[','')
    return A
def projs(A):
    import gc
    J = JS_prep(A)
    if J == '' or J == ' ':
        return J
    J =  str(J).replace('"tokenName":"","','"tokenName":"0","').replace('"tokenSymbol":"","','"tokenSymbol":"0","').replace('"tokenDecimal":"","','"tokenDecimal":"0","')
    J =  str(J).replace('":"","','":"0","')
    J =  str(J).replace('""','"').replace(',,',',')
    gc.collect()
    J = str('[' +J+ ']').replace(' ','')
    J =  str(J).replace('[,','[').replace(',]',']').replace('":"s','*:*s').replace('","s','*,*s').replace('"s',"s")
    J = str(J).replace('*:*s','":"s').replace('*,*s','","s')
    
    pen_B(str(J),'recent.txt')
    return json.loads(J)
def projs_B(A):
    J = JS_prep_B(A)
    if J == '':
        return J
    while J[-1] == '' or J[-1] == ',' or J[-1] == ']' or J[-1] == ' ':
        J = J[:-1]
    while J[0] == '' or J[0] == ',' or J[0] == ']' or J[0] == ' ':
        J = J[1:]
    J = '[' + str(J) + ']'
    return json.loads(J)
def timer(N):
    N = N + 1
    return N
def timermin(N):
    N = N - 1
    return N
def find_point(B,D,X):
    N = 0
    done = 1
    L = count_js(B)
    while done != 0:
        C = B[N]
        if C[D] == str(X):
            done = 0
        if int(N) == int(L):
            return ''
        print(N,L)
        N = timer(N)
    N = int(N)
    B = B[N:]
    return B
def check_comp(J):
    J = projs(J)
    tr,N = tryit(J,0)
    if tr != -1:
        B = J[0]
        E = B['blockNumber']
        F = B['timeStamp']        
        D = J[-1]
        G = D['blockNumber']
        H = D['timeStamp']
        
        if int(F) > int(H):
            J = reverse(J)
    return projs(J)
def JS_rev(js):
    pen_B(js,'other1.txt')
    js = projs(js)
    L = count_js(js)
    js = js[L:]
    pen_B(js,'other.txt')
    return js
def check_blk(f,bl,ts):
    print('checking blk')
    J = exists_js(f)
    tr,N = tryit(J,0)
    print(tr,N)
    if int(tr) == int(0):
        J = check_comp(J)
        B = J[0]
        E = B['blockNumber']
        F = B['timeStamp']        
        D = J[-1]
        G = D['blockNumber']
        H = D['timeStamp']
        #if int(F) < int(day):
            #J = find_point(J,'timeStamp',int(day))
        return J,G,H
    return J,bl,ts

def wall(add,B_L,B_G,day,file):
    print(add)
    import time
    js_new = ''
    L = day,0,B_L,B_G
    first = 0
    #J,B_L,T_S = check_blk(file,B_L,day)
    done = 0
    #print(add,B_L,B_G,T_S)
    J = ''
    while int(done) == int(0):
        link = wall_sup(add,B_L,B_G)
        print(link)
        JS = sites(link)
        js = JS["result"]
        
        while str(js) == 'Max rate limit reached':
            time.sleep(5)
            print('sleeping... wallets')
            js = wall_call(add,B_L,B_G)
        L,done = first_last(js,L)
        print(L,done)
        try:
            A = js[0]
            B = js[-1]
        except:
            A = ''
            B = ''
        #if int(A['timeStamp']) > int(B['timeStamp']):
            #js = reverse(js)
        if str(js) != '[]':
            print(add)
            #js,T_S = hashit(js,day,L[0],L[2],add,file,node_num,node_str)
        try:
            js = JS_prep(js)
        except:
            js = ''
        J =  str(J)+','+str(js)
        pen(J,file)
        B_L = L[3] 
    return J
def hashit(js,day,T_S,bl,add,fname,node_num,node_str):
    Ts = T_S
    dec_str = float(10)**(float(-1)*float(18))
    
    print('hashing it')
    js = projs(js)
    tr = 0
    L_B = count_js(js) - int(1)
    H_js = exists_js('hashs.txt')
    B = exists_js('new.txt')
    B = reader('new.txt')
    H = reader('hashs.txt')
    L_N = 0
    if fname == 'new.txt':
        arr = ''
        #L = count_js(pairs)
        L = int(1)
        N = 0
        #while int(N) != int(L):
            #P = pairs[N]
            #arrs = array[P]
            #arr = arr + ',"'+arrs['pair']+'"\n'
            #arr = str(arr).lower()
            #N = N + 1
        arr = '["'+str(add)+'"]'
        #arr = str(arr).replace('[,','[')
        arr = json.loads(arr)
        print(L_N,L_B)
        while int(L_N) != int(L_B) and tr != -1:
            tr,L_N = tryit(js,L_N)
            line = js[L_N]
            Ts = line["timeStamp"]
            cont = line['contractAddress']
            B_L = line['blockNumber']
            value = line['value']
            value_dec = float(value)*float(dec_str)
            if float(value_dec) == float(str(node_num)) and line['to'].lower() == add.lower():
                if line['hash'].lower() not in H_js:
                    B = str(B).replace('[]','[')+'\n'+str(line)+','
                    H =H.lower()+ ',"'+str(line['hash']).lower()+'"\n'
                    H_js = str(H).replace('[]','[')+']'
                    H_js = str(H_js).replace('[,','[')
                    H_js = json.loads(H_js)
                #print(L_N,L_B)
            L_N = timer(L_N)
    else:
        while int(L_N) != int(L_B) and tr != -1:
            tr,L_N = tryit(js,L_N)
            line = js[L_N]
            Ts = line["timeStamp"]
            cont = line['contractAddress']
            B_L = line['blockNumber']
            if line['hash'].lower() not in H_js and int(Ts) >= int(T_S) and int(B_L) > int(bl):
                if line['to'].lower() == nodestr.lower() or line['from'].lower() == node_str.lower():
                    B = str(B)+str(line)+',\n'
            L_N = timer(L_N)
            #print(L_N,L_B,fname,Ts,T_S)
    pen(H,'hashs.txt')
    tr,i = tryit(B,0)
    if int(tr) != int(-1):
        if B[0] == ',':
            B = B[1:]
    pen_B(str(B),'new.txt')
    return B,Ts

def findit(js,X):
    L_eth = count_js(js)
    N = 0
    while js[N] != str(X):
        N = timer(N)
    return N
def organ(js):
    js
    return js
def add_brac(S):
    return str('{'+str(S)+'}')
def rem_comm(S):
    S = str(S)
    if str(S[0]) == ',':
        S = str(S)[1:]
    if str(S[-1]) == ',':
        S = str(S)[:-1]
    return S
def ch_quote(S):
    return str(str(S).replace("'",'"'))
def foldersave():
    B_L,B_G,Ts,date,day = get_ti()
    foldate = 'fri','sat','sun','mon','tues','wed','thur',
    sec = float(1)
    mi = float(60)
    hour = float(60*mi)
    day = float(24*hour)
    week = float(7*day)
    fri = 1609510651.1613681
    print('fri',fri)
    since = (float(Ts)-(float(fri)))
    D = mi,hour,day,week
    D_2 = 'sec,hour,day,week'
    D_3 = D_2.split(',')
    N = 0
    jas = ''
    while N <= int(3):
        i = float(since)/float(D[N])
        jas = jas+',"'+str(D_3[N])+'":"'+str(float(i))+'"'
        N = timer(N)
        TSH = str(ch_quote(add_brac(rem_comm(jas))))
        print(i,TSH,N)
        timesheet = json.loads(TSH)
    days = int(float(timesheet['day']))
    date = str(date).replace('-','_')
    print(date,days,foldate)
    fold_name = str(date)
    path_price = str(fold_name)+'/'+'price'
    path_bal = str(fold_name)+'/'+'bal'
    path_workbook = str(fold_name)+'/'+'workbook'
    X = fold_name, path_price,path_bal,path_workbook
    X_name = 'fold_name','path_price','path_bal','path_workbook'
    i = 0
    while i != 4:
        A= check_dirs(X[i])
        print(A)
        if A == True:
            i = timer(i)
        elif A == False:
            print('we change it')
            mkdirs(X[i])
            i = timer(i)
    return fold_name,home+path_price,home+path_bal,home+path_workbook
def make_js(js,str_js,delim,case):
    up_str_js,low_str_js = up_low(str_js)
    if case == '[' or case == ']':
        end = ']'
    elif case == '{' or case == '}':
        end == '}'
    js_whole = str(js)+str(end)
    js_whole = JS_prep_B(js_whole)
    num = countit(js_whole,'"')
    if num != 0 and str(str_js) != '':
        num = int(num)/int(2)
        js = str(js)+',\n"'+ str(low_str_js)+'"'
    elif num == 0 and str_js != '':
        js = str(js)+'\n"'+str(low_str_js)+'"'
    js_whole = str(js) + str(end)
    if js_whole != '[]' and js_whole != '{}':
        js_whole = JS_prep_B(js_whole)  
    return js,js_whole
def up_low(txt):
    up = str(txt).upper()
    low = str(txt).lower()
    return up,low
def get_txns(add,B_L,B_G):
    link = wall_sup(add,B_L,B_G)
    print(add)
    #print(link)
    JS = sites(link)
    #print(JS)
    js = JS["result"]
    return js
def fold_check(x):
    try:
        mkdirs(x)
        return
    except:
        return
def home_glob(x):
    global home
    home = x
def scan_glob(x):
    global scanners
    scanners = x
