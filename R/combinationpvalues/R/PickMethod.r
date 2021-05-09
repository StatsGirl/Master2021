#' @title PickMethod
#'
#' @description function that allows the user to define which method of combination p-value 
#' they want use
#' 
#'
#' @param method A data set object
#'
#' @return Allows for the proper function to be selected
#' @examples
#' my_object <- PickMethod("Perason")
#' @export
#' @importFrom dplyr "%>%"
#' 
#' 
PickMethod <- function(x) {
            self.method<- x
            structure(class = "PickMethod")}

