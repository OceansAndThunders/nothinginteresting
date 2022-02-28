pragma solidity 0.6.10;

contract exa {

    function ap () external returns (string memory) {
        if(tx.origin == msg.sender) {
            return "AAAA";
        }
        else {
            return "aaas";
            }
    }

}
