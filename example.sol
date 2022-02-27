pragma solidity 0.6.10;



contract example_contract{
 function checkTXO () public returns (string memory) {
   if (tx.origin == msg.sender) {
         return 'they are the same';
         // do stuff
   }
   else {
         return 'not the same';
   }
 }
}
