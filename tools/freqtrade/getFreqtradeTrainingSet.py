
def getTrainingSet(totalBank, timerange, strategy, configuration,  hyperopt, hyperoptLoss, epoch, timeframe):
    backtesting = "freqtrade backtesting --config %s.json -s %s --timerange=%s --dry-run-wallet %s --timeframe %s"%(configuration,strategy,timerange,totalBank, timeframe)
    hyperoptimization = "freqtrade hyperopt --hyperopt %s --hyperopt-loss %s --spaces all --strategy %s --config %s.json -e %s --timerange=%s --dry-run-wallet %s --timeframe %s"%(hyperopt,hyperoptLoss,strategy,configuration,epoch,timerange,totalBank, timeframe)
    data = "freqtrade download-data --config %s.json --timeframe %s"%(configuration, timeframe)
    trade = "freqtrade trade --config %s.json -s %s --dry-run-wallet %s"%(configuration,strategy, totalBank)
    plot = "freqtrade plot-dataframe --strategy %s --config %s.json --export-filename user_data/backtest_results/backtest-result.json -p BTC/USDT"%(strategy, configuration)
    print(backtesting)
    print(hyperoptimization)
    print(data)
    print(trade)
    print(plot)

timeframes = ['5m','30m', '1h','4h','1d']
for time in timeframes:
    print(time)
    #getTrainingSet('0.063', '20210101-', 'mabStra', 'configBTCUSDT', 'mabStraHo', 'SharpeHyperOptLossDaily', '100', time)
    #getTrainingSet('2.5', '20210319-20210401', 'Quickie', 'configAltEth', 'mabStraHo', 'SharpeHyperOptLossDaily', '100', time)
    #getTrainingSet('1.0', '20210101-', 'BbandRsi', 'configBTCUSDT', 'AwesomeHyperopt', 'SharpeHyperOptLossDaily', '100', time)
    getTrainingSet('1.20', '20210301-', 'mabStra', 'configAltEthBull', 'mabStraHo', 'SharpeHyperOptLossDaily', '100', time)
    #getTrainingSet('1.5', '20210326-', 'mabStra', 'configAltEth2Bull', 'mabStraHo', 'SharpeHyperOptLossDaily', '100', time)
    #getTrainingSet('0.063', '20210101-', 'Heracles', 'configAltBTCBull', 'HeraclesHo', 'SharpeHyperOptLossDaily', '100', time)
    #getTrainingSet('0.005', '20210101-', 'Heracles', 'configAltBTCBull', 'HeraclesHo', 'SharpeHyperOptLossDaily', '100', time)
    #getTrainingSet('1.0', '20210415-', 'GodStra', 'configAltEth', 'mabStraHo', 'SharpeHyperOptLossDaily', '100', time)


