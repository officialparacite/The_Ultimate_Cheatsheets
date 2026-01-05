
---

# AWK

---

## Index

| * | Table of Contents |
|----|-----|
| - | [Program Structure](#awk-program-structure) |
| - | [Running AWK](#running-awk) |
| - | [Command Line Options](#command-line-options) |
| - | [Block Types](#block-types) |
| - | [Printing & Output](#printing--output) |
| - | [Print Quick Reference](#print-quick-reference) |
| - | [Standard Variables](#standard-variables-all-awk) |
| - | [Record/Field Counters](#recordfield-counters) |
| - | [File and Arguments](#file-and-arguments) |
| - | [Pattern Matching Results](#pattern-matching-results) |
| - | [GNU AWK Only](#gnu-awk-gawk-only) |
| - | [Common Patterns](#quick-reference-common-patterns) |
| - | [Field Access](#quick-reference-field-access) |
| - | [Operators](#operators) |
| - | [Regular Expressions](#regular-expressions) |



---

## AWK Program Structure

```
BEGIN { ... }    # Runs ONCE before any input is read
      { ... }    # Runs for EACH line/record of input
END   { ... }    # Runs ONCE after all input is processed
```

## Quick Example

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

---

# Printing & Output

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

---

## Print Quick Reference

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

---

## Quick Reference: Common Patterns

```awk
NR == 1                 # first line only
NR > 1                  # skip header
NR == FNR               # first file only (multi-file)
NF > 0                  # non-empty lines
NF == 4                 # lines with exactly 4 fields
$1 == "error"           # first field equals "error"
/regex/                 # line matches regex
$2 ~ /regex/            # second field matches regex
$3 !~ /regex/           # third field doesn't match
END { print NR }        # total line count
```

---

## Quick Reference: Field Access

```awk
$0          # entire line
$1          # first field
$NF         # last field
$(NF-1)     # second-to-last field
$NF = "x"   # modify last field
NF = 3      # truncate to 3 fields
```

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

[↑ Back to Regex Navigation](#regex-quick-navigation)

---


