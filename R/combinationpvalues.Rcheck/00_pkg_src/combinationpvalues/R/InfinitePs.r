#' @title InfinitePs
#'
#' @description Converts a list of p-values into a list, n= 2,3,...,k
#'
#' @param(x) #' Input n p-values  n = 2,3,...,k
#'
#' @return List of p-values
#' @examples
#' Output <- InfinitePs(0.1,0.3,.7)
#' @export
#' @importFrom dplyr "%>%"
#'

InfinitePs = function(x,...){
    kwargs<-list(...)
    return(c(x,kwargs))
    }
