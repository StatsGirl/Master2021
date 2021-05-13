library(testthat)        # load testthat package
library(combinationpvalues)       # load our package

# Test whether the output is a data frame
test_that("test whether InfinitePs returns a list", {
  output<- InfinitePs(0.2)
  expect_type(output, "list")
})

# Test whether InfinitePs returns length >= 2
test_that("test whether InfinitePs returns length >= 2", {
  output<- InfinitePs(0.2)
  expect_gte(length(output), 2)
})

## Test whether one of the six functions return one p value only
test_that("Test whether one of the six functions return one p value only",
          {
            output <- StoufferMethod(c(0.1,0.4,0.02))
            expect_length(output, 1)
          })
