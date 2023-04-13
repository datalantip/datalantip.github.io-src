import pandas as pd
import numpy as np 



df_ori = pd.read_csv("populasi-ternak-menurut-kabupaten-kota-dan-jenis-ternak-di-provinsi-jawa-tengah-ekor.csv")
# print(df_ori.columns)
df_ori = df_ori.replace('-', np.nan)

i = 1
while i <len(df_ori.columns):
	ternak = df_ori.columns[i]
	# ternak = 'Sapi Potong'

	df = df_ori.drop([0,1,37,38,39,40])

	df_sapi = df.loc[:,[df.columns[0],ternak,df.columns[i+1],df.columns[i+2]]]

	df_sapi.columns = ['kota_kabupaten','2019','2020','2021']
	df_sapi['2021'] = df_sapi['2021'].astype(float)

	df_sapi_max = df_sapi.sort_values(['2021'],ascending=False)

	df_sapi_max = df_sapi_max.loc[:,['kota_kabupaten','2021']]

	df_sapi_max = df_sapi_max.iloc[:5]

	df_sapi_max.to_csv('populasi-'+ternak.lower().replace(" ","-")+'-terbesar-jateng-2021.csv',index=False)

	i+=3

# komoditas = list(df["Pengeluaran"].values)

# for i in komoditas:
# 	df1 = df[df["Pengeluaran"]==i]
# 	df1 = df1.T
# 	df1.reset_index(inplace=True)
# 	df1.drop([0,1], inplace=True)
# 	df1.columns=["Tahun","Pengeluaran"]
# 	filename = i.split(",")[0]
# 	filename = filename.split("-")[0]
# 	filename = filename.replace(" ","-")
# 	df1.to_csv('pengeluaran-'+filename.lower()+'-sebulan-jateng.csv',index=False)

	