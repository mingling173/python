#coding:UTF-8
import scipy.io as scio
dataFile = 'E://data.mat'
data = scio.loadmat(dataFile)
dataNew = 'E://data.mat'
scio.savemat(dataNew, {'A':data['A']})
