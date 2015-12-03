import numpy as np

tsta = np.random.randint(9, size=(11, 13))
tstb = np.random.randint(9, size=(11, 13))

[nRows,nCols] = np.shape(tsta)

rowInds = np.repeat(range(0,nRows),nCols)
colInds = np.asarray(range(0,nCols)*nRows)

allInds = (rowInds,colInds)

indLst = range(0,(np.shape(allInds)[1]))

winSize = 5

for ind in indLst:
    centerInds = (allInds[0][ind],allInds[1][ind])
    minWndwRows = centerInds[0]-2
    if minWndwRows < 0: minWndwRows = 0
    maxWndwRows = centerInds[0]+2
    if maxWndwRows > nRows: maxWndwRows = nRows
    minWndwCols = centerInds[1]-2
    if minWndwCols < 0: minWndwCols = 0
    maxWndwCols = centerInds[1]+2
    if maxWndwCols > nCols: maxWndwCols = nCols

    actNrows = maxWndwRows-minWndwRows+1
    actNcols = maxWndwCols-minWndwCols+1

    wndwRowInds = np.repeat(range(minWndwRows,(maxWndwRows+1)),actNcols)
    wndwColInds = np.asarray(range(minWndwCols,(maxWndwCols+1))*actNrows)
    wndwRowInds[wndwRowInds<0] = 0
    wndwColInds[wndwColInds<0] = 0
    allWndwInds = (wndwRowInds,wndwColInds)

