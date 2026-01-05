
---

# AWK Scripting

---

## Index

| * | Table of Contents | Quick Reference |
|----|-----|-----|
| - | [Program Structure](#awk-program-structure) | [QR](#quick-reference-structure) |
| - | [Running AWK](#running-awk) | [QR](#quick-reference-running) |
| - | [Command Line Options](#command-line-options) | [QR](#quick-reference-options) |
| - | [Block Types](#block-types) | [QR](#quick-reference-blocks) |
| - | [Printing & Output](#printing--output) | [QR](#print-quick-reference) |
| - | [Standard Variables](#standard-variables-all-awk) | [QR](#quick-reference-variables) |
| - | [Record/Field Counters](#recordfield-counters) | [QR](#quick-reference-field-access) |
| - | [File and Arguments](#file-and-arguments) | [QR](#quick-reference-files) |
| - | [Pattern Matching Results](#pattern-matching-results) | [QR](#quick-reference-pattern-matching) |
| - | [GNU AWK Only](#gnu-awk-gawk-only) | [QR](#quick-reference-gawk) |
| - | [Operators](#operators) | [QR](#quick-reference-operators) |
| - | [Regular Expressions](#regular-expressions) | [QR](#regex-quick-reference) |
| - | [Arrays](#arrays) | [QR](#arrays-quick-reference) |
| - | [Control Flow](#control-flow) | [QR](#control-flow-quick-reference) |
| - | [Built-in Functions](#built-in-functions) | [QR](#built-in-functions-quick-reference) |
| - | [User-Defined Functions](#user-defined-functions) | [QR](#user-defined-functions-quick-reference) |
| - | [Output Redirection](#output-redirection) | [QR](#output-redirection-quick-reference) |



---

## AWK Program Structure

```
BEGIN { ... }    # Runs ONCE before any input is read
      { ... }    # Runs for EACH line/record of input
END   { ... }    # Runs ONCE after all input is processed
```

### Quick Example

```awk
#!/usr/bin/awk -f

BEGIN { 
    print "Starting..." 
    sum = 0 
}

{ 
    sum += $1    # runs for each line
}

END { 
    print "Total:", sum 
}
```

> [!NOTE]
>
> The main block can also have **patterns** to filter which lines it runs on:
> 
> ```awk
> /error/  { print }        # only lines containing "error"
> $3 > 100 { print $1 }     # only if 3rd field > 100
> ```

### Quick Reference: Structure

```awk
BEGIN { }     # once before input
      { }     # each line  
END   { }     # once after input
```

---

## Running AWK

### Two Ways to Run

```bash
# Method 1: Command line
awk [options] 'program' file ...

# Method 2: Script file
awk [options] -f script.awk file ...
```

### Command Line Example

```bash
# Print all lines
awk '{print}' marks.txt

# Print specific fields
awk '{print $1, $3}' marks.txt

# With pattern
awk '/error/ {print}' logfile.txt
```

### Script File Example

```bash
# Create script: command.awk
#!/bin/awk -f
BEGIN { FS = "," }
{ print $1, $2 }

# Run it
awk -f command.awk data.csv

# Or make executable
chmod +x command.awk
./command.awk data.csv
```

### Quick Reference: Running

```bash
awk 'program' file                    # inline
awk -f script.awk file                # from file
awk -F',' '{print $1}' file           # set delimiter
awk -v x=10 '{print x}' file          # pass variable
chmod +x script.awk && ./script.awk   # executable
```

---

## Command Line Options

### Common Options

| Option | Long Form | Description |
|--------|-----------|-------------|
| `-f file` | `--file=file` | Read AWK program from file |
| `-F fs` | `--field-separator=fs` | Set input field separator |
| `-v var=val` | `--assign=var=val` | Assign variable before execution |

```bash
# Set field separator
awk -F',' '{print $1}' data.csv

# Assign variable
awk -v name=Jerry 'BEGIN {print "Name =", name}'

# Combine options
awk -F':' -v threshold=100 '$3 > threshold {print $1}' data.txt
```

### GNU AWK (gawk) Options

| Option | Long Form | Description |
|--------|-----------|-------------|
| `-b` | `--characters-as-bytes` | Treat characters as bytes |
| `-c` | `--traditional` | Disable gawk extensions |
| `-d[file]` | `--dump-variables[=file]` | Dump variables to file (default: `awkvars.out`) |
| `-e 'text'` | `--source='text'` | Specify program text |
| `-E file` | `--exec=file` | Like `-f` but last option processed |
| `-h` | `--help` | Print help message |
| `-L[fatal]` | `--lint[=fatal]` | Warn about dubious constructs |
| `-n` | `--non-decimal-data` | Allow octal/hex input data |
| `-N` | `--use-lc-numeric` | Use locale decimal point |
| `-O` | `--optimize` | Enable optimizations |
| `-p[file]` | `--profile[=file]` | Pretty-print program (default: `awkprof.out`) |
| `-P` | `--posix` | Strict POSIX mode |
| `-S` | `--sandbox` | Disable system commands and redirections |
| `-V` | `--version` | Print version info |

### Option Examples

```bash
# Check version
awk --version

# Dump all variables
awk --dump-variables ''
cat awkvars.out

# Enable lint warnings
awk --lint '{pritn $1}' file.txt   # catches typo

# Lint with fatal warnings (exit on warning)
awk --lint=fatal '{print}' file.txt

# Pretty-print program for debugging
awk --profile 'BEGIN{print "hi"} {print} END{print "bye"}' file.txt
cat awkprof.out

# Strict POSIX mode (no gawk extensions)
awk --posix '{print}' file.txt

# Sandbox mode (safe execution)
awk --sandbox '{print}' file.txt
```

### Quick Reference: Options

| Flag | Purpose |
|------|---------|
| `-F','` | Field separator |
| `-f file` | Program from file |
| `-v var=val` | Set variable |
| `--posix` | POSIX mode |
| `--lint` | Show warnings |
| `--version` | Show version |

---

## Block Types

You can mix and match multiple blocks freely:

```awk
#!/usr/bin/awk -f

BEGIN { FS = "," }

/error/ { print "Found error:", $0 }   # pattern + action

{ count++ }                             # action only (every line)

$3 > 100 { print "Large value:", $3 }  # pattern + action

END { print "Total lines:", count }
```

### All Valid Block Types

| Syntax | When it runs |
|--------|--------------|
| `BEGIN { }` | Once before input |
| `{ }` | Every line |
| `/regex/ { }` | Lines matching regex |
| `expression { }` | Lines where expression is true |
| `pattern1, pattern2 { }` | Range: from pattern1 match until pattern2 match |
| `END { }` | Once after input |

### Multiple Blocks Can Match Same Line

Each line is tested against every pattern. All matching blocks execute in order.

```awk
/apple/ { print "Has apple" }
/red/   { print "Has red" }
        { print "---" }
```

```
# Input:        # Output:
red apple       Has apple
                Has red
                ---
banana          ---
red car         Has red
                ---
```

> [!WARNING]
> Patterns must be at the **top level**, not nested inside braces:
> ```awk
> # WRONG
> {
>     /pattern/ { print }
> }
> 
> # CORRECT
> /pattern/ { print }
> ```

### Quick Reference: Blocks

| Pattern | Matches |
|---------|---------|
| `BEGIN` | Before input |
| `END` | After input |
| `/regex/` | Line matches regex |
| `expression` | Expression is true |
| `pat1,pat2` | Range (inclusive) |
| (empty) | Every line |

---

## Printing & Output

### Sample Data

```
# marks.txt
1) Amit     Physics   80
2) Rahul    Maths     90
3) Shyam    Biology   87
4) Kedar    English   85
5) Hari     History   89
```

### Print Specific Fields

```bash
awk '{print $3 "\t" $4}' marks.txt
```
```
Physics   80
Maths     90
Biology   87
English   85
History   89
```

### Print All Matching Lines

```bash
# These are equivalent
awk '/a/ {print $0}' marks.txt
awk '/a/' marks.txt              # default action is print
```
```
2) Rahul    Maths     90
3) Shyam    Biology   87
4) Kedar    English   85
5) Hari     History   89
```

### Print Fields by Pattern

```bash
awk '/a/ {print $3 "\t" $4}' marks.txt
```
```
Maths    90
Biology  87
English  85
History  89
```

### Print Fields in Any Order

```bash
awk '/a/ {print $4 "\t" $3}' marks.txt
```
```
90   Maths
87   Biology
85   English
89   History
```

### Count Matching Lines

```bash
awk '/a/ {++cnt} END {print "Count =", cnt}' marks.txt
```

> [!NOTE]
> Variables don't need to be declared before use. They default to 0 or empty string.

### Filter by Line Length

```bash
awk 'length($0) > 18' marks.txt
```
```
3) Shyam   Biology   87
4) Kedar   English   85
```

### Formatted Output

```bash
# Basic printf
awk '{printf "%-10s %d\n", $2, $4}' marks.txt
```
```
Amit       80
Rahul      90
Shyam      87
Kedar      85
Hari       89
```

| Format | Description |
|--------|-------------|
| `%s` | String |
| `%d` | Integer |
| `%f` | Float |
| `%.2f` | Float with 2 decimal places |
| `%e` | Scientific notation |
| `%x` | Hexadecimal |
| `%-10s` | Left-align, 10 char width |
| `%10s` | Right-align, 10 char width |

### Print Quick Reference

| Task | Command |
|------|---------|
| Print entire line | `{print}` or `{print $0}` |
| Print specific field | `{print $1}` |
| Print multiple fields | `{print $1, $3}` |
| Print with separator | `{print $1 "\t" $2}` |
| Print literal text | `{print "Name:", $1}` |
| Print line number | `{print NR, $0}` |
| Print matching lines | `/pattern/ {print}` |
| Print field count | `{print NF}` |
| Print last field | `{print $NF}` |

---

## Standard Variables (All AWK)

### Input/Output Separators

| Variable | Default | Description |
|----------|---------|-------------|
| `FS` | space/tab | Input field separator |
| `OFS` | space | Output field separator |
| `RS` | newline | Input record separator |
| `ORS` | newline | Output record separator |

```awk
# Parse CSV, output as tab-separated
BEGIN { FS = ","; OFS = "\t" }
{ print $1, $2, $3 }

# Input:  alice,30,engineer
# Output: alice   30      engineer
```

```awk
# Parse records separated by blank lines
BEGIN { RS = ""; FS = "\n" }
{ print "Record:", NR, "First line:", $1 }

# Input:
# name: alice
# age: 30
#
# name: bob
# age: 25
```

```awk
# Output each record on separate lines with dashes
BEGIN { ORS = "\n---\n" }
{ print $0 }

# Input:
# line1
# line2

# Output:
# line1
# ---
# line2
# ---
```

### Number Formatting

| Variable | Default | Description |
|----------|---------|-------------|
| `OFMT` | `"%.6g"` | Output format for numbers |
| `CONVFMT` | `"%.6g"` | Number to string conversion |

```awk
# Control decimal places in output
BEGIN { OFMT = "%.2f" }
{ print $1 + 0 }

# Input:  3.14159
# Output: 3.14
```

```awk
# Control conversion precision
BEGIN { CONVFMT = "%.2f" }
{ x = 3.14159; str = x ""; print str }

# Output: 3.14
```

### Array Subscript Separator

| Variable | Default | Description |
|----------|---------|-------------|
| `SUBSEP` | `"\034"` | Multi-dimensional array subscript separator |

```awk
# Simulating 2D arrays
BEGIN { SUBSEP = ":" }
{ 
    arr[1,2] = "value"
    for (key in arr) print key 
}

# Output: 1:2
```

### Quick Reference: Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `FS` | space | Input field separator |
| `OFS` | space | Output field separator |
| `RS` | newline | Input record separator |
| `ORS` | newline | Output record separator |
| `OFMT` | `"%.6g"` | Number output format |
| `CONVFMT` | `"%.6g"` | Number conversion format |
| `SUBSEP` | `"\034"` | Array subscript separator |

---

## Record/Field Counters

| Variable | Description |
|----------|-------------|
| `NR` | Total record number (across all files) |
| `FNR` | Record number in current file |
| `NF` | Number of fields in current record |

```awk
# Print line numbers
{ print NR, $0 }

# Input:
# apple
# banana

# Output:
# 1 apple
# 2 banana
```

```awk
# Detect new file
NR != FNR { print "Processing file 2" }
```

```awk
# Print last field
{ print $NF }

# Input:  one two three
# Output: three
```

```awk
# Print second-to-last field
{ print $(NF-1) }

# Input:  one two three
# Output: two
```

### Quick Reference: Field Access

```awk
$0          # entire line
$1          # first field
$NF         # last field
$(NF-1)     # second-to-last field
$NF = "x"   # modify last field
NF = 3      # truncate to 3 fields
NR          # line number (total)
FNR         # line number (current file)
NF          # number of fields
```

---

## File and Arguments

| Variable | Description |
|----------|-------------|
| `FILENAME` | Current input filename |
| `ARGC` | Number of command-line arguments |
| `ARGV` | Array of command-line arguments |
| `ENVIRON` | Array of environment variables |

```awk
# Print filename with each line
{ print FILENAME, $0 }
```

```awk
# Access command-line arguments
BEGIN {
    print "Argument count:", ARGC
    for (i = 0; i < ARGC; i++)
        print "ARGV[" i "]:", ARGV[i]
}

# Run: awk -f script.awk file1.txt file2.txt
# Output:
# Argument count: 3
# ARGV[0]: awk
# ARGV[1]: file1.txt
# ARGV[2]: file2.txt
```

```awk
# Access environment variables
BEGIN { print ENVIRON["HOME"] }

# Output: /home/username
```

### Quick Reference: Files

```awk
FILENAME          # current filename
ARGC              # argument count
ARGV[0]           # "awk"
ARGV[1]           # first file
ENVIRON["HOME"]   # environment variable
ENVIRON["USER"]   # username
ENVIRON["PATH"]   # path
```

---

## Pattern Matching Results

| Variable | Description |
|----------|-------------|
| `RSTART` | Start position of match from `match()` |
| `RLENGTH` | Length of match from `match()` |

```awk
# Extract matched substring
{
    if (match($0, /[0-9]+/)) {
        print "Found:", substr($0, RSTART, RLENGTH)
        print "Position:", RSTART
        print "Length:", RLENGTH
    }
}

# Input:  abc123def
# Output:
# Found: 123
# Position: 4
# Length: 3
```

### Quick Reference: Pattern Matching

```awk
match($0, /regex/)              # find position
RSTART                          # start position (0 if no match)
RLENGTH                         # match length (-1 if no match)
substr($0, RSTART, RLENGTH)     # extract match
```

---

## GNU AWK (gawk) Only

| Variable | Description |
|----------|-------------|
| `IGNORECASE` | Case-insensitive matching |
| `FPAT` | Field pattern (regex defining field content) |
| `FIELDWIDTHS` | Fixed-width field specification |
| `BINMODE` | Binary mode for files |
| `LINT` | Enable lint warnings |
| `PREC` | Arbitrary precision (default 53) |
| `ROUNDMODE` | Rounding mode for arithmetic |

```awk
# Case-insensitive matching
BEGIN { IGNORECASE = 1 }
/error/ { print }

# Matches: ERROR, Error, error, etc.
```

```awk
# Parse CSV with quoted fields containing commas
BEGIN { FPAT = "([^,]+)|(\"[^\"]+\")" }
{ print $2 }

# Input:  john,"doe, jr",30
# Output: "doe, jr"
```

```awk
# Fixed-width fields
BEGIN { FIELDWIDTHS = "5 3 8" }
{ print $1, $2, $3 }

# Input:  abcde123XYZwhatever
# Output: abcde 123 XYZwhate
```

```awk
# Enable lint warnings
BEGIN { LINT = 1 }
{ x = 1; if (x = 2) print "oops" }

# Warns about assignment in condition
```

### Quick Reference: gawk

| Variable | Description |
|----------|-------------|
| `IGNORECASE = 1` | Case-insensitive matching |
| `FPAT = "pattern"` | Define field by pattern |
| `FIELDWIDTHS = "5 3 8"` | Fixed-width fields |
| `BINMODE = 1` | Binary mode |
| `LINT = 1` | Enable warnings |

---

## Operators

| * | Operators | Description |
|-|-|-|
| - | Arithmetic Operators | `+` `-` `*` `/` `%` (modulo) |
| - | Increment & Decrement Operators | `++x` `x++` `--x` `x--` |
| - | Assignment Operators | `=` `+=` `-=` `*=` `/=` `%=` `^=` |
| - | Relational Operators | `==` `!=` `<` `>` `<=` `>=` |
| - | Logical Operators | `&&` (AND) `\|\|` (OR) `!` (NOT) |
| - | Ternary Operator | `condition ? if_true : if_false` |
| - | Unary Operators | `+` (positive) `-` (negative) `!` (NOT) |
| - | Exponential Operators | `^` or `**` |
| - | String Concatenation Operator | `"hello" "world"` (space between) |
| - | Array Membership Operator | `(key in array)` |
| - | Regular Expression Operators | `~` (match) `!~` (not match) |


### Quick Reference: Operators

| Type | Operators |
|------|-----------|
| Arithmetic | `+` `-` `*` `/` `%` `^` |
| Assignment | `=` `+=` `-=` `*=` `/=` `%=` `^=` |
| Comparison | `==` `!=` `<` `>` `<=` `>=` |
| Logical | `&&` `\|\|` `!` |
| Regex | `~` `!~` |
| Ternary | `cond ? yes : no` |
| Increment | `++x` `x++` `--x` `x--` |
| String | `"a" "b"` (concatenate) |
| Array | `key in arr` |


---

## Regular Expressions

---

## Regex Quick Navigation

| # | Section | Description |
|---|---------|-------------|
| 1 | [Anchors](#anchors) | `^` `$` start/end of string |
| 2 | [Quantifiers](#quantifiers) | `*` `+` `?` `{n}` repetition |
| 3 | [Character Classes](#character-classes) | `[abc]` `[^abc]` `[a-z]` |
| 4 | [POSIX Character Classes](#posix-character-classes) | `[[:digit:]]` `[[:alpha:]]` etc. |
| 5 | [Dot (Any Character)](#dot-any-character) | `.` matches any char |
| 6 | [Alternation (OR)](#alternation-or) | `\|` match this or that |
| 7 | [Grouping](#grouping) | `()` group patterns |
| 8 | [Escape Sequences](#escape-sequences) | `\t` `\n` `\\` |
| 9 | [Escaping Special Characters](#escaping-special-characters) | `\.` `\$` `\*` |
| 10 | [Negation](#negation) | `[^...]` `!~` |
| 11 | [Word Boundaries (gawk)](#word-boundaries-gawk) | `\<` `\>` `\y` |
| 12 | [Case Sensitivity](#case-sensitivity) | `IGNORECASE` |
| 13 | [Greedy Matching](#greedy-matching) | Longest match behavior |
| 14 | [Dynamic Regex](#dynamic-regex) | Patterns from variables |
| 15 | [Regex Operators](#regex-operators) | `~` `!~` comparison |
| 16 | [Regex Functions](#regex-functions) | `sub` `gsub` `match` `split` |
| 17 | [gensub() (gawk)](#gensub-gawk-only) | Advanced replacement |
| 18 | [patsplit() (gawk)](#patsplit-gawk-only) | Split by pattern |
| 19 | [Common Patterns](#common-real-world-patterns) | Email, IP, phone, etc. |

---

## Anchors

```awk
# ^ = start of string
# $ = end of string

# Field value: "hello world"
/^hello/    ✓  # Matches: starts with "hello"
/^world/    ✗  # NO match: doesn't start with "world"
/world$/    ✓  # Matches: ends with "world"
/hello$/    ✗  # NO match: doesn't end with "hello"
/^hello$/   ✗  # NO match: not EXACTLY "hello"

# Field value: "hello"
/^hello$/   ✓  # Matches: exactly "hello", nothing else
```

| Pattern | Meaning |
|---------|---------|
| `^abc` | Starts with "abc" |
| `abc$` | Ends with "abc" |
| `^abc$` | Exactly "abc" |
| `^$` | Empty string |
| `^.+$` | Non-empty string |

---

## Quantifiers

```awk
# * = zero or more
# + = one or more
# ? = zero or one (optional)
# {n} = exactly n times
# {n,} = n or more times
# {n,m} = between n and m times

# Field value: "ac"
/ab*c/      ✓  # Matches: zero b's is OK
/ab+c/      ✗  # NO match: needs at least one b
/ab?c/      ✓  # Matches: zero or one b

# Field value: "abc"
/ab*c/      ✓  # Matches: one b
/ab+c/      ✓  # Matches: one b
/ab?c/      ✓  # Matches: one b

# Field value: "abbc"
/ab*c/      ✓  # Matches: two b's
/ab+c/      ✓  # Matches: two b's
/ab?c/      ✗  # NO match: more than one b

# Field value: "abbbc"
/ab{3}c/    ✓  # Matches: exactly 3 b's
/ab{2}c/    ✗  # NO match: has 3 b's, not 2
/ab{2,}c/   ✓  # Matches: 2 or more b's
/ab{2,4}c/  ✓  # Matches: between 2 and 4 b's

# Field value: "abbbbbbc"
/ab{2,4}c/  ✗  # NO match: has 6 b's (more than 4)
```

| Quantifier | Meaning | Example |
|------------|---------|---------|
| `*` | Zero or more | `ab*c` → ac, abc, abbc |
| `+` | One or more | `ab+c` → abc, abbc |
| `?` | Zero or one | `ab?c` → ac, abc |
| `{3}` | Exactly 3 | `ab{3}c` → abbbc |
| `{2,}` | 2 or more | `ab{2,}c` → abbc, abbbc... |
| `{2,4}` | 2 to 4 | `ab{2,4}c` → abbc, abbbc, abbbbc |

---

## Character Classes

```awk
# [abc] = any one character in the set
# [^abc] = any one character NOT in the set
# [a-z] = any character in the range

# Field value: "cat"
/[cb]at/    ✓  # Matches: 'c' is in the set [cb]
/[xy]at/    ✗  # NO match: 'c' is not in [xy]
/[a-m]at/   ✓  # Matches: 'c' is in range a-m
/[n-z]at/   ✗  # NO match: 'c' is not in range n-z

# Field value: "bat"
/[^cb]at/   ✗  # NO match: 'b' IS in the excluded set
/[^xy]at/   ✓  # Matches: 'b' is NOT in [xy]

# Field value: "test123"
/[0-9]/     ✓  # Matches: contains digits
/^[a-z]+$/  ✗  # NO match: has digits
/^[a-z0-9]+$/ ✓  # Matches: only letters and digits

# Field value: "Test"
/[a-z]/     ✓  # Matches: has lowercase letters
/^[a-z]+$/  ✗  # NO match: has uppercase 'T'
/[A-Z]/     ✓  # Matches: has uppercase letter
```

| Pattern | Meaning |
|---------|---------|
| `[abc]` | a, b, or c |
| `[^abc]` | NOT a, b, or c |
| `[a-z]` | Lowercase letter |
| `[A-Z]` | Uppercase letter |
| `[0-9]` | Digit |
| `[a-zA-Z]` | Any letter |
| `[a-zA-Z0-9]` | Alphanumeric |

---

## POSIX Character Classes

```awk
# Field value: "Hello123"
/[[:digit:]]/     ✓  # Matches: contains digits
/[[:alpha:]]/     ✓  # Matches: contains letters
/^[[:alnum:]]+$/  ✓  # Matches: only letters and numbers
/^[[:lower:]]+$/  ✗  # NO match: has uppercase 'H'

# Field value: "hello world"
/[[:space:]]/     ✓  # Matches: contains space
/^[[:lower:]]+$/  ✗  # NO match: has a space

# Field value: "Hello, World!"
/[[:punct:]]/     ✓  # Matches: has comma and exclamation

# Field value: "abc123"
/^[[:xdigit:]]+$/ ✓  # Matches: all valid hex chars
```

| Class | Equivalent | Description |
|-------|------------|-------------|
| `[[:digit:]]` | `[0-9]` | Digits |
| `[[:alpha:]]` | `[a-zA-Z]` | Letters |
| `[[:alnum:]]` | `[a-zA-Z0-9]` | Letters and digits |
| `[[:space:]]` | `[ \t\n\r\f\v]` | All whitespace |
| `[[:blank:]]` | `[ \t]` | Space and tab only |
| `[[:upper:]]` | `[A-Z]` | Uppercase letters |
| `[[:lower:]]` | `[a-z]` | Lowercase letters |
| `[[:punct:]]` | | Punctuation |
| `[[:print:]]` | | Printable (with space) |
| `[[:graph:]]` | | Visible (no space) |
| `[[:cntrl:]]` | | Control characters |
| `[[:xdigit:]]` | `[0-9A-Fa-f]` | Hex digits |

---

## Dot (Any Character)

```awk
# . = any single character (except newline)

# Field value: "cat"
/c.t/       ✓  # Matches: 'a' is any character
/c..t/      ✗  # NO match: only one char between c and t

# Field value: "c@t"
/c.t/       ✓  # Matches: '@' is any character

# Field value: "ct"
/c.t/       ✗  # NO match: needs exactly one char between

# Field value: "cat in hat"
/c.t/       ✓  # Matches: finds "cat"
/.at/       ✓  # Matches: 'c' or 'h' before "at"
```

| Pattern | Meaning |
|---------|---------|
| `.` | Any single character |
| `.*` | Any number of any characters |
| `.+` | One or more of any character |
| `.?` | Zero or one of any character |

---

## Alternation (OR)

```awk
# | = OR (match this OR that)
# Note: use \| in some awk versions, | in gawk

# Field value: "cat"
/(cat|dog)/    ✓  # Matches: is "cat"
/(dog|bird)/   ✗  # NO match: not "dog" or "bird"

# Field value: "I have a cat"
/(cat|dog)/    ✓  # Matches: contains "cat"

# Field value: "error"
/(error|warning|info)/ ✓  # Matches: is "error"

# Field value: "debug"
/(error|warning|info)/ ✗  # NO match: not in the list
```

---

## Grouping

```awk
# () = group patterns together

# Field value: "ababab"
/(ab)+/     ✓  # Matches: "ab" repeated
/(ab){3}/   ✓  # Matches: "ab" exactly 3 times
/(ab){4}/   ✗  # NO match: only 3 repetitions

# Field value: "abcabc"
/(abc)+/    ✓  # Matches: "abc" repeated

# Field value: "catdog"
/(cat|dog)+/ ✓  # Matches: contains "cat" or "dog"
```

---

## Escape Sequences

```awk
# Special escape sequences in regex
\t      # Tab
\n      # Newline
\r      # Carriage return
\b      # Backspace
\f      # Form feed
\\      # Literal backslash

# Field value: "hello	world" (tab between)
/\t/        ✓  # Matches: contains tab

# Field value: "path\\to\\file"
/\\/        ✓  # Matches: contains backslash
```

| Escape | Meaning |
|--------|---------|
| `\t` | Tab |
| `\n` | Newline |
| `\r` | Carriage return |
| `\b` | Backspace |
| `\f` | Form feed |
| `\\` | Literal backslash |

---

## Escaping Special Characters

```awk
# Use \ to match literal special characters
# Special chars: . * + ? [ ] ( ) { } ^ $ | \

# Field value: "test.txt"
/\./        ✓  # Matches: literal dot
/\.txt$/    ✓  # Matches: ends with ".txt"

# Field value: "price: $50"
/\$/        ✓  # Matches: literal dollar sign

# Field value: "2+2=4"
/\+/        ✓  # Matches: literal plus sign
/+/         ✗  # ERROR: + needs something before it

# Field value: "question?"
/\?/        ✓  # Matches: literal question mark

# Field value: "array[5]"
/\[/        ✓  # Matches: literal [
/\[5\]/     ✓  # Matches: literal [5]
```

| Character | Escaped |
|-----------|---------|
| `.` | `\.` |
| `*` | `\*` |
| `+` | `\+` |
| `?` | `\?` |
| `[` | `\[` |
| `]` | `\]` |
| `(` | `\(` |
| `)` | `\)` |
| `{` | `\{` |
| `}` | `\}` |
| `^` | `\^` |
| `$` | `\$` |
| `\|` | `\\\|` |
| `\` | `\\` |

---

## Negation

```awk
# [^...] = NOT any of these characters
# !~ = does NOT match

# Field value: "hello"
/[^0-9]/    ✓  # Matches: has non-digit characters
/^[^0-9]+$/ ✓  # Matches: entire field has no digits

# Field value: "hello123"
/^[^0-9]+$/ ✗  # NO match: has digits

# Using !~ operator:
$1 !~ /[0-9]/  # True if field 1 does NOT contain digits
```

---

## Word Boundaries (gawk)

```awk
# \< = start of word
# \> = end of word
# \y = word boundary (either side)

# Field value: "the cat in the hat"
/\<cat\>/   ✓  # Matches: "cat" as whole word
/\<hat\>/   ✓  # Matches: "hat" as whole word
/\<ca\>/    ✗  # NO match: "ca" is not a whole word

# Field value: "category"
/\<cat\>/   ✗  # NO match: "cat" is part of word
/cat/       ✓  # Matches: "cat" substring exists
```

| Boundary | Meaning |
|----------|---------|
| `\<` | Start of word |
| `\>` | End of word |
| `\y` | Either boundary |
| `\<word\>` | Whole word only |

---

## Case Sensitivity

```awk
# Default: case sensitive
# Set IGNORECASE=1 for case insensitive

# Field value: "Hello"
/hello/     ✗  # NO match: case sensitive
/Hello/     ✓  # Matches: exact case

# With IGNORECASE=1:
BEGIN { IGNORECASE=1 }
/hello/     ✓  # Matches: case insensitive
/HELLO/     ✓  # Matches: case insensitive

# Or use character classes:
/[Hh]ello/  ✓  # Matches: "Hello" or "hello"
```

---

## Greedy Matching

```awk
# AWK regex is ALWAYS greedy (matches longest possible)
# No non-greedy quantifiers like *? or +?

# Field value: "<b>bold</b> and <i>italic</i>"
match($0, /<.*>/)
# Matches: "<b>bold</b> and <i>italic</i>" (entire string!)
# NOT just "<b>"

# Workaround: use negated character class
match($0, /<[^>]*>/)
# Matches: "<b>" (first tag only)

# Field value: "aaaaab"
/a+/        # Matches: "aaaaa" (all a's, greedy)
```

| Greedy | Non-greedy Workaround |
|--------|----------------------|
| `.*` | `[^X]*` (stop at X) |
| `.+` | `[^X]+` (stop at X) |
| `<.*>` | `<[^>]*>` |
| `".*"` | `"[^"]*"` |

---

## Dynamic Regex

```awk
# Static regex (literal)
/error/ { print }

# Dynamic regex (from variable)
BEGIN { pattern = "error" }
$0 ~ pattern { print }

# Dynamic regex from field
$1 ~ $2 { print "Field 1 matches pattern in field 2" }

# Building regex dynamically
BEGIN { ext = "txt" }
$0 ~ ("\\." ext "$") { print "Text file:", $0 }
```

---

## Regex Operators

```awk
# Comparison operators
$0 ~ /regex/     # Line matches regex
$0 !~ /regex/    # Line does NOT match regex
$1 ~ /regex/     # Field 1 matches regex

# In conditions
if ($0 ~ /error/) print "found"

# Pattern-action
/regex/ { action }           # Implicit: $0 ~ /regex/
$2 ~ /regex/ { action }      # Explicit field match
```

| Operator | Meaning |
|----------|---------|
| `~` | Matches |
| `!~` | Does not match |
| `/regex/` | Shorthand for `$0 ~ /regex/` |

---

## Regex Functions

```awk
# sub(regex, replacement, [target])
# Replace first match (modifies in place)
# Returns: number of replacements (0 or 1)

# Field value: "hello world"
sub(/world/, "AWK")      # Result: "hello AWK"
sub(/o/, "0")            # Result: "hell0 world"
sub(/o/, "0", $2)        # Replace in field 2 only

# gsub(regex, replacement, [target])
# Replace ALL matches (modifies in place)
# Returns: number of replacements

# Field value: "hello world"
gsub(/o/, "0")           # Result: "hell0 w0rld", returns 2
gsub(/[aeiou]/, "*")     # Result: "h*ll* w*rld"

# match(string, regex)
# Find position of match
# Sets RSTART and RLENGTH

# Field value: "hello world"
match($0, /world/)       # Returns: 7, RSTART=7, RLENGTH=5
match($0, /xyz/)         # Returns: 0 (not found)

# Extract matched text
if (match($0, /[0-9]+/)) {
    print substr($0, RSTART, RLENGTH)
}

# split(string, array, regex)
# Split string into array by regex

# Field value: "a:b::c"
n = split($0, arr, /:+/) # Split on one or more colons
                         # arr[1]="a", arr[2]="b", arr[3]="c"
                         # n=3
```

| Function | Purpose | Returns |
|----------|---------|---------|
| `sub(r,s)` | Replace first match | 0 or 1 |
| `gsub(r,s)` | Replace all matches | Count |
| `match(str,r)` | Find position | Position (0 if none) |
| `split(str,arr,r)` | Split by regex | Number of elements |

---

## gensub() (gawk Only)

```awk
# Syntax: gensub(regex, replacement, how, [target])
# Returns new string (doesn't modify original)
# Supports backreferences: \1 \2 etc.

# Field value: "hello world"
gensub(/world/, "AWK", "g")        # "hello AWK"
gensub(/o/, "0", 1)                # "hell0 world" (first only)
gensub(/o/, "0", 2)                # "hello w0rld" (second only)
gensub(/o/, "0", "g")              # "hell0 w0rld" (all)

# Backreferences
# Field value: "hello world"
gensub(/(\w+) (\w+)/, "\\2 \\1", "g")  # "world hello"

# Field value: "2024-01-15"
gensub(/([0-9]+)-([0-9]+)-([0-9]+)/, "\\2/\\3/\\1", "g")
# Result: "01/15/2024"

# Field value: "John Smith"
gensub(/(.+) (.+)/, "Last: \\2, First: \\1", 1)
# Result: "Last: Smith, First: John"
```

| Parameter | Meaning |
|-----------|---------|
| `"g"` | Replace all |
| `1` | Replace first |
| `2` | Replace second |
| `n` | Replace nth |
| `\\1` | First capture group |
| `\\2` | Second capture group |

---

## patsplit() (gawk Only)

```awk
# Syntax: patsplit(string, array, pattern [, separators])
# Split by pattern matches (extract matches)

# Field value: "abc123def456ghi"
n = patsplit($0, nums, /[0-9]+/)
# nums[1]="123", nums[2]="456", n=2

# Extract all words
n = patsplit($0, words, /[a-z]+/)
# words[1]="abc", words[2]="def", words[3]="ghi"

# Extract all email addresses
patsplit($0, emails, /[^[:space:]]+@[^[:space:]]+/)
```

---

## Common Real-World Patterns

```awk
# Email (simplified)
/^[^@]+@[^@]+\.[a-z]+$/

# IP Address
/^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/

# Phone XXX-XXX-XXXX
/^[0-9]{3}-[0-9]{3}-[0-9]{4}$/

# Date YYYY-MM-DD
/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/

# URL
/^https?:\/\//

# Blank line
/^[[:space:]]*$/

# Non-blank line
/[^[:space:]]/

# Starts with # (comment)
/^[[:space:]]*#/

# Numeric (integer)
/^-?[0-9]+$/

# Numeric (decimal)
/^-?[0-9]*\.?[0-9]+$/

# Hex number
/^0x[0-9A-Fa-f]+$/

# MAC address
/^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$/
```

| Pattern | Validates |
|---------|-----------|
| `/^[^@]+@[^@]+\.[a-z]+$/` | Email |
| `/^[0-9]{1,3}(\.[0-9]{1,3}){3}$/` | IP address |
| `/^[0-9]{3}-[0-9]{3}-[0-9]{4}$/` | Phone |
| `/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/` | Date YYYY-MM-DD |
| `/^https?:\/\//` | URL |
| `/^-?[0-9]+$/` | Integer |
| `/^-?[0-9]*\.?[0-9]+$/` | Decimal |
| `/^[[:space:]]*$/` | Blank line |
| `/^#/` | Comment line |

---

## Complete Example Script

```awk
#!/usr/bin/awk -f
BEGIN { FS="," }

# Only numeric IDs
$1 ~ /^[0-9]+$/ { print "Valid ID:", $1 }

# Valid email in column 3
$3 ~ /^[^@]+@[^@]+\.[a-z]+$/ { print "Email:", $3 }

# Lines NOT starting with # or empty
!/^#/ && !/^$/ { print }

# Phone numbers in XXX-XXX-XXXX format
$2 ~ /^[0-9]{3}-[0-9]{3}-[0-9]{4}$/ { print "Phone:", $2 }

# Find errors or warnings (case insensitive)
BEGIN { IGNORECASE=1 }
/(error|warning)/ { print "Alert:", $0 }

# Extract numbers
match($0, /[0-9]+/) { print "Found number at position:", RSTART }

# Replace all vowels with *
{ gsub(/[aeiou]/, "*"); print }
```

---

## Regex Quick Reference

### Anchors & Boundaries

| Pattern | Meaning |
|---------|---------|
| `^` | Start of string |
| `$` | End of string |
| `\<` | Start of word (gawk) |
| `\>` | End of word (gawk) |
| `\y` | Word boundary (gawk) |


### Quantifiers

| Pattern | Meaning |
|---------|---------|
| `*` | Zero or more |
| `+` | One or more |
| `?` | Zero or one |
| `{n}` | Exactly n |
| `{n,}` | n or more |
| `{n,m}` | n to m |


### Character Classes

| Pattern | Meaning |
|---------|---------|
| `.` | Any character |
| `[abc]` | a, b, or c |
| `[^abc]` | NOT a, b, c |
| `[a-z]` | Range a-z |
| `[0-9]` | Digit |
| `[a-zA-Z]` | Any letter |
| `[a-zA-Z0-9]` | Alphanumeric |


### POSIX Classes

| Class | Meaning |
|-------|---------|
| `[[:digit:]]` | `[0-9]` |
| `[[:alpha:]]` | `[a-zA-Z]` |
| `[[:alnum:]]` | `[a-zA-Z0-9]` |
| `[[:space:]]` | All whitespace |
| `[[:blank:]]` | Space and tab |
| `[[:upper:]]` | `[A-Z]` |
| `[[:lower:]]` | `[a-z]` |
| `[[:punct:]]` | Punctuation |
| `[[:xdigit:]]` | `[0-9A-Fa-f]` |
| `[[:print:]]` | Printable |
| `[[:graph:]]` | Visible (no space) |
| `[[:cntrl:]]` | Control chars |


### Escape Sequences

| Pattern | Meaning |
|---------|---------|
| `\.` | Literal dot |
| `\*` | Literal asterisk |
| `\+` | Literal plus |
| `\?` | Literal question |
| `\[` `\]` | Literal brackets |
| `\(` `\)` | Literal parens |
| `\{` `\}` | Literal braces |
| `\^` | Literal caret |
| `\$` | Literal dollar |
| `\\` | Literal backslash |
| `\t` | Tab |
| `\n` | Newline |
| `\r` | Carriage return |
| `\b` | Backspace |
| `\f` | Form feed |


### Operators & Syntax

```awk
/regex/           # line matches
!/regex/          # line doesn't match
$1 ~ /regex/      # field matches
$1 !~ /regex/     # field doesn't match
(a|b)             # alternation (OR)
()                # grouping
```

### Case Sensitivity

```awk
# Default: case sensitive
/hello/                      # only lowercase

# Case insensitive (gawk)
BEGIN { IGNORECASE = 1 }
/hello/                      # matches Hello, HELLO, etc.

# Manual case insensitive
/[Hh][Ee][Ll][Ll][Oo]/       # any case
```

### Dynamic Regex

```awk
# Pattern from variable
BEGIN { pat = "error" }
$0 ~ pat { print }

# Building pattern
BEGIN { ext = "txt" }
$0 ~ ("\\." ext "$") { print }

# Pattern from field
$1 ~ $2 { print }
```

### Greedy Matching

```awk
# AWK is always greedy (longest match)
/<.*>/        # matches entire "<b>x</b>"

# Workaround: negated class
/<[^>]*>/     # matches "<b>" only
/"[^"]*"/     # matches first quoted string
```

### Functions

| Function | Purpose | Returns |
|----------|---------|---------|
| `sub(/re/, "new")` | Replace first | 0 or 1 |
| `sub(/re/, "new", target)` | Replace in target | 0 or 1 |
| `gsub(/re/, "new")` | Replace all | Count |
| `gsub(/re/, "new", target)` | Replace all in target | Count |
| `match(str, /re/)` | Find position | Position (0=none) |
| `split(str, arr, /re/)` | Split by regex | Element count |


```awk
# match() sets RSTART and RLENGTH
if (match($0, /[0-9]+/)) {
    print substr($0, RSTART, RLENGTH)
}
```

### gawk Functions

```awk
# gensub(regex, replacement, how, [target])
# Returns new string (doesn't modify original)

gensub(/o/, "0", "g")           # replace all
gensub(/o/, "0", 1)             # replace first
gensub(/o/, "0", 2)             # replace second

# Backreferences
gensub(/(.+) (.+)/, "\\2 \\1", 1)   # swap words

# patsplit(string, array, pattern)
# Extract all matches into array

patsplit("ab12cd34", nums, /[0-9]+/)
# nums[1]="12", nums[2]="34"

patsplit($0, emails, /[^[:space:]]+@[^[:space:]]+/)
```

### Common Patterns

| Pattern | Validates |
|---------|-----------|
| `/^$/` | Empty line |
| `/^[[:space:]]*$/` | Blank line |
| `/[^[:space:]]/` | Non-blank line |
| `/^#/` | Comment line |
| `/^[0-9]+$/` | Integer |
| `/^-?[0-9]+$/` | Signed integer |
| `/^[0-9]*\.?[0-9]+$/` | Decimal |
| `/^-?[0-9]*\.?[0-9]+$/` | Signed decimal |
| `/^0x[0-9A-Fa-f]+$/` | Hex number |
| `/^[^@]+@[^@]+\.[a-z]+$/` | Email (simple) |
| `/^[0-9]{3}-[0-9]{4}$/` | Phone XXX-XXXX |
| `/^[0-9]{3}-[0-9]{3}-[0-9]{4}$/` | Phone XXX-XXX-XXXX |
| `/^[0-9]{1,3}(\.[0-9]{1,3}){3}$/` | IP address |
| `/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/` | Date YYYY-MM-DD |
| `/^https?:\/\//` | URL |
| `/^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$/` | MAC address |


---

[↑ Back to Regex Navigation](#regex-quick-navigation)

---

## Arrays

---

## Arrays Quick Navigation

| # | Section | Description |
|---|---------|-------------|
| 1 | [Array Basics](#array-basics) | Creating, accessing, assigning |
| 2 | [Deleting Elements](#deleting-array-elements) | `delete` statement |
| 3 | [Checking Membership](#checking-array-membership) | `in` operator |
| 4 | [Iterating Arrays](#iterating-over-arrays) | `for (key in array)` |
| 5 | [Array Length](#array-length) | Counting elements |
| 6 | [Multi-Dimensional Arrays](#multi-dimensional-arrays) | Simulating 2D arrays |
| 7 | [SUBSEP](#subsep) | Multi-index separator |
| 8 | [Array Functions (gawk)](#array-functions-gawk) | `asort`, `asorti`, `delete` |
| 9 | [Common Array Patterns](#common-array-patterns) | Real-world examples |

---

## Array Basics

```awk
# Syntax
array_name[index] = value

# Arrays are associative (like dictionaries/hash maps)
# - No declaration needed
# - No size limit
# - Index can be string or number
# - Indexes need not be continuous
```

### Creating and Accessing

```awk
BEGIN {
    # String indexes
    fruits["mango"] = "yellow"
    fruits["orange"] = "orange"
    fruits["apple"] = "red"

    # Numeric indexes
    numbers[1] = "one"
    numbers[2] = "two"
    numbers[100] = "hundred"  # gaps are OK

    # Access elements
    print fruits["mango"]     # yellow
    print numbers[1]          # one
}
```

### Uninitialized Elements

```awk
BEGIN {
    # Accessing non-existent element returns empty string
    print arr["missing"]      # prints empty string
    print arr["missing"] + 0  # prints 0 (numeric context)

    # This also CREATES the element!
    # Be careful when checking existence
}
```

| Operation | Syntax | Notes |
|-----------|--------|-------|
| Create/Assign | `arr[key] = value` | Creates if doesn't exist |
| Access | `arr[key]` | Returns "" if missing |
| Numeric access | `arr[key] + 0` | Returns 0 if missing |

---

## Deleting Array Elements

```awk
# Syntax
delete array_name[index]

# Delete entire array (gawk)
delete array_name
```

### Examples

```awk
BEGIN {
    fruits["mango"] = "yellow"
    fruits["orange"] = "orange"
    fruits["apple"] = "red"

    # Delete single element
    delete fruits["orange"]

    print fruits["orange"]    # prints empty string

    # Delete entire array (gawk)
    delete fruits
}
```

```awk
# Delete elements matching condition
{
    for (key in arr) {
        if (arr[key] < 10) {
            delete arr[key]
        }
    }
}
```

---

## Checking Array Membership

```awk
# Syntax: (index in array)
# Returns 1 (true) if exists, 0 (false) if not
# Does NOT create the element (unlike direct access)

BEGIN {
    fruits["mango"] = "yellow"
    fruits["apple"] = "red"

    # Check if key exists
    if ("mango" in fruits) {
        print "mango exists"
    }

    if ("banana" in fruits) {
        print "banana exists"
    } else {
        print "no banana"       # this prints
    }
}
```

### Safe Access Pattern

```awk
# Wrong: creates element if missing
if (arr[key] != "") { ... }

# Right: check first, then access
if (key in arr) {
    print arr[key]
}
```

| Method | Creates Element? | Use Case |
|--------|-----------------|----------|
| `arr[key]` | Yes | When you want the value |
| `(key in arr)` | No | When checking existence |

---

## Iterating Over Arrays

```awk
# Syntax
for (variable in array) {
    # variable contains the INDEX, not value
    # use array[variable] to get value
}
```

### Examples

```awk
BEGIN {
    fruits["mango"] = "yellow"
    fruits["orange"] = "orange"
    fruits["apple"] = "red"

    # Iterate over all elements
    for (fruit in fruits) {
        print fruit, "is", fruits[fruit]
    }
}

# Output (order not guaranteed):
# mango is yellow
# orange is orange
# apple is red
```

```awk
# Count word frequency
{
    for (i = 1; i <= NF; i++) {
        words[$i]++
    }
}
END {
    for (word in words) {
        print word, words[word]
    }
}
```

> [!WARNING]
> Array iteration order is **not guaranteed**. Don't rely on any specific order.

---

## Array Length

```awk
# Method 1: length() function (gawk and modern awk)
BEGIN {
    arr[1] = "a"
    arr[2] = "b"
    arr[5] = "c"

    print length(arr)    # 3 (counts elements, not max index)
}

# Method 2: Manual count (portable)
BEGIN {
    count = 0
    for (key in arr) {
        count++
    }
    print count
}
```

---

## Multi-Dimensional Arrays

AWK only supports one-dimensional arrays, but you can simulate multi-dimensional:

### Method 1: String Index

```awk
BEGIN {
    # Simulating 3x3 array
    # array[row,col] = value

    array["0,0"] = 100; array["0,1"] = 200; array["0,2"] = 300
    array["1,0"] = 400; array["1,1"] = 500; array["1,2"] = 600
    array["2,0"] = 700; array["2,1"] = 800; array["2,2"] = 900

    # Access
    print array["1,1"]    # 500

    # Iterate
    for (key in array) {
        print key, "=", array[key]
    }
}
```

### Method 2: Using SUBSEP (Preferred)

```awk
BEGIN {
    # AWK automatically joins indexes with SUBSEP
    array[0,0] = 100    # actually stored as array["0" SUBSEP "0"]
    array[0,1] = 200
    array[1,0] = 400
    array[1,1] = 500
    
    # Access
    print array[1,1]      # 500
    
    # Check membership
    if ((1,1) in array) {
        print "exists"
    }
}
```

| Syntax | Stored As |
|--------|-----------|
| `arr["0,0"]` | `arr["0,0"]` |
| `arr[0,0]` | `arr["0\0340"]` (using SUBSEP) |

---

## SUBSEP

```awk
# SUBSEP = subscript separator for multi-dimensional arrays
# Default value: "\034" (non-printing character)

BEGIN {
    # Default behavior
    arr[1,2] = "value"

    for (key in arr) {
        print key           # prints "1\0342" (not readable)
    }
}

# Custom SUBSEP for readable keys
BEGIN {
    SUBSEP = ":"

    arr[1,2] = "value"
    arr["x","y"] = "coord"

    for (key in arr) {
        print key           # prints "1:2" and "x:y"
    }
}
```

### Splitting Multi-Index Keys

```awk
BEGIN {
    SUBSEP = ":"
    arr[1,2] = 100
    arr[3,4] = 200

    for (key in arr) {
        split(key, indices, SUBSEP)
        row = indices[1]
        col = indices[2]
        print "arr[" row "," col "] =", arr[key]
    }
}

# Output:
# arr[1,2] = 100
# arr[3,4] = 200
```

---

## Array Functions (gawk)

### asort() - Sort by Values

```awk
# Syntax: asort(source, [dest])
# Sorts array by VALUES
# Replaces indexes with 1, 2, 3...
# Returns number of elements

BEGIN {
    arr["x"] = "banana"
    arr["y"] = "apple"
    arr["z"] = "cherry"
 
    n = asort(arr)

    for (i = 1; i <= n; i++) {
        print i, arr[i]
    }
}

# Output:
# 1 apple
# 2 banana
# 3 cherry
```

### asorti() - Sort by Indexes

```awk
# Syntax: asorti(source, dest)
# Sorts array INDEXES into dest array
# Returns number of elements

BEGIN {
    arr["banana"] = 1
    arr["apple"] = 2
    arr["cherry"] = 3

    n = asorti(arr, sorted)

    for (i = 1; i <= n; i++) {
        key = sorted[i]
        print key, arr[key]
    }
}

# Output:
# apple 2
# banana 1
# cherry 3
```

### Custom Sort Order (gawk 4.0+)

```awk
# PROCINFO["sorted_in"] controls iteration order

BEGIN {
    PROCINFO["sorted_in"] = "@ind_str_asc"   # sort by index, string, ascending

    arr["banana"] = 3
    arr["apple"] = 1
    arr["cherry"] = 2

    for (key in arr) {
        print key, arr[key]
    }
}

# Output (sorted by key):
# apple 1
# banana 3
# cherry 2
```

| PROCINFO["sorted_in"] | Order |
|----------------------|-------|
| `"@unsorted"` | Default, arbitrary |
| `"@ind_str_asc"` | Index as string, ascending |
| `"@ind_str_desc"` | Index as string, descending |
| `"@ind_num_asc"` | Index as number, ascending |
| `"@ind_num_desc"` | Index as number, descending |
| `"@val_str_asc"` | Value as string, ascending |
| `"@val_str_desc"` | Value as string, descending |
| `"@val_num_asc"` | Value as number, ascending |
| `"@val_num_desc"` | Value as number, descending |

---

## Common Array Patterns

### Word Frequency Count

```awk
# Count occurrences of each word
{
    for (i = 1; i <= NF; i++) {
        words[$i]++
    }
}
END {
    for (word in words) {
        print words[word], word
    }
}

# Run: awk -f wordfreq.awk file.txt | sort -rn | head
```

### Remove Duplicates

```awk
# Print only unique lines
!seen[$0]++

# Explanation:
# - seen[$0] is 0 (false) first time
# - !seen[$0] is 1 (true), so line prints
# - ++ increments AFTER evaluation
# - Next time same line: seen[$0] is 1, !1 is false, no print
```

### Group By Field

```awk
# Sum values grouped by first field
{
    sum[$1] += $2
}
END {
    for (key in sum) {
        print key, sum[key]
    }
}

# Input:
# apple 10
# banana 20
# apple 5
# banana 15

# Output:
# apple 15
# banana 35
```

### Find Maximum per Group

```awk
{
    if ($2 > max[$1]) {
        max[$1] = $2
        maxline[$1] = $0
    }
}
END {
    for (key in maxline) {
        print maxline[key]
    }
}
```

### Two-File Processing

```awk
# First file: build lookup array
# Second file: use lookup array

NR == FNR {
    # First file
    lookup[$1] = $2
    next
}

# Second file
$1 in lookup {
    print $0, lookup[$1]
}

# Run: awk -f script.awk lookup.txt data.txt
```

### Count Unique Values

```awk
{
    unique[$1] = 1
}
END {
    print length(unique), "unique values"
}
```

### Store Lines in Array

```awk
# Store all lines, print in reverse
{
    lines[NR] = $0
}
END {
    for (i = NR; i >= 1; i--) {
        print lines[i]
    }
}
```

### Transpose Data

```awk
# Convert rows to columns
{
    for (i = 1; i <= NF; i++) {
        arr[i,NR] = $i
    }
    if (NF > maxcol) maxcol = NF
}
END {
    for (i = 1; i <= maxcol; i++) {
        for (j = 1; j <= NR; j++) {
            printf "%s%s", arr[i,j], (j < NR ? "\t" : "\n")
        }
    }
}
```

---

## Arrays Quick Reference

| Operation | Syntax |
|-----------|--------|
| Create | `arr[key] = value` |
| Access | `arr[key]` |
| Delete element | `delete arr[key]` |
| Delete array | `delete arr` |
| Check exists | `if (key in arr)` |
| Iterate | `for (k in arr)` |
| Length | `length(arr)` |
| Sort values | `asort(arr)` |
| Sort indexes | `asorti(arr, dest)` |
| Multi-dim | `arr[i,j]` or `arr["i,j"]` |

---

[↑ Back to Arrays Navigation](#arrays-quick-navigation)

---

## Control Flow

### Control Flow Quick Navigation

| # | Section | Description |
|---|---------|-------------|
| 1 | [If Statement](#if-statement) | Basic conditional |
| 2 | [If-Else Statement](#if-else-statement) | Two-way conditional |
| 3 | [If-Else-If Ladder](#if-else-if-ladder) | Multiple conditions |
| 4 | [Ternary Operator](#ternary-operator) | Inline conditional |
| 5 | [While Loop](#while-loop) | Condition-based loop |
| 6 | [Do-While Loop](#do-while-loop) | Loop at least once |
| 7 | [For Loop](#for-loop) | Counter-based loop |
| 8 | [For-In Loop](#for-in-loop) | Array iteration |
| 9 | [Loop Control](#loop-control) | `break`, `continue`, `next`, `exit` |

---

### If Statement

```awk
# Syntax
if (condition)
    action

# Multiple actions
if (condition) {
    action-1
    action-2
}
```

```awk
# Example: Check if even
awk 'BEGIN { 
    num = 10
    if (num % 2 == 0) 
        printf "%d is even number.\n", num 
}'

# Output: 10 is even number.
```

```awk
# Example: In main block
{ 
    if ($3 > 100) 
        print "Large:", $0 
}
```

---

### If-Else Statement

```awk
# Syntax
if (condition)
    action-1
else
    action-2

# Multiple actions
if (condition) {
    action-1
    action-2
} else {
    action-3
    action-4
}
```

```awk
# Example: Check even/odd
awk 'BEGIN {
    num = 11
    if (num % 2 == 0) 
        printf "%d is even number.\n", num
    else 
        printf "%d is odd number.\n", num
}'

# Output: 11 is odd number.
```

```awk
# Example: In main block
{
    if ($3 > 50)
        print "Pass:", $1
    else
        print "Fail:", $1
}
```

---

### If-Else-If Ladder

```awk
# Syntax
if (condition-1)
    action-1
else if (condition-2)
    action-2
else if (condition-3)
    action-3
else
    action-default
```

```awk
# Example: Multiple conditions
awk 'BEGIN {
    a = 30
    
    if (a == 10)
        print "a = 10"
    else if (a == 20)
        print "a = 20"
    else if (a == 30)
        print "a = 30"
    else
        print "a is something else"
}'

# Output: a = 30
```

```awk
# Example: Grade assignment
{
    score = $2
    if (score >= 90)
        grade = "A"
    else if (score >= 80)
        grade = "B"
    else if (score >= 70)
        grade = "C"
    else if (score >= 60)
        grade = "D"
    else
        grade = "F"
    
    print $1, grade
}
```

---

### Ternary Operator

```awk
# Syntax
variable = (condition) ? value-if-true : value-if-false
```

```awk
# Example: Inline conditional
awk 'BEGIN {
    num = 10
    result = (num % 2 == 0) ? "even" : "odd"
    print num, "is", result
}'

# Output: 10 is even
```

```awk
# Example: In print
{ print $1, ($2 > 50 ? "Pass" : "Fail") }
```

```awk
# Example: Nested ternary (use sparingly)
{ 
    grade = ($2 >= 90) ? "A" : ($2 >= 80) ? "B" : ($2 >= 70) ? "C" : "F"
    print $1, grade
}
```

---

### While Loop

```awk
# Syntax
while (condition) {
    action
}
```

```awk
# Example: Print 1 to 5
awk 'BEGIN {
    i = 1
    while (i <= 5) {
        print i
        i++
    }
}'

# Output:
# 1
# 2
# 3
# 4
# 5
```

```awk
# Example: Sum of fields
{
    i = 1
    sum = 0
    while (i <= NF) {
        sum += $i
        i++
    }
    print "Sum:", sum
}
```

---

### Do-While Loop

```awk
# Syntax
do {
    action
} while (condition)

# Loop executes at least once
```

```awk
# Example: Print 1 to 5
awk 'BEGIN {
    i = 1
    do {
        print i
        i++
    } while (i <= 5)
}'

# Output:
# 1
# 2
# 3
# 4
# 5
```

```awk
# Example: Executes once even if condition false
awk 'BEGIN {
    i = 10
    do {
        print "i =", i
        i++
    } while (i < 5)
}'

# Output: i = 10
```

---

### For Loop

```awk
# Syntax
for (initialization; condition; increment) {
    action
}
```

```awk
# Example: Print 1 to 5
awk 'BEGIN {
    for (i = 1; i <= 5; i++) {
        print i
    }
}'

# Output:
# 1
# 2
# 3
# 4
# 5
```

```awk
# Example: Iterate through fields
{
    for (i = 1; i <= NF; i++) {
        print "Field", i, "=", $i
    }
}
```

```awk
# Example: Reverse fields
{
    for (i = NF; i >= 1; i--) {
        printf "%s ", $i
    }
    printf "\n"
}
```

---

### For-In Loop

```awk
# Syntax
for (key in array) {
    action using array[key]
}

# Note: Order is not guaranteed
```

```awk
# Example: Iterate array
awk 'BEGIN {
    fruits["apple"] = "red"
    fruits["banana"] = "yellow"
    fruits["grape"] = "purple"
    
    for (fruit in fruits) {
        print fruit, "is", fruits[fruit]
    }
}'

# Output (order may vary):
# apple is red
# banana is yellow
# grape is purple
```

```awk
# Example: Word frequency
{
    for (i = 1; i <= NF; i++)
        count[$i]++
}
END {
    for (word in count)
        print word, count[word]
}
```

---

### Loop Control

#### break

```awk
# Exit the loop immediately

awk 'BEGIN {
    for (i = 1; i <= 10; i++) {
        if (i == 5) break
        print i
    }
    print "Done"
}'

# Output:
# 1
# 2
# 3
# 4
# Done
```

#### continue

```awk
# Skip to next iteration

awk 'BEGIN {
    for (i = 1; i <= 5; i++) {
        if (i == 3) continue
        print i
    }
}'

# Output:
# 1
# 2
# 4
# 5
```

#### next

```awk
# Skip to next input line (not just loop iteration)

# Skip lines starting with #
/^#/ { next }
{ print }
```

```awk
# Skip blank lines
NF == 0 { next }
{ print }
```

#### nextfile (gawk)

```awk
# Skip to next input file

# Print only first line of each file
FNR == 1 { print FILENAME, $0; nextfile }
```

#### exit

```awk
# Exit the program (runs END block first)

# Stop after finding "error"
/error/ { 
    print "Found error at line", NR
    exit 1
}
END { print "Done" }
```

```awk
# Exit with status code
BEGIN {
    if (ARGC < 2) {
        print "Usage: script.awk file"
        exit 1
    }
}
```

---

### Control Flow Quick Reference: 

#### Conditionals

```awk
# If
if (cond) action

# If-else
if (cond) action1 else action2

# If-else-if
if (cond1) action1
else if (cond2) action2
else action3

# Ternary
var = (cond) ? val1 : val2
```

#### Loops

```awk
# While
while (cond) { action }

# Do-while
do { action } while (cond)

# For
for (i = 0; i < n; i++) { action }

# For-in (arrays)
for (key in arr) { action }
```

#### Control Statements

| Statement | Description |
|-----------|-------------|
| `break` | Exit loop |
| `continue` | Next iteration |
| `next` | Next input line |
| `nextfile` | Next input file (gawk) |
| `exit` | Exit program |
| `exit n` | Exit with status n |

#### Common Patterns

```awk
# Skip header
NR == 1 { next }

# Skip blank lines
/^$/ { next }
NF == 0 { next }

# Skip comments
/^#/ { next }

# Process only matching lines
/pattern/ { action; next }
{ default action }

# Stop at pattern
/stop/ { exit }

# Process first n lines
NR > 10 { exit }

# Process range
NR >= 5 && NR <= 10 { print }

# Conditional field processing
{
    for (i = 1; i <= NF; i++) {
        if ($i ~ /^[0-9]+$/)
            sum += $i
    }
}
```

---

[↑ Back to Control Flow Navigation](#control-flow-quick-navigation)

---

## Built-in Functions

### Functions Quick Navigation

| # | Section | Description |
|---|---------|-------------|
| 1 | [Arithmetic Functions](#arithmetic-functions) | Math operations |
| 2 | [String Functions](#string-functions) | Text manipulation |
| 3 | [Time Functions](#time-functions) | Date and time |
| 4 | [Bit Manipulation Functions](#bit-manipulation-functions) | Bitwise operations (gawk) |
| 5 | [I/O Functions](#io-functions) | Input/output operations |
| 6 | [Miscellaneous Functions](#miscellaneous-functions) | Type, system, etc. |

---

### Arithmetic Functions

| Function | Description |
|----------|-------------|
| `int(x)` | Truncate to integer |
| `sqrt(x)` | Square root |
| `exp(x)` | Exponential (e^x) |
| `log(x)` | Natural logarithm |
| `sin(x)` | Sine (radians) |
| `cos(x)` | Cosine (radians) |
| `atan2(y, x)` | Arctangent of y/x |
| `rand()` | Random number 0 to 1 |
| `srand([seed])` | Seed random generator |

#### Examples

```awk
# int() - Truncate to integer
awk 'BEGIN { print int(5.9) }'       # 5
awk 'BEGIN { print int(-5.9) }'      # -5

# sqrt() - Square root
awk 'BEGIN { print sqrt(16) }'       # 4
awk 'BEGIN { print sqrt(2) }'        # 1.41421

# exp() and log() - Exponential and logarithm
awk 'BEGIN { print exp(1) }'         # 2.71828 (e)
awk 'BEGIN { print log(2.71828) }'   # 1

# sin() and cos() - Trigonometry (radians)
awk 'BEGIN { print sin(0) }'         # 0
awk 'BEGIN { print cos(0) }'         # 1
awk 'BEGIN { pi = 3.14159; print sin(pi/2) }'  # 1

# atan2() - Arctangent
awk 'BEGIN { print atan2(1, 1) }'    # 0.785398 (π/4)

# rand() and srand() - Random numbers
awk 'BEGIN { print rand() }'                    # 0.xxx (same each run)
awk 'BEGIN { srand(); print rand() }'           # 0.xxx (different each run)
awk 'BEGIN { srand(42); print rand() }'         # 0.xxx (reproducible)

# Random integer between 1 and 10
awk 'BEGIN { srand(); print int(rand() * 10) + 1 }'

# Random integer in range [min, max]
awk 'BEGIN { 
    srand()
    min = 5; max = 15
    print int(rand() * (max - min + 1)) + min 
}'
```

#### Derived Math Operations

```awk
# Absolute value
function abs(x) { return (x < 0) ? -x : x }

# Power (x^y)
awk 'BEGIN { print 2^10 }'           # 1024

# Modulo
awk 'BEGIN { print 17 % 5 }'         # 2

# Round to nearest integer
function round(x) { return int(x + 0.5) }

# Ceiling
function ceil(x) { return (x == int(x)) ? x : int(x) + 1 }

# Floor
function floor(x) { return int(x) }

# Min/Max
function min(a, b) { return (a < b) ? a : b }
function max(a, b) { return (a > b) ? a : b }
```

---

### String Functions

| Function | Description |
|----------|-------------|
| `length(s)` | Length of string |
| `substr(s, start, [len])` | Extract substring |
| `index(s, target)` | Find position of target |
| `split(s, arr, [sep])` | Split into array |
| `sub(regex, repl, [target])` | Replace first match |
| `gsub(regex, repl, [target])` | Replace all matches |
| `match(s, regex)` | Find regex match |
| `sprintf(fmt, ...)` | Format string |
| `tolower(s)` | Convert to lowercase |
| `toupper(s)` | Convert to uppercase |
| `gensub(regex, repl, how, [target])` | Advanced replace (gawk) |
| `patsplit(s, arr, regex)` | Split by pattern (gawk) |
| `strtonum(s)` | String to number (gawk) |

#### length()

```awk
# Length of string
awk 'BEGIN { print length("hello") }'        # 5

# Length of field
awk '{ print length($1) }' file

# Length of line
awk '{ print length($0) }' file
awk '{ print length() }' file                # $0 is default

# Filter by length
awk 'length($0) > 80' file                   # lines > 80 chars
```

#### substr()

```awk
# substr(string, start, [length])
# Note: AWK strings are 1-indexed

awk 'BEGIN { print substr("hello world", 1, 5) }'    # hello
awk 'BEGIN { print substr("hello world", 7) }'       # world (to end)
awk 'BEGIN { print substr("hello world", 7, 3) }'    # wor

# Extract parts of field
awk '{ print substr($1, 1, 3) }' file        # first 3 chars of field 1

# Last n characters
awk 'BEGIN { 
    s = "hello"
    n = 2
    print substr(s, length(s) - n + 1) 
}'                                            # lo
```

#### index()

```awk
# index(string, target) - returns position (0 if not found)

awk 'BEGIN { print index("hello world", "wor") }'    # 7
awk 'BEGIN { print index("hello world", "xyz") }'    # 0

# Check if substring exists
awk '{ if (index($0, "error") > 0) print }' file

# Find and extract
awk '{
    pos = index($0, "=")
    if (pos > 0) {
        key = substr($0, 1, pos - 1)
        val = substr($0, pos + 1)
        print key, "->", val
    }
}' file
```

#### split()

```awk
# split(string, array, [separator])
# Returns number of elements

awk 'BEGIN {
    n = split("a:b:c:d", arr, ":")
    print "Count:", n              # 4
    for (i = 1; i <= n; i++)
        print arr[i]               # a, b, c, d
}'

# Split with regex separator
awk 'BEGIN {
    split("a1b2c3d", arr, /[0-9]/)
    for (i in arr) print arr[i]    # a, b, c, d
}'

# Split field
awk -F'|' '{
    n = split($2, parts, ",")
    for (i = 1; i <= n; i++)
        print parts[i]
}' file

# Default separator is FS
awk 'BEGIN { FS = ":" }
{
    n = split($0, arr)             # uses FS
    print "Fields:", n
}' /etc/passwd
```

#### sub() and gsub()

```awk
# sub(regex, replacement, [target])
# Replace first match, modifies in place, returns 0 or 1

awk 'BEGIN {
    s = "hello world"
    sub(/world/, "AWK", s)
    print s                        # hello AWK
}'

# Default target is $0
awk '{ sub(/error/, "ERROR"); print }' file

# gsub() - replace ALL matches
awk 'BEGIN {
    s = "hello world world"
    n = gsub(/world/, "AWK", s)
    print s                        # hello AWK AWK
    print "Replaced:", n           # 2
}'

# Remove all spaces
awk '{ gsub(/ /, ""); print }' file

# Replace in specific field
awk '{ gsub(/old/, "new", $2); print }' file

# & in replacement = matched text
awk '{ gsub(/[0-9]+/, "[&]"); print }' file
# Input:  abc123def456
# Output: abc[123]def[456]
```

#### match()

```awk
# match(string, regex)
# Returns position of match (0 if none)
# Sets RSTART and RLENGTH

awk 'BEGIN {
    s = "hello123world"
    if (match(s, /[0-9]+/)) {
        print "Position:", RSTART   # 6
        print "Length:", RLENGTH    # 3
        print "Match:", substr(s, RSTART, RLENGTH)  # 123
    }
}'

# Extract all numbers
awk '{
    while (match($0, /[0-9]+/)) {
        print substr($0, RSTART, RLENGTH)
        $0 = substr($0, RSTART + RLENGTH)
    }
}' file
```

#### sprintf()

```awk
# sprintf(format, values...) - returns formatted string

awk 'BEGIN {
    s = sprintf("%s is %d years old", "Alice", 30)
    print s                        # Alice is 30 years old
}'

# Padding and alignment
awk 'BEGIN {
    print sprintf("%-10s %5d", "Alice", 30)   # Alice          30
    print sprintf("%010d", 42)                 # 0000000042
}'

# Float formatting
awk 'BEGIN {
    print sprintf("%.2f", 3.14159)            # 3.14
    print sprintf("%8.2f", 3.14159)           #     3.14
}'
```

#### tolower() and toupper()

```awk
awk 'BEGIN { print tolower("HELLO World") }'  # hello world
awk 'BEGIN { print toupper("hello World") }'  # HELLO WORLD

# Case-insensitive comparison
awk '{ if (tolower($1) == "error") print }' file

# Capitalize first letter
awk '{ 
    first = toupper(substr($0, 1, 1))
    rest = substr($0, 2)
    print first rest 
}' file
```

#### gensub() (gawk only)

```awk
# gensub(regex, replacement, how, [target])
# Returns new string (doesn't modify original)
# Supports backreferences \1 \2 etc.

awk 'BEGIN {
    s = "hello world"
    
    # Replace all
    print gensub(/o/, "0", "g", s)        # hell0 w0rld
    
    # Replace first
    print gensub(/o/, "0", 1, s)          # hell0 world
    
    # Replace second
    print gensub(/o/, "0", 2, s)          # hello w0rld
    
    print s                                # hello world (unchanged)
}'

# Backreferences
awk 'BEGIN {
    s = "John Smith"
    print gensub(/(.+) (.+)/, "\\2, \\1", "g", s)
}'
# Output: Smith, John

# Reformat date
awk 'BEGIN {
    date = "2024-01-15"
    print gensub(/([0-9]+)-([0-9]+)-([0-9]+)/, "\\2/\\3/\\1", "g", date)
}'
# Output: 01/15/2024
```

#### patsplit() (gawk only)

```awk
# patsplit(string, array, pattern, [seps])
# Split by extracting pattern matches

awk 'BEGIN {
    s = "abc123def456ghi789"
    n = patsplit(s, nums, /[0-9]+/)
    for (i = 1; i <= n; i++)
        print nums[i]              # 123, 456, 789
}'

# Extract all email addresses
awk '{
    n = patsplit($0, emails, /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/)
    for (i = 1; i <= n; i++)
        print emails[i]
}' file
```

#### strtonum() (gawk only)

```awk
# Convert string to number (handles hex, octal)

awk 'BEGIN {
    print strtonum("42")           # 42
    print strtonum("0x2A")         # 42 (hex)
    print strtonum("052")          # 42 (octal)
}'
```

---

### Time Functions

| Function | Description |
|----------|-------------|
| `systime()` | Current Unix timestamp |
| `mktime(datespec)` | Convert date to timestamp |
| `strftime(format, [timestamp])` | Format timestamp |

#### systime()

```awk
# Returns current Unix timestamp (seconds since 1970-01-01)

awk 'BEGIN { print systime() }'    # 1705312345 (example)
```

#### mktime()

```awk
# mktime("YYYY MM DD HH MM SS")
# Returns Unix timestamp for given date

awk 'BEGIN {
    ts = mktime("2024 01 15 10 30 00")
    print ts                       # 1705315800
}'

# Calculate days between dates
awk 'BEGIN {
    date1 = mktime("2024 01 01 00 00 00")
    date2 = mktime("2024 12 31 00 00 00")
    days = (date2 - date1) / 86400
    print "Days:", days            # 365
}'
```

#### strftime()

```awk
# strftime(format, [timestamp])
# Default timestamp is current time

awk 'BEGIN { print strftime("%Y-%m-%d %H:%M:%S") }'
# Output: 2024-01-15 10:30:00

awk 'BEGIN { print strftime("%A, %B %d, %Y") }'
# Output: Monday, January 15, 2024

# Format specific timestamp
awk 'BEGIN {
    ts = mktime("2024 01 15 10 30 00")
    print strftime("%Y-%m-%d", ts)  # 2024-01-15
}'
```

#### strftime Format Codes

| Code | Description | Example |
|------|-------------|---------|
| `%Y` | Year (4 digit) | 2024 |
| `%y` | Year (2 digit) | 24 |
| `%m` | Month (01-12) | 01 |
| `%d` | Day (01-31) | 15 |
| `%H` | Hour (00-23) | 14 |
| `%M` | Minute (00-59) | 30 |
| `%S` | Second (00-59) | 45 |
| `%A` | Weekday name | Monday |
| `%a` | Weekday abbrev | Mon |
| `%B` | Month name | January |
| `%b` | Month abbrev | Jan |
| `%j` | Day of year | 015 |
| `%U` | Week number | 03 |
| `%w` | Weekday (0-6) | 1 |
| `%Z` | Timezone | EST |
| `%%` | Literal % | % |

---

### Bit Manipulation Functions (gawk)

| Function | Description |
|----------|-------------|
| `and(v1, v2)` | Bitwise AND |
| `or(v1, v2)` | Bitwise OR |
| `xor(v1, v2)` | Bitwise XOR |
| `compl(val)` | Bitwise complement |
| `lshift(val, n)` | Left shift by n bits |
| `rshift(val, n)` | Right shift by n bits |

#### Examples

```awk
awk 'BEGIN {
    # and() - Bitwise AND
    print and(12, 10)              # 8  (1100 & 1010 = 1000)
    
    # or() - Bitwise OR
    print or(12, 10)               # 14 (1100 | 1010 = 1110)
    
    # xor() - Bitwise XOR
    print xor(12, 10)              # 6  (1100 ^ 1010 = 0110)
    
    # compl() - Complement
    print compl(0)                 # large number (all 1s)
    
    # lshift() - Left shift
    print lshift(1, 4)             # 16 (1 << 4)
    
    # rshift() - Right shift
    print rshift(16, 2)            # 4  (16 >> 2)
}'
```

```awk
# Check if bit is set
function bit_set(val, bit) {
    return and(val, lshift(1, bit)) != 0
}

# Set a bit
function set_bit(val, bit) {
    return or(val, lshift(1, bit))
}

# Clear a bit
function clear_bit(val, bit) {
    return and(val, compl(lshift(1, bit)))
}

# Toggle a bit
function toggle_bit(val, bit) {
    return xor(val, lshift(1, bit))
}
```

---

### I/O Functions

| Function | Description |
|----------|-------------|
| `getline` | Read next line |
| `getline var` | Read into variable |
| `getline < file` | Read from file |
| `cmd \| getline` | Read from command |
| `close(file)` | Close file or pipe |
| `fflush([file])` | Flush output buffer |
| `system(cmd)` | Execute shell command |

#### getline

```awk
# Read next line into $0, updates NF, NR
{
    if ((getline) > 0) {
        print "Next line:", $0
    }
}

# Read into variable (doesn't change $0, NF)
{
    if ((getline nextline) > 0) {
        print "Current:", $0
        print "Next:", nextline
    }
}

# Return values:
#  1 = success
#  0 = end of file
# -1 = error
```

#### getline from file

```awk
# Read from specific file
BEGIN {
    while ((getline line < "data.txt") > 0) {
        print line
    }
    close("data.txt")
}

# Read entire file into array
BEGIN {
    n = 0
    while ((getline lines[++n] < "data.txt") > 0);
    close("data.txt")
    
    for (i = 1; i < n; i++)
        print lines[i]
}
```

#### getline from command

```awk
# Read from command output
BEGIN {
    while (("ls -la" | getline line) > 0) {
        print line
    }
    close("ls -la")
}

# Get current date
BEGIN {
    "date" | getline current_date
    close("date")
    print "Today:", current_date
}

# Read single value
BEGIN {
    "whoami" | getline user
    close("whoami")
    print "User:", user
}
```

#### Output redirection

```awk
# Write to file
{ print $0 > "output.txt" }

# Append to file
{ print $0 >> "output.txt" }

# Pipe to command
{ print $0 | "sort" }
{ print $0 | "mail -s 'Report' user@example.com" }

# Close file/pipe (important for many files)
{
    outfile = "output_" $1 ".txt"
    print $0 > outfile
    close(outfile)
}
```

#### close()

```awk
# Close file or pipe
{
    print $0 > "output.txt"
}
END {
    close("output.txt")
}

# Required when:
# - Re-reading a file
# - Writing to many files (avoid too many open files)
# - Ensuring pipe command completes
```

#### fflush()

```awk
# Flush output buffer
{ 
    print $0
    fflush()           # flush stdout
}

# Flush specific file
{
    print $0 > "output.txt"
    fflush("output.txt")
}

# Flush all output
{ fflush("") }
```

#### system()

```awk
# Execute shell command, returns exit status

BEGIN {
    ret = system("ls -la")
    print "Exit status:", ret
}

# Run command for each line
{
    cmd = "echo " $0 " | wc -c"
    system(cmd)
}

# Conditional execution
{
    if (system("test -f " $1) == 0) {
        print $1, "exists"
    }
}
```

---

### Miscellaneous Functions

| Function | Description |
|----------|-------------|
| `typeof(x)` | Return type of variable (gawk) |
| `isarray(x)` | Check if array (gawk) |
| `delete arr[key]` | Delete array element |
| `delete arr` | Delete entire array (gawk) |

#### typeof() (gawk)

```awk
awk 'BEGIN {
    a = 42
    b = "hello"
    c[1] = "x"
    
    print typeof(a)        # number
    print typeof(b)        # string
    print typeof(c)        # array
    print typeof(d)        # untyped (undefined)
}'
```

#### isarray() (gawk)

```awk
awk 'BEGIN {
    arr[1] = "a"
    str = "hello"
    
    print isarray(arr)     # 1 (true)
    print isarray(str)     # 0 (false)
}'
```

---

### Built-in Functions Quick Reference

#### Arithmetic

| Function | Returns |
|----------|---------|
| `int(x)` | Integer part |
| `sqrt(x)` | Square root |
| `exp(x)` | e^x |
| `log(x)` | Natural log |
| `sin(x)` `cos(x)` | Trig functions |
| `atan2(y,x)` | Arctangent |
| `rand()` | Random 0-1 |
| `srand([n])` | Seed random |

#### String

| Function | Returns |
|----------|---------|
| `length(s)` | Length |
| `substr(s,i,[n])` | Substring |
| `index(s,t)` | Position of t |
| `split(s,a,[sep])` | Element count |
| `sub(r,s,[t])` | 0 or 1 |
| `gsub(r,s,[t])` | Replace count |
| `match(s,r)` | Position |
| `sprintf(f,...)` | Formatted string |
| `tolower(s)` | Lowercase |
| `toupper(s)` | Uppercase |
| `gensub(r,s,h,[t])` | New string (gawk) |

#### Time (gawk)

| Function | Returns |
|----------|---------|
| `systime()` | Unix timestamp |
| `mktime(date)` | Timestamp |
| `strftime(fmt,[ts])` | Formatted date |

#### I/O

| Function | Returns |
|----------|---------|
| `getline` | 1, 0, or -1 |
| `close(f)` | 0 or -1 |
| `system(cmd)` | Exit status |
| `fflush([f])` | 0 or -1 |

#### Common Patterns

```awk
# Random integer 1-10
int(rand() * 10) + 1

# Extract filename extension
match(file, /\.[^.]+$/); ext = substr(file, RSTART+1)

# Trim whitespace
gsub(/^[ \t]+|[ \t]+$/, "", str)

# Title case
{ 
    $0 = tolower($0)
    $0 = toupper(substr($0,1,1)) substr($0,2)
}

# Parse key=value
{
    pos = index($0, "=")
    key = substr($0, 1, pos-1)
    val = substr($0, pos+1)
}

# Current datetime
strftime("%Y-%m-%d %H:%M:%S")
```

---

[↑ Back to Functions Navigation](#functions-quick-navigation)

---

## User-Defined Functions

### Syntax

```awk
function function_name(argument1, argument2, ...) {
    function body
    return value
}
```

### Rules

- Function name must begin with a letter
- Can contain letters, numbers, underscores
- Cannot use AWK reserved words
- Arguments are optional
- Arguments are passed by value (scalars) or by reference (arrays)

---

### Basic Example

```awk
# Define function
function greet(name) {
    return "Hello, " name "!"
}

# Use function
BEGIN {
    print greet("World")    # Hello, World!
}
```

---

### Multiple Arguments

```awk
function find_min(num1, num2) {
    if (num1 < num2)
        return num1
    return num2
}

function find_max(num1, num2) {
    if (num1 > num2)
        return num1
    return num2
}

BEGIN {
    print "Min:", find_min(10, 20)    # Min: 10
    print "Max:", find_max(10, 20)    # Max: 20
}
```

---

### No Arguments

```awk
function print_separator() {
    print "-------------------"
}

BEGIN {
    print_separator()
    print "Report"
    print_separator()
}
```

---

### Local Variables

```awk
# Variables after arguments are local (convention: add extra spaces)
function sum_array(arr, n,    i, sum) {
    sum = 0
    for (i = 1; i <= n; i++) {
        sum += arr[i]
    }
    return sum
}

BEGIN {
    a[1] = 10; a[2] = 20; a[3] = 30
    print sum_array(a, 3)    # 60
}
```

> [!NOTE]
> AWK doesn't have true local variables. The convention is to declare them as extra parameters (often separated by extra spaces for clarity).

---

### Arrays as Arguments

```awk
# Arrays are passed by reference (modified in place)
function double_values(arr, n,    i) {
    for (i = 1; i <= n; i++) {
        arr[i] *= 2
    }
}

BEGIN {
    a[1] = 5; a[2] = 10; a[3] = 15
    double_values(a, 3)
    print a[1], a[2], a[3]    # 10 20 30
}
```

---

### Recursive Functions

```awk
function factorial(n) {
    if (n <= 1)
        return 1
    return n * factorial(n - 1)
}

BEGIN {
    print factorial(5)    # 120
}
```

```awk
function fibonacci(n) {
    if (n <= 1)
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
}

BEGIN {
    for (i = 0; i < 10; i++)
        printf "%d ", fibonacci(i)
    print ""
}
# Output: 0 1 1 2 3 5 8 13 21 34
```

---

### Practical Examples

#### Trim Whitespace

```awk
function trim(s) {
    gsub(/^[ \t]+|[ \t]+$/, "", s)
    return s
}

{
    print trim($0)
}
```

#### Repeat String

```awk
function repeat(s, n,    result, i) {
    result = ""
    for (i = 1; i <= n; i++)
        result = result s
    return result
}

BEGIN {
    print repeat("-", 20)    # --------------------
    print repeat("ab", 5)    # ababababab
}
```

#### Check if Numeric

```awk
function is_numeric(s) {
    return s ~ /^-?[0-9]*\.?[0-9]+$/
}

{
    if (is_numeric($1))
        print $1, "is a number"
    else
        print $1, "is not a number"
}
```

#### Join Array

```awk
function join(arr, n, sep,    result, i) {
    result = arr[1]
    for (i = 2; i <= n; i++)
        result = result sep arr[i]
    return result
}

BEGIN {
    a[1] = "one"; a[2] = "two"; a[3] = "three"
    print join(a, 3, ", ")    # one, two, three
}
```

#### Reverse String

```awk
function reverse(s,    i, result) {
    result = ""
    for (i = length(s); i >= 1; i--)
        result = result substr(s, i, 1)
    return result
}

BEGIN {
    print reverse("hello")    # olleh
}
```

#### Title Case

```awk
function title_case(s,    words, n, i, result) {
    n = split(tolower(s), words, " ")
    for (i = 1; i <= n; i++) {
        words[i] = toupper(substr(words[i], 1, 1)) substr(words[i], 2)
    }
    return join(words, n, " ")
}
```

#### Absolute Value

```awk
function abs(x) {
    return (x < 0) ? -x : x
}
```

#### Round to Decimal Places

```awk
function round(x, decimals,    mult) {
    mult = 10 ^ decimals
    return int(x * mult + 0.5) / mult
}

BEGIN {
    print round(3.14159, 2)    # 3.14
}
```

---

### User-Defined Functions Quick Reference

```awk
# Basic syntax
function name(args) { body; return value }

# With local variables (convention)
function name(args,    local1, local2) { body }

# No return value (procedure)
function print_header() { print "====" }

# Return value
function add(a, b) { return a + b }

# Array argument (passed by reference)
function process(arr, n) { arr[1] = 0 }

# Recursive
function fact(n) { return n <= 1 ? 1 : n * fact(n-1) }

# Call functions
BEGIN { result = my_function(arg1, arg2) }
{ my_function($1, $2) }
END { print my_function(total) }
```

---

[↑ Back to Index](#index)

---

## Output Redirection

### Redirection Quick Navigation

| # | Section | Description |
|---|---------|-------------|
| 1 | [Write to File](#write-to-file) | `>` operator |
| 2 | [Append to File](#append-to-file) | `>>` operator |
| 3 | [Pipe to Command](#pipe-to-command) | `\|` operator |
| 4 | [Two-Way Communication](#two-way-communication) | `\|&` operator (gawk) |
| 5 | [Closing Files and Pipes](#closing-files-and-pipes) | `close()` function |

---

### Write to File

```awk
# Syntax
print DATA > "output-file"
printf FORMAT, DATA > "output-file"
```

- Creates file if it doesn't exist
- **Overwrites** file on first write
- Subsequent writes append (within same AWK run)

#### Examples

```awk
# Write to file
awk 'BEGIN { print "Hello, World!" > "/tmp/message.txt" }'

# Write fields to file
awk '{ print $1, $2 > "output.txt" }' input.txt

# Write to file based on condition
awk '{ 
    if ($3 > 100) 
        print $0 > "large.txt"
    else 
        print $0 > "small.txt"
}' data.txt

# Write to dynamically named files
awk '{ 
    outfile = $1 ".txt"
    print $0 > outfile
}' data.txt
```

---

### Append to File

```awk
# Syntax
print DATA >> "output-file"
printf FORMAT, DATA >> "output-file"
```

- Creates file if it doesn't exist
- **Appends** to existing content

#### Examples

```awk
# Append to file
awk 'BEGIN { print "New line" >> "/tmp/message.txt" }'

# Append log entries
awk '{ 
    print strftime("%Y-%m-%d %H:%M:%S"), $0 >> "log.txt" 
}' events.txt

# Preserve existing and add new
awk 'BEGIN { 
    print "--- Start ---" >> "report.txt"
}
{ 
    print $0 >> "report.txt" 
}
END { 
    print "--- End ---" >> "report.txt"
}' data.txt
```

---

### Pipe to Command

```awk
# Syntax
print DATA | "command"
printf FORMAT, DATA | "command"
```

- Sends output to another program
- Command runs as shell process

#### Examples

```awk
# Convert to uppercase
awk 'BEGIN { print "hello, world!" | "tr [a-z] [A-Z]" }'
# Output: HELLO, WORLD!

# Sort output
awk '{ print $2 | "sort" }' data.txt

# Sort numerically and get unique
awk '{ print $1 | "sort -n | uniq" }' data.txt

# Count lines with wc
awk '{ print $0 | "wc -l" }' data.txt

# Send email
awk 'END { 
    print "Process complete: " NR " lines" | "mail -s \"Report\" user@example.com"
}' data.txt

# Pipe to multiple commands
awk '{ 
    print $1 | "sort | uniq -c | sort -rn | head -10"
}' access.log
```

---

### Two-Way Communication

```awk
# Syntax (gawk only)
print DATA |& "command"    # send to command
"command" |& getline var   # receive from command
```

- Send data to command AND receive results back
- Uses `|&` operator
- Must close write end before reading

#### Examples

```awk
# Basic two-way communication
BEGIN {
    cmd = "tr [a-z] [A-Z]"
    
    # Send to command
    print "hello, world!" |& cmd
    
    # Close write end (important!)
    close(cmd, "to")
    
    # Read from command
    cmd |& getline result
    print result
    
    # Close completely
    close(cmd)
}
# Output: HELLO, WORLD!
```

```awk
# Interact with bc calculator
BEGIN {
    cmd = "bc"
    
    print "scale=2; 22/7" |& cmd
    close(cmd, "to")
    
    cmd |& getline pi
    print "Pi approximation:", pi
    
    close(cmd)
}
# Output: Pi approximation: 3.14
```

```awk
# Multiple exchanges
BEGIN {
    cmd = "cat -n"    # number lines
    
    print "first" |& cmd
    print "second" |& cmd
    print "third" |& cmd
    close(cmd, "to")
    
    while ((cmd |& getline line) > 0) {
        print line
    }
    close(cmd)
}
```

---

### Closing Files and Pipes

```awk
# Syntax
close("filename")
close("command")
close("command", "to")    # close write end only (two-way)
close("command", "from")  # close read end only (two-way)
```

#### When to Close

- Writing to many different files (avoid "too many open files")
- Re-reading a file from beginning
- Ensuring pipe command completes
- Two-way communication (must close "to" before reading)

#### Examples

```awk
# Close after writing to many files
{
    outfile = "output_" $1 ".txt"
    print $0 > outfile
    close(outfile)
}

# Re-read a file
BEGIN {
    while ((getline line < "data.txt") > 0)
        print "First pass:", line
    close("data.txt")
    
    while ((getline line < "data.txt") > 0)
        print "Second pass:", line
    close("data.txt")
}

# Ensure sort completes before continuing
{
    print $0 | "sort > sorted.txt"
}
END {
    close("sort > sorted.txt")
    # Now sorted.txt is complete
}
```

---

### Practical Examples

#### Split File by Column Value

```awk
{
    outfile = $1 ".txt"
    print $0 > outfile
}
END {
    # Close all files (good practice)
    for (file in PROCINFO["open_files"])
        close(file)
}
```

#### Create Report with Header/Footer

```awk
BEGIN {
    outfile = "report.txt"
    print "====== REPORT ======" > outfile
    print "Date:", strftime("%Y-%m-%d") > outfile
    print "" > outfile
}
{
    print $0 > outfile
}
END {
    print "" > outfile
    print "Total lines:", NR > outfile
    print "====================" > outfile
    close(outfile)
}
```

#### Log Errors to Separate File

```awk
{
    if (/ERROR/) {
        print $0 > "errors.log"
        print $0 >> "all.log"
    } else if (/WARNING/) {
        print $0 > "warnings.log"
        print $0 >> "all.log"
    } else {
        print $0 >> "all.log"
    }
}
```

#### Process and Sort Output

```awk
{
    # Count occurrences
    count[$1]++
}
END {
    # Print and sort
    for (key in count) {
        print count[key], key | "sort -rn"
    }
    close("sort -rn")
}
```

#### Interactive Command

```awk
# Query a database (example with sqlite)
BEGIN {
    db = "sqlite3 mydb.db"
    
    print "SELECT name FROM users WHERE active=1;" |& db
    close(db, "to")
    
    while ((db |& getline name) > 0) {
        print "Active user:", name
    }
    close(db)
}
```

---

### Output Redirection Quick Reference

#### Operators

| Operator | Description | Creates File | Overwrites |
|----------|-------------|--------------|------------|
| `>` | Write to file | Yes | Yes (first write) |
| `>>` | Append to file | Yes | No |
| `\|` | Pipe to command | N/A | N/A |
| `\|&` | Two-way pipe (gawk) | N/A | N/A |

#### Syntax Summary

```awk
# Write to file (overwrites)
print "text" > "file.txt"

# Append to file
print "text" >> "file.txt"

# Pipe to command
print "text" | "command"

# Two-way communication (gawk)
print "text" |& "command"
close("command", "to")
"command" |& getline result
close("command")

# Close file/pipe
close("file.txt")
close("command")
```

#### Common Patterns

```awk
# Write different data to different files
/error/   { print > "errors.txt" }
/warning/ { print > "warnings.txt" }
          { print > "all.txt" }

# Dynamic filename
{ print > ($1 ".txt") }

# Sorted unique output
{ print | "sort -u" }

# Top 10 most frequent
{ count[$1]++ }
END {
    for (k in count) print count[k], k | "sort -rn | head -10"
}

# Write to file and stdout
{ 
    print > "file.txt"
    print
}

# Tee equivalent
{ print | "tee file.txt" }
```

---

[↑ Back to Index](#index)

---


