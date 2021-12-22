
pragma solidity 0.6.12;

import '@pancakeswap/pancake-swap-lib/contracts/access/Ownable.sol';
import "./RespctToken.sol";

contract SafeRespctTransfer is Ownable{

    // SafeRespctTransfer is a library that allows to transfer tokens from one address to another
    RespctToken public respct;

    constructor(RespctToken _respct ) public {
        respct = _respct;
    }

    // Safe respct transfer function, just in case if rounding error causes pool to not have enough RESPCTs.
    function safeRespctTransfer(address _to, uint256 _amount) public onlyOwner {
        uint256 respctBal = respct.balanceOf(address(this));
        if (_amount > respctBal) {
            respct.transfer(_to, respctBal);
        } else {
            respct.transfer(_to, _amount);
        }
    }
    
}