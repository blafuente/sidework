let myArr = [1, 2, 1, 2, 1, 3, 2];
let n = 7;

let arr = myArr.sort()
console.log(arr)
let matchingPair = 0;

for(let i=0; i < arr.length; i++){
    if(arr[i] === arr[i+1]){
        matchingPair++;
        i++
    }
}

console.log(matchingPair)