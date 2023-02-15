

hist_from_count = function(countfile, upper = 500, lower = -upper, varname = "temperature", ...)
{
    d = read.table(countfile, row.names = NULL)
    colnames(d) = c("count", "value")
    d[["count"]] = as.numeric(d[["count"]])
    d = d[lower < d[["value"]] & d[["value"]] < upper, ]
    result = hist(d[["value"]], plot = FALSE, ...)
    d[["bin"]] = cut(d[["value"]], breaks = result[["breaks"]])
    counts = tapply(d[["count"]], d[["bin"]], sum)
    counts[is.na(counts)] = 0

    result[["counts"]] = counts
    result[["density"]] = counts / sum(counts)
    result[["xname"]] = varname
    result
}

h = hist_from_count("TMAX.txt")
plot(h)

