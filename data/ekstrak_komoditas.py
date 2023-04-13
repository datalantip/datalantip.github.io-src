import pandas as pd
import numpy as np 



df = pd.read_csv("pengeluaran_bulanan_jateng.csv")
print(df)

komoditas = list(df["Pengeluaran"].values)

for i in komoditas:
	df1 = df[df["Pengeluaran"]==i]
	df1 = df1.T
	df1.reset_index(inplace=True)
	df1.drop([0,1], inplace=True)
	df1.columns=["Tahun","Pengeluaran"]
	filename = i.split(",")[0]
	filename = filename.split("-")[0]
	filename = filename.replace(" ","-")
	df1.to_csv('pengeluaran-'+filename.lower()+'-sebulan-jateng.csv',index=False)

