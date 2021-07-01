#import P_CombiningPValuesFinal as cp
import P_CombiningPValuesFinal as cp
import pandas as pd
import scipy.stats as ss
from scipy.stats import t
from scipy.stats import chi2
from scipy.stats import gamma
from scipy.stats import beta
from scipy.stats import norm
input1 = pd.read_csv("~/Desktop/Thesis2021/DataSets/metap_beckerp.csv")

print(input1['x'].values[0:5])
A = cp.CountPs("Tippett") #name of statistic: Fisher, Pearson, Ed, Stouffer, George, Tippett
inputs = list(input1['x'].values.flatten())
Input = A.InfinitePs(inputs[0:5])
Output1 = A.StoufferMethod(Input[0]) 
Output2 = A.GeorgeMethod(Input[0]) 
Output3 = A.FisherMethod(Input[0]) 
Output4 = A.PearsonMethod(Input[0])
Output5 = A.EdMethod(Input[0])
Output6 = A.TippettMethod(Input[0])

#Testing using several of existing functions, mention that some do not follow the test statistics mentioned in 
#Heard 2017 paper
Fisher = ss.combine_pvalues(Input[0], "fisher")
print(Fisher," other package")


SignOrNot = A.CombinedPvalue(output = Output3)
print(Output3, SignOrNot, "my package Fisher")

#A = cp.CountPs("Pearson")
Fisher = ss.combine_pvalues(Input[0], "pearson")
print(Fisher," other package")


SignOrNot = A.CombinedPvalue(output = Output5)
print(Output5, SignOrNot, "my package Ed")

#A = cp.CountPs("Tippett")
Fisher = ss.combine_pvalues(Input[0], "tippett")
print(Fisher," other package")


SignOrNot = A.CombinedPvalue(output = Output6)
print(Output6, SignOrNot, "my package Tippett")

#A = cp.CountPs("Stouffer")
Fisher = ss.combine_pvalues(Input[0], "stouffer")
print(Fisher," other package")


SignOrNot = A.CombinedPvalue(output = Output1)
print(Output1, SignOrNot, "my package stouffer")

#A = cp.CountPs("George")
Fisher = ss.combine_pvalues(Input[0], "mudholkar_george")
print(Fisher," other package")


SignOrNot = A.CombinedPvalue(output = Output2)
print(Output2, SignOrNot, "my package George")

