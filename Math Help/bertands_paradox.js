var n_length =0;
var n_area =0;
for (var i=0; i<10000; i++){
  var length = Math.random()*3;
  var area =  Math.random()*9;
  if (length<1){
    n_length +=1;
  }
  if (area<1){
    n_area +=1;
  }
}
console.log((n_length/i),(n_area/i))
