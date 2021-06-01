# Master2021

Thesis repo contains the Python and R code created by Breya McGlown under the guidance of E. Olusegun George.

Both languages provide the end user the opportunity to utilize six fundamental statistics used for combination of p-values and calculate the combined p value based on the method selected, typically used during Meta-analyses.

To Use: 

    Python: 
    
    1) pip install P-CombiningPValuesFinal
    2) Below is an example of how to use the functions within the package, also refer to tests in the packaging_tutorial folder
        inputs = list(input1['x'].values.flatten())
        Input = A.InfinitePs(inputs[0:5])
        Output1 = A.StoufferMethod(Input[0])
        SignOrNot = cp.CombinedPvalue(output = Output1, Input = Input[0])
    3) The function CombinedPvalue will return the combined p-value based on the method selected
    
    R: 

    1) install.packages("combinationpvalues")
    2) Below is an example of how to use the functions within the package, also refer to the examples in the package by calling example("combinationpvalues")
        Output <- InfinitePs(0.1,0.3,.7)
        Final <- TippettMethod(Output)
        Combined <- CombinedPValueMethod(Final,"Tippett")
    3) The function CombinedPValueMethod will return the combined p-value based on the method selected

