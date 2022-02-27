pragma solidity 0.6.10;

contract example {


    function checkTxOrigin(address addr) public returns (memory string){
    
      if(tx.origin == addr) {
          return "checked !";
      }
      else {
          return "not origin";
       }
    }}
