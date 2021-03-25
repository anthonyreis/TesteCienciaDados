def getStatistics(dataFrame):
    mean = dataFrame.mean()
    std_deviation = dataFrame.std()
    most_common = dataFrame.mode()
    variance = dataFrame.var()

    return {
        "mean": mean, 
        "std_deviation": std_deviation,
        "most_common": most_common[0],
        "variance": variance
    }