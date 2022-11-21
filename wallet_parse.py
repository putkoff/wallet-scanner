#!/opt/rh/rh-python35/root/usr/python
import os
import os.path
import requests
import json
import time
import datetime
import math
import gc
import sys
import functions as f
from eth_log.models.contract import Contract
from web3 import Web3
from web3.auto import w3
import eth_event
import json
from hexbytes import HexBytes
from ast import literal_eval
from attributedict.collections import AttributeDict
def exists_js(file,x):
    try:
        h = f.reader_B(file)
        return f.json_it(h)
    except:
        f.pen(x,file)
        return f.json_it(x)
def mains(x):
    from web3 import Web3
    global net,ch_id,main,file,w3,last_api,c_k,hashs_js,expo,dec
    hashs_js = ''
    last_api = [0,0]
    scan = ['avax','polygon','ethereum','cronos_test','optimism','binance']
    main = {
        'avax':{'net':'https://api.avax.network/ext/bc/C/rpc','chain':'43114','main':'AVAX'},
            'polygon':{'net':'https://polygon-rpc.com/','chain':'137','main':'MATIC'},
            'ethereum':{'net':'https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161','chain':'1','main':'ETH'},
            'cronos_test':{'net':'https://cronos-testnet-3.crypto.org:8545/','chain':'338','main':'TCRO'},
            'optimism':{'net':'https://kovan.optimism.io','chain':'69','main':'OPT'},
            'binance':{'net':'https://bsc-dataseed.binance.org/','chain':'56','main':'bsc'}
            }
    expo = ''
    dec = ''
    main = main[x]
    net,ch_id,main,file,w3 = main['net'],main['chain'],main['main'],str(x)+'.txt',Web3(Web3.HTTPProvider(main['net']))
    c_k = 0
    return net,ch_id,main,file,w3
def change_glob(x,v):
    globals()[x] = v
def check_sum(x):
    return Web3.toChecksumAddress(str(x))
def get_c(i):
    c = ',\n'
    if i == 0:
        c = ''
    return c
def get_hashs_1(add,r):
    r=['new0.txt','new.txt']
    for k in range(0,len(add)):
        wall = json.loads('['+f.reader(r[k]).replace("'",'"')+']')
        if wall[0] == []:
            wall = wall[1:]
        get_hashs(wall,k,add)
        f.pen(ha_all,'all_hash.txt')
def get_hashs(n,k,add):
    global ha_all
    for i in range(1,len(n)):
        ha = n[i]["hash"]
        if str(ha) not in ha_all["hashs"][k]:
            ha_all["hashs"][k].append(str(ha))
        if str(ha) not in ha_all["hash_values"]:   
            ha_all["hash_values"] = json.loads(str(str(ha_all["hash_values"])[:-1]+get_c(len(ha_all["hash_values"]))+'"'+str(ha)+'":[0]}').replace("'",'"'))
        if str(n[i]["contractAddress"]).lower() == str(add).lower():
            ha_all["hash_values"][str(ha)][0] = float(ha_all["hash_values"][str(ha)][0]) + float(float(str('1e-18'))*float(n[i]["value"]))
        change_glob('ha_all',ha_all)
        if i%10000 == float(0):
            print(len(ha_all["hashs"][k]))
def expo_it(x):
    return float(float(str('1e-18'))*float(x))
def div_ten(x):
    return float(float(x)/float(10))
def add_one(x):
    return float(float(x)+ float(1))
def float_it(x,y):
    return float(float(x)+float(y))
def create_new(x,y,z):

    return js_it(str(x)[:-1]+get_c(y)+'"'+str(z)+'":[0]}')
def js_it(x):
    return json.loads(str(x).replace("'",'"'))
def evs(x):
    ev = ["0x120ccbf9", "0xa74b343c", "0xbbc67998"]#kek('compoundAllNodes(uint256)'),kek('createNodeWithTokens(string,uint256)')]
    sel = {'0x120ccbf9':'compoundAllNodes','0xbbc67998':'createNodeWithTokens','0xa74b343c':'migrateOldNode'}
    if x in ev:
        for ii in range(0,len(ev)):
            if x == ev[ii]:
                fun = ev[ii]
        return sel[fun]
    else:
        return False
def det_val(val,inn,fr,to,add):
    if inn == '0xbbc67998' or inn == '0xa74b343c':
        if str(val) == "10000000000000000000" or str(val) == "10100000000000000000":
            return val
        return False
    elif inn == '0x120ccbf9':
        if str(fr).lower() == str("0x0000000000000000000000000000000000000000").lower() and str(to).lower() in add:
            return val
        return False
    else:
        return False
def fun_it(ha,ad):
    n = w3.eth.get_transaction(HexBytes(ha))
    fr = n['from']
    fun = False
    inn = ''
    to = n.to
    if str(to).lower() in ad:
        inn = str(n.input)[:10]
        fun = evs(inn)
    return fr,fun,inn,to
def kek(x):
    st = '"'+str(x)+'"'
    return w3.keccak(text=str(x)).hex()
