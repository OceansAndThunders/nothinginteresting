pragma solidity 0.6.10;



contract example_contract {

    function transfer(address payable receipent, uint amount) public {
        require(tx.origin == msg.sender, "not authorized");

        (bool sent, ) = receipent.call{value: amount}("");
        require(sent, "something wrong");
    }
}
