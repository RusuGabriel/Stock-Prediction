import datetime as dt
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime(2019,8,18)
end = dt.datetime(2019,11,2)

df_CCHL = web.DataReader('CCH.L','yahoo',start,end)

df_CPGL = web.DataReader('CPG.L','yahoo',start,end)

df_BCS = web.DataReader('BCS','yahoo',start,end)

df_BLNDL = web.DataReader('BLND.L','yahoo',start,end)

df_AV = web.DataReader('AV.L','yahoo',start,end)

df_HLMAL = web.DataReader('HLMA.L','yahoo',start,end)

df_NGL = web.DataReader('NG.L','yahoo',start,end)

df_RRL = web.DataReader('RR.L','yahoo',start,end)

df_VOD = web.DataReader('VOD','yahoo',start,end)

df_UN = web.DataReader('UN','yahoo',start,end)

df2 = web.DataReader('AVVIY','yahoo',start,end)


df_CCHL.to_csv('Coca-Cola HBC.csv')

df_CPGL.to_csv('Compass Group.csv')

df_BCS.to_csv('Barclays.csv')

df_BLNDL.to_csv('British Land Company.csv')

df_AV.to_csv('Aviva.csv')

df_HLMAL.to_csv('Halma.csv')

df_NGL.to_csv('National Grid.csv')

df_RRL.to_csv('Rolls-Royce.csv')

df_VOD.to_csv('Vodafone Group.csv')

df_UN.to_csv('Unilever.csv')









