pragma solidity 0.6.10;

contract example {


    function checkTxOrigin(address addr) public returns (string memory){
    
      if(tx.origin == addr) {
          return "checked !";
      }
      else {
          return "not origin";
       }
    }}
