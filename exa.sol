pragma solidity 0.6.10;

contract exa {

    function ap () public returns (string memory) {
        if(tx.origin == msg.sender) {
            return "AAAA";
        }
        else {
            return "aaas";
            }
    }

}
