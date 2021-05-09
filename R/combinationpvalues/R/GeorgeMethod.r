#' @title PearsonsMethod
#'
#' @description #' Combination p-value method that uses George statistic
#' Summation i=1 to n log(pi/(1-pi)) where p equals p-value
#' 
#' @param x #' InfinitePs
#'
#' @return Combined P-value
#' @examples
#' Output <- InfinitePs(0.1,0.3,.7)
#' Final <- GeorgeMethod(Output)
#' @export
#' @importFrom dplyr "%>%"
#' 

GeorgeMethod = function(x) {
            if (self.method == "George"){
            k <- 1
            Len<- length(x)
            temp <-vector("list",Len)
            for (i in x) {
            temp[[k]]<- log(i/(1-i))
            k <- k + 1
            }
            temp1 <- Reduce("+",temp)
            output <- temp1
            return(output)
            }
        }