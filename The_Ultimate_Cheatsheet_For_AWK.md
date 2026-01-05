
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
