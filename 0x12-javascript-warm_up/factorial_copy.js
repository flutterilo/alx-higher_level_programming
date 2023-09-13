#!/usr/bin/node

const num = Number(process.argv[2]);
let fact = 1;

if (num) {
  for (let i = 1; i <= num; i++) {
    fact *= i;
  }
  console.log(fact);
} else {
  console.log('not a number and fact is 1');
}
