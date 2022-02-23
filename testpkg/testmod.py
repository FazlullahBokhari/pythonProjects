from Listpkg import listmod as ls
from dictpkg import dictmod as dt
from setpkg import setmod as s
from tuplepkg import tuplemod as tp


lst = [1,2,3,4,5,6,7,8,9]
ls.lspop(lst,5)

dct = {'name':'Faiz','email':'fazlullahb@gmail.com','mob':9873300865}
dt.dtget(dct,'name')


st = {1,2,3,4,5,7,8,9,10}
var = 15
s.stadd(s,var)

t = (1,2,3,4,5,6,3,3)

tp.tpcount(t,3)
