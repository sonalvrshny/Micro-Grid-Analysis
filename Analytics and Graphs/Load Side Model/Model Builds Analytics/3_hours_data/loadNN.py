import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import math
from keras.models import Sequential
from keras.layers import Dense, Activation

from datetime import datetime
from datetime import timedelta


def timeAssign(data):
    m = len(data)
    for i in range(m):
        dt = datetime.strptime(data.iloc[i],'%m/%d/%Y %H:%M')
        temp = dt.minute
        if(temp%15):
            k = math.floor(temp/15)
            mint = 15*(k+1)
            if(mint == 60):
                dt = dt.replace(minute=59) + timedelta(seconds = 60)
            else:
                dt = dt.replace(minute=mint)
            data.iloc[i] = dt.strftime('%m/%d/%Y %H:%M')
        else:
            data.iloc[i] = dt.strftime('%m/%d/%Y %H:%M')
    return data

def pfAssign(pfa,pfb,pfc,_id):
    # plz update for case when it starts with event id 5
    tmpa = -1
    tmpb = -1
    tmpc = -1
    pfa_5 = []
    pfb_5 = []
    pfc_5 = []
    for i in range(len(_id)):
        if(_id[i] == 3):
            tmpa = pfa[i]
            tmpb = pfb[i]
            tmpc = pfc[i]
        if(_id[i]== 5 and tmpa != -1):
            pfa_5.append(tmpa)
            pfb_5.append(tmpb)
            pfc_5.append(tmpc)
    pfa_5,pfb_5,pfc_5 = interpolate(pfa_5,pfb_5,pfc_5)
    return pfa_5,pfb_5,pfc_5

def interpolate(pfa,pfb,pfc):
    length = len(pfa)
    i = 0
    j = 0
    pfa_5 = []
    pfb_5 = []
    pfc_5 = []
    while(i<length):
        if(pfa[i]==0):
            count=0
            index=i
            while(pfa[index]==0):
                count=count+1
                index=index+1
            temp_a = pfa[i+count] - pfa[i-1]
            temp_b = pfb[i+count] - pfb[i-1]
            temp_c = pfc[i+count] - pfc[i-1]
            t = 0
            while(t<count):
                pfa_5.append((t*temp_a/(count+1)) + pfa[i-1])
                pfb_5.append((t*temp_b/(count+1)) + pfb[i-1])
                pfc_5.append((t*temp_c/(count+1)) + pfc[i-1])
                i=i+1
                j=j+1
                t=t+1
        else:
            pfa_5.append(pfa[i]) 
            pfb_5.append(pfb[i]) 
            pfc_5.append(pfc[i]) 
            i=i+1
            j=j+1
    return pfa_5,pfb_5,pfc_5

def calculate_power(va,vb,vc,ia,ib,ic,pfa,pfb,pfc):
    power = []
    for i in range(len(pfa)):
        # Power in kw
        power.append((va.iloc[i]*ia.iloc[i]*pfa[i]+vb.iloc[i]*ib.iloc[i]*pfb[i]+vc.iloc[i]*ic.iloc[i]*pfc[i])/1000)
    return power
# import data
df = pd.read_csv(r"BMSData_1.csv",header=0)

# segregate data
print(df)
df = df[['vltgA', 'vltgB', 'vltgC', 'vltgGN', 'currA', 'currB', 'currC', 'currN', 'PFA', 'PFB', 'PFC', 'eventId', 'eventTime']]
# df.to_csv(r'intermediate1.csv')

# Storing all data into individual vectors and scaling
va = df['vltgA'].apply(lambda x: x/10)
vb = df['vltgB'].apply(lambda x: x/10)
vc = df['vltgC'].apply(lambda x: x/10)
vgn = df['vltgGN'].apply(lambda x: x/10)
ia = df['currA'].apply(lambda x: x/10)
ib = df['currB'].apply(lambda x: x/10)
ic = df['currC'].apply(lambda x: x/10)
i_n = df['currN'].apply(lambda x: x/10)
pfa = df['PFA'].apply(lambda x: x/100)
pfb = df['PFB'].apply(lambda x: x/100)
pfc = df['PFC'].apply(lambda x: x/100)
_id = df['eventId']
tstmp = df['eventTime']

df_5 = df.loc[df['eventId'] == 5]
# df_5.to_csv(r'intermediate2.csv')

# Storing all values with event ID 5 into separate vectors
va5 = df_5['vltgA'].apply(lambda x: x/10)
vb5 = df_5['vltgB'].apply(lambda x: x/10)
vc5 = df_5['vltgC'].apply(lambda x: x/10)
vgn5 = df_5['vltgGN'].apply(lambda x: x/10)
ia5 = df_5['currA'].apply(lambda x: x/10)
ib5 = df_5['currB'].apply(lambda x: x/10)
ic5 = df_5['currC'].apply(lambda x: x/10)
in5 = df_5['currN'].apply(lambda x: x/10)
id5 = df_5['eventId']
tstmp5 = df_5['eventTime']

# update tstmp 5
tstmp5_updated = timeAssign(tstmp5)
tstmp5_updated = tstmp5_updated.reset_index(drop=True)
pfa_5,pfb_5,pfc_5 = pfAssign(pfa,pfb,pfc,_id)
power = calculate_power(va5,vb5,vc5,ia5,ib5,ic5,pfa_5,pfb_5,pfc_5)
power = pd.DataFrame({"Power (Kw)":power})
df = [tstmp5_updated, power]
output = pd.concat(df,axis=1)
output = output.rename(index=str, columns={"eventTime": "datetime"})
output.to_csv(r'BMS_Data[2].csv', index=False)
