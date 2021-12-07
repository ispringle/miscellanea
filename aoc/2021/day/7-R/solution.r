data <- t(read.table("input.txt",header=FALSE,sep=","))
fuel <- sum(abs(median(data) - data))
print(fuel)

target_a <- ceiling(mean(data))
target_b <- floor(mean(data))
used <- function(x) x * (x + 1) / 2
fuel <- min(sum(used(abs(target_a - data))), sum(used(abs(target_b - data))))
print(fuel)
