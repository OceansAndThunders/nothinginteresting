pragma solidity 0.6.10;



contract example_contract{
 function checkTXO () public returns (bool) {
   if (tx.origin == msg.sender) {
         return true;
         // do stuff
   }
   else {
         return false;
   }
 }
}
