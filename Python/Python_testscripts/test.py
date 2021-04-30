import P_CombiningPValuesFinal as cp

A = cp.CountPs("Stouffer") #name of statistic: Fisher, Pearson, Ed, Stouffer, George, Tippett
Input = A.InfinitePs(0.1,.3,.7)
Output = A.StoufferMethod(Input)
print(Output)






