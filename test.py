
class User():
    def __init__(self, _id, _amount, _rewardDebt) -> None:
        self.pool_id = _id
        self.amount = _amount
        self.rewardDebt = _rewardDebt

    def updateAmount(self, _amount, _Pool):
        self.amount += _amount
        _Pool.updatePoolBalance(_amount)


class Pool():
    pool_id = 0
    total_alloc = 0
    # rewardPerBlock = 1.5
    def __init__(self, _alloc, _blockNumber):
        Pool.total_alloc += _alloc
        Pool.pool_id += 1

        self.id = Pool.pool_id
        self.Multiplier = _alloc
        self.lastRewardBlock =_blockNumber
        self.accPerShare = 0
        self.poolBalance = 0
    
    def updatePoolBalance(self, amount):
        self.poolBalance +=amount
    

blockNumber = 0
rewardPerBlock = 1.5


def updateStakingPool(_User, _Pool):
    
    pass



def getReward( _Pool, _User):

    accPerShare = _Pool.accPerShare
    userSupply = _User.amount

    if (blockNumber > _Pool.lastRewardBlock) and userSupply!=0:
        mul = _Pool.Multiplier
        rewardX = (rewardPerBlock * mul)/Pool.total_alloc
        accRespctPerShare = accPerShare + (rewardX*(1e12)/userSupply)
    
    return ((userSupply * accRespctPerShare)/(1e12))-(_User.rewardDebt)