def div_it():
    global add_tots,fr_it
    add_tots[fr]["total"][1] = div_ten(add_tots[fr]["total"][0])
    add_tots[fr][fun][1] = div_ten(add_tots[fr][fun][0])
    fr_it[fun][1] = div_ten(fr_it[fun][0])
    change_glob('fr_it',fr_it)
    change_glob('add_tots',add_tots)
def add_up(x):
    global add_tots,fr_it
    add_tots[fr]["total"][0] = float_it(add_tots[fr]["total"][0],x)
    add_tots[fr][fun][0] = float_it(add_tots[fr][fun][0],x)
    fr_it['tot_val'][0] = float_it(fr_it['tot_val'][0],x)
    fr_it[fun][0] = float_it(fr_it[fun][0],val_expo)
    change_glob('fr_it',fr_it)
    change_glob('add_tots',add_tots)
def add_all():
    add_tots[fr][fun][2] = add_one(add_tots[fr][fun][2])
    fr_it['tot_val'][1] = add_one(fr_it['tot_val'][1])
    fr_it[fun][2] = add_one(fr_it[fun][2])
def create_new(x,y,z,zz):
    return js_it(str(x)[:-1]+get_c(y)+'"'+str(z)+'":'+zz+'}')
def int_time_it(sec):
    hrs_1 = float(sec/float(3600))
    hrs = int(hrs_1)
    mins_1 = float(hrs_1-hrs)*float(60)
    mins = int(mins_1)
    secs = float(mins_1-mins)*(float(60))
    return hrs,mins,secs
def diff_it(t1,t2):
    return float(float(t2) - float(t1))
def time_it(t1,t2):
    diff = diff_it(t1,t2)
    hrs,mins,secs = int_time_it(diff)
    return diff,hrs,mins,secs
def txn_get(x,y):
    txn_data = json.loads('{"hashs":[],"ts":[],"id":[],"val":[],"fro":[],"to":[]}')
    varis = ["hashs","ts","id","val","fro","to"]
    for i in range(0,len(varis)):
        txn_data[varis[i]].append(y[i])
        if txn_data[varis[i]][0] == '':
            print(y)
            exit()
    return txn_data
        
     
ev = ["0x120ccbf9", "0xa74b343c", "0xbbc67998"]#kek('compoundAllNodes(uint256)'),kek('createNodeWithTokens(string,uint256)')]
sel = {'0x120ccbf9':'compoundAllNodes','0xbbc67998':'createNodeWithTokens','0xa74b343c':'migrateOldNode'}
cont = [str('0x1aea17a08ede10d158baac969f809e6747cb2b22').lower(),str('0x5aa2ff4ab706307d8b3d90a462c1ddc055655734').lower()]
net,ch_id,main,file,w3=mains('avax')
f.change_glob('scanners','snowtrace.io')
B_L = '0000000000'
B_G = '9999999999'
day = 60*60*24
for k in range(0,1):
    file = 'txns_'+cont[k]+'_.txt'
    f.pen('',file)
    B_L = '0000000000'
    B_G = '9999999999'
    add_ls = []
    total_txns = json.loads('{}')
    f.pen(0,'last.txt')
    f.pen([],'recent.txt')

    f.wall(cont[k],B_L,B_G,day,file)
    x = f.reader(file).replace('}],{','},{')
    if str(x)[-1] != ']':
        x = x+']'
    if x[0] == ',' or x[0] == ' ':
        x = x[1:]
    if x[0] != '[':
        x = '['+x
    txns = js_it(x)
    
    for i in range(0,len(txns)):
        n = txns[i]
        if str(n["contractAddress"]).lower() in cont:
            fro = str(n["from"]).lower() 
            to = str(n["to"]).lower()
            tx_adds = [to,fro]
            txn_ind = str(n["transactionIndex"]).lower() 
            hashs = str(n["hash"]).lower() 
            ts  = str(n["timeStamp"]).lower()
            val = float(str(n["value"]).lower())*float(str('1e-18'))
            c_add = str(n["contractAddress"]).lower()
            di = 'N'
            if fro != str(n).lower():
                di_fro = fro
            else:
                di_fro = 'Y'
            if to != str(n).lower():
                di_to = to
            else:
                di_to = 'Y'
            for ii in range(0,len(tx_adds)):
                add = tx_adds[ii]
                if c_add in cont:
                    if add not in add_ls:
                        new = '"'+str(add).lower()+'":[]'
                        total_txns = f.json_it(str(str(total_txns)[:-1] + f.get_c(len(add_ls))+new+'}'))
                        add_ls.append(add)
                    varss = [hashs,txn_ind,ts,val,di_fro,di_to]
                    total_txns[add].append(txn_get(add,varss))
        if i%10000== float(0):
            l = len(txns)
            l_i = l - i
            print(i,' txns scanned out of ',l,' with ',l_i,' more to go')
    f.pen(total_txns,'total_txns_'+str(k)+'.txt')
    f.pen(add_ls,'total_adds_'+str(k)+'.txt')
