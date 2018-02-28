console.log();

var x = 5;

var l = [1, 2, 3, 4]
l.length
l[0]
l.push(5)
l.slice(0, 3)
String()
parseInt()

true, false

var d = {'key1': 'value2', 'key2': 'value2'}
d.key1
d['key1']

for (var number in l) { // this is considered bad practice, I should remove this
  console.log(number);
}

for (i = 0; i <= l.length; i++) {
  console.log(number)
}

function foo(a) {
  return a
}

console.log(foo(5))

var i = 0
if (i == 0) {
  console.log(i)
}
if (i < 10) {
  console.log(i)
  i += 1
} else if (i < 5) {
  console.log(i * 2)
} else {
  console.log('hello')
}


document.getElementById();
document.getElementsByTagName();
document.getElementsByClassName();
document.querySelectorAll("p .animal"); // selects by CSS. This will get elements with the class animal between <p> and </p>
document.querySelector("#animal"); // returns single tag by the animal id
