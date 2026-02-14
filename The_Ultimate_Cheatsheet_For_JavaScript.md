# JavaScript Programming

---

## Index

| * | Table of Contents |
|---|-------------------|
| - | [Variables](#variables) |
| - | [Printing](#printing) |
| - | [Arithmetic](#arithmetic) |
| - | [Strings](#strings) |
| - | [Arrays](#arrays) |
| - | [Objects](#objects) |
| - | [Maps](#maps) |
| - | [Sets](#sets) |
| - | [Destructuring](#destructuring) |
| - | [Conditionals](#conditionals) |
| - | [For Loops](#for-loops) |
| - | [While Loops](#while-loops) |
| - | [Functions](#functions) |
| - | [File I/O](#file-io) |
| - | [Command Line Arguments](#command-line-arguments) |
| - | [Exception Handling](#exception-handling) |
| - | [Exit Codes](#exit-codes) |

---

## Variables

```javascript
const name = "Alice";               // string (immutable binding)
let pi = 3.14;                      // float (mutable)
let count = 42;                     // integer
let isValid = true;                 // boolean
let nothing = null;                 // null value
let notDefined = undefined;         // undefined

// Type checking
typeof name;                        // 'string'
typeof count;                       // 'number'
Array.isArray([1, 2]);              // true

// Type conversion
parseInt("42");                     // string to int
parseFloat("3.14");                 // string to float
String(42);                         // int to string
Number("42");                       // string to number
Boolean(1);                         // number to bool (true)
[..."abc"];                         // ['a', 'b', 'c']
```

---

## Printing

```javascript
console.log(name);                  // print variable
console.log(`Hello ${name}`);       // template literal
console.log("Sum:", 3 + 5);         // multiple arguments
console.log("a", "b", "c");         // a b c

// Formatting
console.log(pi.toFixed(2));         // '3.14' (2 decimal places)
console.log(count.toString().padStart(5, "0")); // '00042'
console.log(name.padStart(10));     // right-align, width 10
console.log(name.padEnd(10));       // left-align, width 10

// Other console methods
console.error("Error message");     // stderr
console.warn("Warning");            // warning
console.table([{a: 1}, {a: 2}]);    // tabular display
```

---

## Arithmetic

```javascript
3 + 5;                              // 8 (addition)
3 - 1;                              // 2 (subtraction)
3 * 5;                              // 15 (multiplication)
5 / 2;                              // 2.5 (division)
Math.floor(5 / 2);                  // 2 (integer division)
5 % 2;                              // 1 (modulus)
2 ** 3;                             // 8 (exponent)

// Assignment operators
let x = 10;
x += 5;                             // x = x + 5
x -= 3;                             // x = x - 3
x *= 2;                             // x = x * 2
x /= 4;                             // x = x / 4
x **= 2;                            // x = x ** 2

// Built-in math functions
Math.abs(-5);                       // 5
Math.round(3.7);                    // 4
Math.round(3.14159 * 100) / 100;    // 3.14
Math.pow(2, 3);                     // 8
Math.sqrt(16);                      // 4
Math.floor(3.7);                    // 3
Math.ceil(3.2);                     // 4
Math.PI;                            // 3.141592...
Math.max(1, 2, 3);                  // 3
Math.min(1, 2, 3);                  // 1
```

---

## Strings

```javascript
const string = "hello world";
```

### Access & Slicing

```javascript
string[0];                          // 'h' (indexing)
string.at(-1);                      // 'd' (last char)
string.slice(0, 5);                 // 'hello'
string.slice(6);                    // 'world'
string.slice(-5);                   // 'world'
string.length;                      // 11
```

### Modify / Transform

```javascript
string.replace("world", "JS");      // 'hello JS' (first only)
string.replaceAll("l", "L");        // 'heLLo worLd'
string.toUpperCase();               // 'HELLO WORLD'
string.toLowerCase();               // 'hello world'
string.trim();                      // remove leading/trailing whitespace
string.trimStart();                 // remove leading whitespace
string.trimEnd();                   // remove trailing whitespace
string.repeat(2);                   // 'hello worldhello world'
```

### Searching & Checking

```javascript
string.indexOf("world");            // 6 (-1 if not found)
string.lastIndexOf("o");            // 7
string.startsWith("hell");          // true
string.endsWith("orld");            // true
string.includes("world");           // true

// Character checks (via regex)
/^\d+$/.test("123");                // true (all digits)
/^[a-zA-Z]+$/.test("abc");          // true (all letters)
```

### Splitting & Joining

```javascript
const words = string.split(" ");    // ['hello', 'world']
const parts = "a:b:c".split(":", 2);// ['a', 'b']
const chars = [...string];          // ['h', 'e', 'l', ...]

words.join(" ");                    // 'hello world'
["a", "b", "c"].join(", ");         // 'a, b, c'
```

### Concatenation & Formatting

```javascript
"hello" + " " + "world";            // 'hello world'
`Hello ${name}`;                    // template literal
```

---

## Arrays

```javascript
const arr = ["one", "two", "three"];
const empty = [];
const nums = Array.from({length: 5}, (_, i) => i); // [0, 1, 2, 3, 4]
```

### Access & Slicing

```javascript
arr[0];                             // 'one'
arr.at(-1);                         // 'three' (last element)
arr.slice(1, 3);                    // ['two', 'three']
arr.slice(-2);                      // last 2 elements
[...arr].reverse();                 // reversed copy
arr.length;                         // 3
```

### Add / Insert

```javascript
arr.push("four");                   // add at end
arr.unshift("zero");                // add at start
arr.splice(1, 0, "new");            // insert at index 1
arr.concat(["five", "six"]);        // return new merged array
```

### Remove

```javascript
arr.pop();                          // remove and return last
arr.shift();                        // remove and return first
arr.splice(1, 2);                   // remove 2 elements at index 1
arr.length = 0;                     // clear array
```

### Sorting & Reversing

```javascript
arr.sort();                         // sort in place (alphabetical)
arr.sort((a, b) => a - b);          // sort numbers ascending
arr.sort((a, b) => b - a);          // sort numbers descending
arr.reverse();                      // reverse in place
[...arr].sort();                    // return sorted copy
```

### Searching

```javascript
arr.indexOf("two");                 // index of first occurrence
arr.includes("one");                // true
arr.find(x => x.length > 3);        // first match or undefined
arr.findIndex(x => x.length > 3);   // index of first match or -1
arr.filter(x => x.length > 3);      // all matches
```

### Transforming

```javascript
arr.map(x => x.toUpperCase());      // transform each element
arr.filter(x => x.length > 3);      // filter elements
arr.reduce((sum, x) => sum + x, 0); // reduce to single value
arr.forEach(x => console.log(x));   // iterate (no return)
```

---

## Objects

```javascript
const obj = {one: 1, two: 2, three: 3};
const empty = {};
const fromEntries = Object.fromEntries([["a", 1], ["b", 2]]);
```

### Access

```javascript
obj.one;                            // 1
obj["one"];                         // 1
obj.four;                           // undefined
obj.four ?? 4;                      // 4 (nullish coalescing)
```

### Add / Update

```javascript
obj.four = 4;                       // add or update
Object.assign(obj, {five: 5});      // merge into obj
const merged = {...obj, six: 6};    // spread into new object
```

### Remove

```javascript
delete obj.three;                   // delete property
```

### Keys, Values & Iteration

```javascript
Object.keys(obj);                   // ['one', 'two', 'three']
Object.values(obj);                 // [1, 2, 3]
Object.entries(obj);                // [['one', 1], ['two', 2], ...]

for (const key in obj) {
    console.log(key, obj[key]);
}

for (const [key, value] of Object.entries(obj)) {
    console.log(key, value);
}
```

### Membership

```javascript
"one" in obj;                       // true
obj.hasOwnProperty("one");          // true
Object.hasOwn(obj, "one");          // true (ES2022)
```

---

## Maps

```javascript
const map = new Map([["one", 1], ["two", 2]]);
const empty = new Map();
```

### Access & Modify

```javascript
map.get("one");                     // 1
map.get("missing");                 // undefined
map.set("three", 3);                // add or update
map.has("one");                     // true
map.delete("two");                  // remove
map.clear();                        // remove all
map.size;                           // number of entries
```

### Iteration

```javascript
for (const [key, value] of map) {
    console.log(key, value);
}

map.keys();                         // iterator of keys
map.values();                       // iterator of values
map.entries();                      // iterator of [key, value]
map.forEach((value, key) => console.log(key, value));
```

---

## Sets

```javascript
const set = new Set([1, 2, 3]);
const empty = new Set();
const fromArray = new Set([1, 2, 2, 3]); // {1, 2, 3}
```

### Add / Remove

```javascript
set.add(4);                         // add element
set.delete(2);                      // remove element
set.has(1);                         // true
set.clear();                        // remove all
set.size;                           // number of elements
```

### Set Operations

```javascript
const a = new Set([1, 2, 3]);
const b = new Set([3, 4, 5]);

// Union
new Set([...a, ...b]);              // {1, 2, 3, 4, 5}

// Intersection
new Set([...a].filter(x => b.has(x))); // {3}

// Difference
new Set([...a].filter(x => !b.has(x))); // {1, 2}

// Convert to array
[...set];                           // [1, 2, 3]
Array.from(set);                    // [1, 2, 3]
```

---

## Destructuring

### Array Destructuring

```javascript
const [a, b] = [1, 2];              // a=1, b=2
const [first, ...rest] = [1, 2, 3, 4]; // first=1, rest=[2,3,4]
const [x, , z] = [1, 2, 3];         // x=1, z=3 (skip middle)
const [val = 0] = [];               // default value
```

### Object Destructuring

```javascript
const {one, two} = {one: 1, two: 2}; // one=1, two=2
const {one: first} = {one: 1};      // rename: first=1
const {missing = 0} = {};           // default value
const {a, ...others} = {a: 1, b: 2, c: 3}; // rest
```

### Nested Destructuring

```javascript
const {user: {name}} = {user: {name: "Alice"}};
const [[a, b], [c, d]] = [[1, 2], [3, 4]];
```

### Function Parameters

```javascript
function greet({name, age}) {
    console.log(`${name} is ${age}`);
}
greet({name: "Alice", age: 25});

// With defaults
function config({port = 3000, host = "localhost"} = {}) {
    console.log(port, host);
}
```

### Spread Operator

```javascript
// Merge arrays
const merged = [...arr1, ...arr2];

// Merge objects
const merged = {...obj1, ...obj2};

// Copy
const copy = [...arr];
const copy = {...obj};
```

---

## Conditionals

### If / Else If / Else

```javascript
const x = 10;

if (x > 0) {
    console.log("Positive");
} else if (x === 0) {
    console.log("Zero");
} else {
    console.log("Negative");
}
```

### Logical Operators

```javascript
if (x > 0 && x < 20) {
    console.log("Between 1 and 19");
}

if (x < 0 || x > 100) {
    console.log("Out of range");
}

if (x !== 10) {
    console.log("Not 10");
}
```

### Truthiness / Empty Checks

```javascript
// Falsy: false, 0, '', null, undefined, NaN

if (!string) {                      // empty string check
    console.log("Empty");
}

if (arr.length) {                   // non-empty array check
    console.log("Has items");
}

if (value === null) {
    console.log("Is null");
}

if (value != null) {                // not null or undefined
    console.log("Has value");
}
```

### Ternary Operator

```javascript
const result = condition ? "Yes" : "No";
const value = x > 0 ? x : 0;
```

### Nullish Coalescing & Optional Chaining

```javascript
const val = maybeNull ?? "default"; // only null/undefined
const val = maybeNull || "default"; // any falsy value

const name = user?.profile?.name;   // safe property access
const result = obj?.method?.();     // safe method call
```

### Switch

```javascript
switch (value) {
    case 1:
        console.log("One");
        break;
    case 2:
        console.log("Two");
        break;
    default:
        console.log("Other");
}
```

---

## For Loops

### Basic Iteration

```javascript
const arr = ["one", "two", "three"];

for (const item of arr) {
    console.log(item);
}
```

### With Index

```javascript
for (let i = 0; i < arr.length; i++) {
    console.log(i, arr[i]);
}

arr.forEach((item, i) => {
    console.log(i, item);
});
```

### Object Iteration

```javascript
const obj = {one: 1, two: 2};

for (const key in obj) {
    console.log(key, obj[key]);
}

for (const [key, value] of Object.entries(obj)) {
    console.log(key, value);
}
```

### Range-like Loops

```javascript
for (let i = 0; i < 5; i++) {       // 0, 1, 2, 3, 4
    console.log(i);
}

for (let i = 2; i < 10; i++) {      // 2, 3, ..., 9
    console.log(i);
}

for (let i = 0; i < 10; i += 2) {   // 0, 2, 4, 6, 8
    console.log(i);
}

for (let i = 10; i > 0; i--) {      // 10, 9, ..., 1
    console.log(i);
}
```

### Multiple Arrays (zip-like)

```javascript
const names = ["Alice", "Bob"];
const ages = [25, 30];

names.forEach((name, i) => {
    console.log(name, ages[i]);
});

// Or with map
names.map((name, i) => [name, ages[i]]);
```

---

## While Loops

### Basic While

```javascript
let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}
```

### Do While

```javascript
let i = 0;
do {
    console.log(i);
    i++;
} while (i < 5);
```

### Break and Continue

```javascript
let i = 0;
while (i < 10) {
    i++;
    if (i === 3) continue;          // skip to next iteration
    if (i === 7) break;             // exit loop
    console.log(i);
}
```

### Infinite Loop

```javascript
while (true) {
    const input = prompt("Enter (q to quit):");
    if (input === "q") break;
}
```

---

## Functions

### Basic Function

```javascript
function greet(name) {
    console.log(`Hello ${name}`);
}

greet("Alice");                     // Hello Alice
```

### Return Values

```javascript
function add(a, b) {
    return a + b;
}

const result = add(2, 3);           // 5

// Multiple return values (via array/object)
function getStats(nums) {
    return [Math.min(...nums), Math.max(...nums), nums.reduce((a, b) => a + b)];
}

const [low, high, total] = getStats([1, 2, 3]);
```

### Default Arguments

```javascript
function greet(name = "World") {
    console.log(`Hello ${name}`);
}

greet();                            // Hello World
greet("Alice");                     // Hello Alice
```

### Rest Parameters

```javascript
function sumAll(...nums) {
    return nums.reduce((a, b) => a + b, 0);
}

sumAll(1, 2, 3, 4);                 // 10
```

### Arrow Functions

```javascript
const square = x => x ** 2;
square(5);                          // 25

const add = (x, y) => x + y;
add(2, 3);                          // 5

const greet = name => {
    console.log(`Hello ${name}`);
};

// With array methods
const nums = [1, 2, 3, 4, 5];
nums.map(x => x ** 2);              // [1, 4, 9, 16, 25]
nums.filter(x => x % 2 === 0);      // [2, 4]
nums.sort((a, b) => b - a);         // [5, 4, 3, 2, 1]
```

### Async Functions

```javascript
async function fetchData(url) {
    const response = await fetch(url);
    return response.json();
}

// Arrow async
const fetchData = async (url) => {
    const response = await fetch(url);
    return response.json();
};
```

---

## File I/O

### Node.js (Synchronous)

```javascript
const fs = require("fs");

// Read
const content = fs.readFileSync("file.txt", "utf8");
const lines = content.split("\n");

// Write
fs.writeFileSync("file.txt", "Hello World\n");

// Append
fs.appendFileSync("file.txt", "New line\n");
```

### Node.js (Asynchronous with Promises)

```javascript
const fs = require("fs/promises");

// Read
const content = await fs.readFile("file.txt", "utf8");

// Write
await fs.writeFile("file.txt", "Hello World\n");

// Append
await fs.appendFile("file.txt", "New line\n");
```

### File Operations

```javascript
const fs = require("fs");
const path = require("path");

fs.existsSync("file.txt");          // check if exists
fs.statSync("file.txt").isFile();   // is a file?
fs.statSync("dir").isDirectory();   // is a directory?
fs.statSync("file.txt").size;       // file size in bytes
fs.unlinkSync("file.txt");          // delete file
fs.renameSync("old.txt", "new.txt");// rename
fs.readdirSync(".");                // list directory
fs.mkdirSync("path/to/dir", {recursive: true}); // create directories
```

---

## Command Line Arguments

```javascript
// Node.js
process.argv[0];                    // node executable
process.argv[1];                    // script path
process.argv[2];                    // first argument
process.argv.slice(2);              // all arguments
```

### Using Commander (recommended)

```javascript
const {program} = require("commander");

program
    .argument("<filename>", "Input file")
    .option("-v, --verbose", "Verbose output")
    .option("-n, --number <n>", "Number of items", 10)
    .parse();

const options = program.opts();
const filename = program.args[0];

console.log(filename);
console.log(options.verbose);
console.log(options.number);
```

---

## Exception Handling

### Try / Catch

```javascript
try {
    const x = JSON.parse(input);
    const result = 10 / x;
} catch (e) {
    if (e instanceof SyntaxError) {
        console.log("Invalid JSON");
    } else {
        console.log(`Error: ${e.message}`);
    }
}
```

### Try / Catch / Finally

```javascript
try {
    const data = fs.readFileSync("data.txt", "utf8");
    console.log("Success!");
} catch (e) {
    console.log("File not found");
} finally {
    console.log("Cleanup");         // always runs
}
```

### Throwing Errors

```javascript
function divide(a, b) {
    if (b === 0) {
        throw new Error("Cannot divide by zero");
    }
    return a / b;
}

// Re-throw
try {
    riskyOperation();
} catch (e) {
    console.log("Error occurred");
    throw e;                        // re-throw
}
```

### Common Error Types

| Error | Description |
|-------|-------------|
| `Error` | Generic error |
| `TypeError` | Wrong type |
| `ReferenceError` | Undefined variable |
| `SyntaxError` | Invalid syntax |
| `RangeError` | Value out of range |

### Async Error Handling

```javascript
// With async/await
try {
    const data = await fetchData(url);
} catch (e) {
    console.log("Fetch failed");
}

// With promises
fetchData(url)
    .then(data => console.log(data))
    .catch(e => console.log("Fetch failed"));
```

---

## Exit Codes

```javascript
// Node.js
process.exit(0);                    // success
process.exit(1);                    // failure

process.exitCode = 1;               // set exit code without exiting
```

---

[↑ Back to Index](#index)
