let arr = [1, 2, 55, 5, 6, 89, 900, 958545, 457];
let largestNumber = arr[0];
const largestNum = () => {
  for (i = 0; i < arr.length; i++) {
    if (arr[i] > largestNumber) {
      largestNumber = arr[i];
    }
  }
  return largestNumber;
};
console.log(largestNum());

