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
A = cp.CountPs("Fisher") #name of statistic: Fisher, Pearson, Ed, Stouffer, George, Tippett
inputs = list(input1['x'].values.flatten())
Input = A.InfinitePs(inputs[0:5])
Output1 = A.StoufferMethod(Input[0]) #TODO check this one, just wrong
Output2 = A.GeorgeMethod(Input[0]) #TODO check this one, negative the ss. function is positive
Output3 = A.FisherMethod(Input[0]) 
Output4 = A.PearsonMethod(Input[0]) #TODO check this one, negative the ss. function is positive
Output5 = A.EdMethod(Input[0])
Output6 = A.TippettMethod(Input[0])
#print(Output6) #TODO the test statistic returned, need to convert it over to p-value based on distirbution.
#Need new function to return p value

#Testing using several of existing functions, mention that some do not follow the test statistics mentioned in 
#Heard 2017 paper
Fisher = ss.combine_pvalues(Input[0], "fisher")
print(Fisher)

def CombinedPvalue(output,Input):
        """
        Returns the p value of the combined pvalues based on the 
        method selected
        """
        n = len(Input)

        if cp.CountPs == 'Tippett':
            output = output
            output = beta.pdf(output,a = 1, b = n) #ST is Beta(1,n)
        elif cp.CountPs == 'Stouffer':
            output = output
            output = norm.pdf(output,scale = n) #SS is N(0,n)
        elif cp.CountPs == 'George':
            output = output
            output = gamma.pdf(output,a = n) #SG is Gamma(x,n)
        elif cp.CountPs == 'Ed':
            output = output
            output = gamma.pdf(output,a = n) #SE is Gamma(x,n)
        elif cp.CountPs == 'Pearson':
            output = output
            output = chi2.pdf(output,2*n) #SP is Chi-square df=2n
        else:
            output = output
            output = chi2.pdf(output,2*n) #SF is Chi-square df=2n
        
        return output

SignOrNot = CombinedPvalue(output = Output3, Input = Input[0])
print(Output3, SignOrNot) #TODO the test statistics are the same but the returned p-values are different




