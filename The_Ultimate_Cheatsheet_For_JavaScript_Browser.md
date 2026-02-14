# JavaScript (Browser)

---

## Index

| * | Table of Contents |
|---|-------------------|
| - | [DOM Selection](#dom-selection) |
| - | [DOM Manipulation](#dom-manipulation) |
| - | [Events](#events) |
| - | [Forms](#forms) |
| - | [Storage](#storage) |
| - | [Fetch API](#fetch-api) |
| - | [URL & Navigation](#url--navigation) |
| - | [Timers](#timers) |
| - | [Dialog & Alerts](#dialog--alerts) |
| - | [Clipboard](#clipboard) |
| - | [Console & Debugging](#console--debugging) |

---

## DOM Selection

```javascript
// Single element
document.getElementById("myId");
document.querySelector(".class");       // first match
document.querySelector("#id");
document.querySelector("div.class");
document.querySelector("[data-id='5']");

// Multiple elements (NodeList)
document.querySelectorAll(".class");
document.querySelectorAll("ul li");
document.getElementsByClassName("class"); // HTMLCollection
document.getElementsByTagName("div");

// Relative selection
element.querySelector(".child");
element.closest(".parent");             // nearest ancestor
element.parentElement;
element.children;                       // direct children
element.nextElementSibling;
element.previousElementSibling;
```

---

## DOM Manipulation

### Creating & Inserting

```javascript
const div = document.createElement("div");
div.textContent = "Hello";
div.innerHTML = "<span>Hello</span>";

parent.appendChild(div);
parent.prepend(div);                    // insert first
parent.append(div, div2);               // insert multiple at end
element.before(newEl);                  // insert before
element.after(newEl);                   // insert after
parent.insertBefore(newEl, refEl);
element.replaceWith(newEl);
```

### Removing

```javascript
element.remove();
parent.removeChild(element);
element.innerHTML = "";                 // clear children
```

### Attributes

```javascript
element.getAttribute("href");
element.setAttribute("href", "/page");
element.removeAttribute("disabled");
element.hasAttribute("disabled");

// Data attributes
element.dataset.userId;                 // data-user-id
element.dataset.userId = "123";

// Common properties
element.id;
element.className;
element.href;
element.src;
element.value;
element.checked;
element.disabled;
```

### Classes

```javascript
element.classList.add("active");
element.classList.remove("active");
element.classList.toggle("active");
element.classList.contains("active");   // true/false
element.classList.replace("old", "new");
element.className = "class1 class2";    // replace all
```

### Styles

```javascript
element.style.color = "red";
element.style.backgroundColor = "blue";
element.style.display = "none";
element.style.cssText = "color: red; font-size: 16px;";

// Get computed style
getComputedStyle(element).color;
```

### Content

```javascript
element.textContent;                    // text only
element.textContent = "New text";
element.innerHTML;                      // HTML content
element.innerHTML = "<b>Bold</b>";
element.outerHTML;                      // includes element itself
```

### Dimensions & Position

```javascript
element.offsetWidth;                    // width + padding + border
element.offsetHeight;
element.clientWidth;                    // width + padding
element.clientHeight;
element.scrollWidth;                    // full scrollable width
element.scrollHeight;

element.getBoundingClientRect();        // {top, left, width, height, ...}
element.offsetTop;                      // relative to offsetParent
element.offsetLeft;
```

---

## Events

### Adding Listeners

```javascript
element.addEventListener("click", (e) => {
    console.log("Clicked", e.target);
});

element.addEventListener("click", handler);
element.removeEventListener("click", handler);

// Once
element.addEventListener("click", handler, {once: true});
```

### Common Events

```javascript
// Mouse
"click", "dblclick", "mousedown", "mouseup", "mousemove"
"mouseenter", "mouseleave", "mouseover", "mouseout"

// Keyboard
"keydown", "keyup", "keypress"

// Form
"submit", "change", "input", "focus", "blur"

// Document
"DOMContentLoaded", "load", "scroll", "resize"
```

### Event Object

```javascript
element.addEventListener("click", (e) => {
    e.target;                           // element that triggered
    e.currentTarget;                    // element with listener
    e.preventDefault();                 // prevent default action
    e.stopPropagation();                // stop bubbling
    e.type;                             // event type
});

// Keyboard events
element.addEventListener("keydown", (e) => {
    e.key;                              // "Enter", "a", "Escape"
    e.code;                             // "KeyA", "Enter"
    e.ctrlKey;                          // true if Ctrl held
    e.shiftKey;
    e.altKey;
    e.metaKey;                          // Cmd on Mac
});

// Mouse events
element.addEventListener("click", (e) => {
    e.clientX;                          // viewport coordinates
    e.clientY;
    e.pageX;                            // document coordinates
    e.pageY;
    e.button;                           // 0=left, 1=middle, 2=right
});
```

### Event Delegation

```javascript
document.querySelector("ul").addEventListener("click", (e) => {
    if (e.target.matches("li")) {
        console.log("Li clicked:", e.target.textContent);
    }
});
```

### Page Load

```javascript
document.addEventListener("DOMContentLoaded", () => {
    // DOM ready
});

window.addEventListener("load", () => {
    // everything loaded (images, etc.)
});
```

---

## Forms

### Accessing Values

```javascript
const form = document.querySelector("form");
const input = document.querySelector("input");

input.value;                            // text input value
input.checked;                          // checkbox/radio
select.value;                           // selected option value
select.selectedIndex;

// FormData
const formData = new FormData(form);
formData.get("fieldName");
formData.getAll("checkboxes");
Object.fromEntries(formData);           // all as object
```

### Form Submission

```javascript
form.addEventListener("submit", (e) => {
    e.preventDefault();
    const data = new FormData(form);
    // process data
});

form.submit();                          // programmatic submit
form.reset();                           // clear form
```

### Validation

```javascript
input.validity.valid;
input.checkValidity();
input.setCustomValidity("Error message");
input.reportValidity();

// Validation properties
input.validity.valueMissing;            // required but empty
input.validity.typeMismatch;            // wrong type (email, url)
input.validity.patternMismatch;         // regex pattern failed
input.validity.tooLong;
input.validity.tooShort;
input.validity.rangeOverflow;           // > max
input.validity.rangeUnderflow;          // < min
```

---

## Storage

### localStorage (persistent)

```javascript
localStorage.setItem("key", "value");
localStorage.getItem("key");            // null if not exists
localStorage.removeItem("key");
localStorage.clear();
localStorage.length;

// Store objects
localStorage.setItem("user", JSON.stringify({name: "Alice"}));
JSON.parse(localStorage.getItem("user"));
```

### sessionStorage (per tab)

```javascript
sessionStorage.setItem("key", "value");
sessionStorage.getItem("key");
sessionStorage.removeItem("key");
sessionStorage.clear();
```

### Cookies

```javascript
// Set
document.cookie = "name=value";
document.cookie = "name=value; expires=Fri, 31 Dec 2025 23:59:59 GMT";
document.cookie = "name=value; max-age=3600";   // 1 hour
document.cookie = "name=value; path=/; secure; samesite=strict";

// Get all
document.cookie;                        // "name=value; other=123"

// Parse
const cookies = Object.fromEntries(
    document.cookie.split("; ").map(c => c.split("="))
);

// Delete
document.cookie = "name=; max-age=0";
```

---

## Fetch API

### GET Request

```javascript
const response = await fetch("/api/data");
const data = await response.json();

// With error handling
try {
    const response = await fetch("/api/data");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
} catch (e) {
    console.error("Fetch failed:", e);
}
```

### POST Request

```javascript
const response = await fetch("/api/data", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({name: "Alice"})
});
const data = await response.json();
```

### Other Methods

```javascript
// PUT
await fetch("/api/item/1", {
    method: "PUT",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({name: "Updated"})
});

// DELETE
await fetch("/api/item/1", {method: "DELETE"});

// Form data
const formData = new FormData();
formData.append("file", fileInput.files[0]);
await fetch("/upload", {method: "POST", body: formData});
```

### Response Handling

```javascript
response.ok;                            // true if 200-299
response.status;                        // 200, 404, etc.
response.statusText;                    // "OK", "Not Found"
response.headers.get("Content-Type");

await response.json();                  // parse JSON
await response.text();                  // raw text
await response.blob();                  // binary data
await response.arrayBuffer();
```

### Abort Request

```javascript
const controller = new AbortController();
setTimeout(() => controller.abort(), 5000);

try {
    const response = await fetch("/api", {signal: controller.signal});
} catch (e) {
    if (e.name === "AbortError") console.log("Request aborted");
}
```

---

## URL & Navigation

### Current URL

```javascript
location.href;                          // full URL
location.protocol;                      // "https:"
location.host;                          // "example.com:8080"
location.hostname;                      // "example.com"
location.port;                          // "8080"
location.pathname;                      // "/path/page"
location.search;                        // "?query=1"
location.hash;                          // "#section"
```

### Navigation

```javascript
location.href = "/new-page";            // navigate (adds history)
location.replace("/new-page");          // navigate (no history)
location.reload();

history.back();
history.forward();
history.go(-2);                         // go back 2 pages
history.pushState({}, "", "/new-url");  // change URL without reload
history.replaceState({}, "", "/new-url");
```

### URL Parsing

```javascript
const url = new URL("https://example.com/path?a=1&b=2");
url.searchParams.get("a");              // "1"
url.searchParams.getAll("a");           // ["1"]
url.searchParams.has("a");              // true
url.searchParams.set("c", "3");
url.searchParams.append("a", "4");
url.searchParams.delete("b");
url.toString();

// Current page params
const params = new URLSearchParams(location.search);
params.get("query");
```

---

## Timers

```javascript
// Delay
const timeoutId = setTimeout(() => {
    console.log("After 1 second");
}, 1000);
clearTimeout(timeoutId);

// Interval
const intervalId = setInterval(() => {
    console.log("Every second");
}, 1000);
clearInterval(intervalId);

// Animation frame
const frameId = requestAnimationFrame((timestamp) => {
    // smooth animation
});
cancelAnimationFrame(frameId);
```

---

## Dialog & Alerts

```javascript
alert("Message");
const confirmed = confirm("Are you sure?");     // true/false
const input = prompt("Enter name:", "default"); // string or null
```

---

## Clipboard

```javascript
// Write
await navigator.clipboard.writeText("Copied text");

// Read
const text = await navigator.clipboard.readText();
```

---

## Console & Debugging

```javascript
console.log("Message");
console.error("Error");
console.warn("Warning");
console.info("Info");
console.table([{a: 1}, {a: 2}]);
console.dir(object);                    // expandable object
console.count("label");                 // count calls
console.time("label");                  // start timer
console.timeEnd("label");               // end timer
console.group("label");                 // group logs
console.groupEnd();
console.clear();

debugger;                               // breakpoint
```

---

[↑ Back to Index](#index)
