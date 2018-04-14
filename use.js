/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
function checkfiles()
            {
                var fup=document.getElementById('l1');
                var t = fup.innerText;
                if(t=='Not in fasta format: please check')
                {
                 fup.focus();
                 return false;
                }
               else
               {
                return true;            
               }
           }
