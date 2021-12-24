
import random

class UserPool():
    def __init__(self, _amount, _rewardDebt) -> None:
        self.amount = _amount
        self.rewardDebt = _rewardDebt
        self.balance = 0

    def updateAmount(self, _amount, _Pool):
        self.amount += _amount
        _Pool.updatePoolBalance(_amount)
class Pool():
    # rewardPerBlock = 1.5
    def __init__(self, _alloc, _blockNumber):
        self.allocPoint = _alloc
        self.lastRewardBlock =_blockNumber
        self.accPerShare = 0
        self.poolBalance = 0
    
    def updatePoolBalance(self, amount):
        self.poolBalance +=amount
    
startblockNumber = 0
currentBlock = 0
rewardPerBlock = 1
total_alloc = 0
bonusMultiplier = 1
state = 0
cakePerblockList= [1,3,6,9,12,15,18,21,24,27,30,33,36,39]
poolList  = []
userUserPool = {
    1:[-1]*10,
    2:[-1]*10,
    3:[-1]*10,
    4:[-1]*10,
    5:[-1]*10,
    6:[-1]*10,
    7:[-1]*10,
    8:[-1]*10,
    9:[-1]*10,
    10:[-1]*10
    } 
poolUserPool = {} #1 -> [U1P, U2P, U3P] | 2 -> [UP4, UP5, UP6] | 3 -> [UP7, UP8, UP9]

def updateBonusMultplier(_mux):
    global bonusMultiplier
    bonusMultiplier = _mux

def updaterewardPerBlock(_reward):
    global rewardPerBlock
    rewardPerBlock = _reward

def getMultipler(lastRewardBlock, currentBlock):
    return (currentBlock - lastRewardBlock) * bonusMultiplier

def updatePools(_pid):
    pool = poolList[_pid]
    if currentBlock <= pool.lastRewardBlock:
        return
    
    totalSupply = pool.poolBalance
    if totalSupply==0:
        pool.lastRewardBlock = currentBlock
        return
    
    multiplier = getMultipler(pool.lastRewardBlock, currentBlock)
    reward = multiplier * rewardPerBlock * pool.allocPoint / total_alloc
    print(reward/10)
    print(reward)
    pool.accPerShare = pool.accPerShare + (reward*1e12/totalSupply)
    pool.lastRewardBlock = currentBlock

def updateStakingPool():
    points = 0

    for i in poolList:
        points += i.allocPoint
    
    if points!=0:
        points = points/3
        global total_alloc
        total_alloc = total_alloc - poolList[0].allocPoint  +points
        poolList[0].allocPoint = points

def massUpdatePools():
    for i in range(len(poolList)):
        updatePools(i)

def add(_allpoint, _withUpdate):
    
    if (poolList.length >0 and poolList.length%2 == 0) or poolList.length ==1:
        global state
        state +=1
        global rewardPerBlock
        rewardPerBlock = cakePerblockList[state]

    if _withUpdate:
        massUpdatePools()
    # lastreward = 0
    if currentBlock > startblockNumber:
        lastreward = currentBlock
    else:
        lastreward = startblockNumber
    global total_alloc
    total_alloc += _allpoint

    P = Pool(_allpoint, lastreward)
    poolList.append(P)
    poolUserPool[poolList.length] = [-1]*10
    updateStakingPool()

def deposit(_amount, _pid, _userID):

    if poolUserPool[_pid][_userID] == -1:
        userNew = UserPool(0,0)
        userUserPool[_userID][_pid] = userNew
        poolUserPool[_pid][_userID] = userNew

    updatePools(_pid)
    user = userUserPool[_userID][_pid]
    pool = poolList[_pid]
    if user.amount > 0:
        pending =( user.amount * (pool.accPerShare/1e12))- user.rewardDebt
        if pending > 0:
            print("Pending reward: ", pending)
            user.balance += pending
    
    if _amount > 0:
        user.updateAmount(_amount, pool)
    
    user.rewardDebt = user.amount * (pool.accPerShare/1e12)
    print("Deposited for", _amount, "to pool", _pid, "for user", _userID)

def withdraw(_amount, _pid, _userID):
    updatePools(_pid)
    user = userUserPool[_userID][_pid]
    pool = poolList[_pid]
    if user.amount > 0:
        pending =( user.amount * (pool.accPerShare/1e12))- user.rewardDebt
        if pending > 0:
            print("Pending reward: ", pending)
            user.balance += pending
    
    if _amount > 0:
        user.updateAmount(-_amount, pool)
    
    user.rewardDebt = user.amount * (pool.accPerShare/1e12)
    print("Withdrawn", _amount, "from pool", _pid, "for user", _userID)

def getReward( _Pool, _User):
    accPerShare = _Pool.accPerShare
    userSupply = _User.amount

    if (startblockNumber > _Pool.lastRewardBlock) and userSupply!=0:
        mul = _Pool.Multiplier
        rewardX = (rewardPerBlock * mul)/Pool.total_alloc
        accRespctPerShare = accPerShare + (rewardX*(1e12)/userSupply)
    
    return ((userSupply * accRespctPerShare)/(1e12))-(_User.rewardDebt)

def blockCounter():
    x = random.randint(1,7521)
    global currentBlock
    currentBlock += x

