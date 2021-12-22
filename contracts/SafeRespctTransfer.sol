
pragma solidity 0.6.12;

import "./RespctToken.sol";

contract SafeCakeTransfer {

    // SafeCakeTransfer is a library that allows to transfer tokens from one address to another
    CakeToken public cake;

    constructor(
            CakeToken _cake
        ) public {
            cake = _cake;
        }

        // Safe cake transfer function, just in case if rounding error causes pool to not have enough CAKEs.
        function safeCakeTransfer(address _to, uint256 _amount) public onlyOwner {
            uint256 cakeBal = cake.balanceOf(address(this));
            if (_amount > cakeBal) {
                cake.transfer(_to, cakeBal);
            } else {
                cake.transfer(_to, _amount);
            }
        }
}