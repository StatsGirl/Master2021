#' @title TippettMethod
#'
#' @description #' Combination p-value method that uses Tippett statistic
#' min(p1,...,pn), n= 2,3,...,k where p equals p-value
#' 
#' @param x #' InfinitePs
#'
#' @return Combined P-value
#' @examples
#' Output <- InfinitePs(0.1,0.3,.7)
#' Final <- TippettMethod(Output)
#' @export
#' @importFrom dplyr "%>%"
#' 
TippettMethod = function(x){
            if (self.method == "Tippett"){
            temp <- Reduce(min,x)
            output <- temp
            return(output)
            }
        }