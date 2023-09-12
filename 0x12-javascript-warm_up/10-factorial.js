#!/usr/bin/node

const num = Number(process.argv[2]);

if (num) {
  let fact = 1;
  for (let i = 1; i <= num; i++) {
    fact *= i;
  }
  console.log(fact);
} else {
  console.log(1);
}
