
---

# Bash Scripting

## Index

| * | Table of Contents |
|---|-------------------|
| - | [Variables](#variables) |
| - | [Arithmetic](#arithmetic) |
| - | [Parameter Expansion](#parameter-expansion) |
| - | [Arrays](#arrays) |
| - | [Positional Arguments](#positional-arguments) |
| - | [Command Substitution](#command-substitution) |
| - | [Conditional Statements](#conditional-statements) |
| - | [File Checks](#file-checks) |
| - | [Logical Operators](#logical-operators) |
| - | [Loops](#loops) |
| - | [Input/Output](#inputoutput) |
| - | [Redirection & Piping](#redirection--piping) |
| - | [Text Processing](#text-processing) |
| - | [Functions](#functions) |
| - | [Exit Codes](#exit-codes) |
| - | [Miscellaneous](#miscellaneous) |

---

## Variables

```bash
name="Alice"                    # declaring a variable
echo "$name"                    # using the variable
printf "Hello %s\n" "world"     # using printf with format specifiers
readonly pi=3.14                # declaring a constant variable
unset name                      # removing the variable

local var="value"               # local variable (inside functions)
export VAR="value"              # export for child processes
```

---

## Arithmetic

```bash
# Basic arithmetic
echo $(( 3 + 5 ))               # 8
echo $(( 10 - 3 ))              # 7
echo $(( 4 * 5 ))               # 20
echo $(( 20 / 4 ))              # 5
echo $(( 17 % 5 ))              # 2 (modulo)
echo $(( 2 ** 10 ))             # 1024 (exponent)

# Increment/Decrement
(( count++ ))                   # increment
(( count-- ))                   # decrement
(( count += 10 ))               # add and assign

# Advanced arithmetic with bc
echo "5 + 3" | bc               # 8
echo "scale=2; 22/7" | bc       # 3.14
echo "5 + 50*3/20 + (19*2)/7" | bc -l   # 17.42857142857142857142
```

---

## Parameter Expansion

```bash
echo "${variable}"                      # variable value
echo "${#variable}"                     # string length
echo "${variable/old/new}"              # replace first occurrence
echo "${variable//old/new}"             # replace all occurrences
echo "${variable:start:length}"         # substring/slicing
echo "${variable:5}"                    # from position 5 to end
echo "${variable: -5}"                  # last 5 characters

echo "${variable#pattern}"              # remove prefix (shortest)
echo "${variable##pattern}"             # remove prefix (longest)
echo "${variable%pattern}"              # remove suffix (shortest)
echo "${variable%%pattern}"             # remove suffix (longest)

echo "${variable:-default}"             # default if unset
echo "${variable:=default}"             # assign default if unset
echo "${variable:?error message}"       # error if unset
echo "${variable:+alternative}"         # alternative if set

echo "${!other_variable}"               # indirect expansion

echo "${variable^^}"                    # uppercase (bash 4+)
echo "${variable,,}"                    # lowercase (bash 4+)
```

---

## Arrays

### Indexed Arrays

```bash
array=(one two three four five six)

echo "${array[0]}"              # one (first element)
echo "${array[-1]}"             # six (last element)
echo "${array[@]}"              # all elements
echo "${#array[@]}"             # length of array
echo "${#array[2]}"             # length of element
echo "${!array[@]}"             # all indices

echo "${array[@]:2:3}"          # slicing (3 elements from index 2)
echo "${array[@]/one/seven}"    # substitution

array+=("seven")                # append element
unset array[1]                  # remove element
```

### Associative Arrays (Bash 4+)

```bash
declare -A colors
colors[red]="#FF0000"
colors[green]="#00FF00"

echo "${colors[red]}"           # #FF0000
echo "${!colors[@]}"            # all keys
echo "${colors[@]}"             # all values

for key in "${!colors[@]}"; do
    echo "$key: ${colors[$key]}"
done
```

---

## Positional Arguments

```bash
$0                              # name of the current script
$1                              # first argument
$2                              # second argument
${10}                           # tenth argument (braces for 10+)
$@                              # all arguments (as separate words)
$*                              # all arguments (as single string)
$#                              # number of arguments
$$                              # PID of the script
$?                              # exit status of last command
$!                              # PID of last background process

shift                           # remove first argument
shift 2                         # remove first 2 arguments
```

---

## Command Substitution

```bash
date=$(date)
files=$(ls -l)
count=$(wc -l < file.txt)

echo "Today is $(date +%Y-%m-%d)"

# Older syntax (harder to nest)
date=`date`
```

---

## Conditional Statements

### Numeric Comparison

```bash
if (( a > 5 )); then echo "yes"; fi
if (( a >= 10 && a <= 20 )); then echo "in range"; fi
```

| (( )) | [[ ]] | Description |
|-------|-------|-------------|
| `==` | `-eq` | Equal |
| `!=` | `-ne` | Not equal |
| `>` | `-gt` | Greater than |
| `>=` | `-ge` | Greater or equal |
| `<` | `-lt` | Less than |
| `<=` | `-le` | Less or equal |

### String Comparison

```bash
if [[ "$str" == "hello" ]]; then
    echo "match"
elif [[ "$str" == "world" ]]; then
    echo "world"
else
    echo "no match"
fi

[[ "$str" == pattern* ]]        # glob pattern matching
[[ "$str" =~ ^regex$ ]]         # regex matching
[[ -z "$str" ]]                 # empty check
[[ -n "$str" ]]                 # non-empty check
```

### Case Statement

```bash
case "$fruit" in
    apple)
        echo "red"
        ;;
    banana|lemon)
        echo "yellow"
        ;;
    *)
        echo "unknown"
        ;;
esac
```

---

## File Checks

```bash
[[ -e file ]]                   # exists
[[ -f file ]]                   # exists and is regular file
[[ -d file ]]                   # exists and is directory
[[ -L file ]]                   # exists and is symlink
[[ -s file ]]                   # exists and size > 0
[[ -r file ]]                   # readable
[[ -w file ]]                   # writable
[[ -x file ]]                   # executable

[[ file1 -nt file2 ]]           # file1 newer than file2
[[ file1 -ot file2 ]]           # file1 older than file2
[[ file1 -ef file2 ]]           # same file (hard link)
```

---

## Logical Operators

```bash
# Within conditionals
[[ -f file && -r file ]]        # AND
[[ -f file1 || -f file2 ]]      # OR
[[ ! -f file ]]                 # NOT

# Command chaining
[ -f file ] && echo "exists"    # run if first succeeds
[ -f file ] || echo "missing"   # run if first fails
cmd1 && cmd2 || cmd3            # if-then-else style
```

---

## Loops

### For Loops

```bash
for i in {1..5}; do echo "$i"; done

for i in {0..10..2}; do echo "$i"; done     # with step

for fruit in apple banana orange; do
    echo "$fruit"
done

for item in "${array[@]}"; do
    echo "$item"
done

for file in *.txt; do
    echo "$file"
done

for file in $(ls *.txt); do
    echo "$file"
done
```

### C-Style For Loop

```bash
for (( i=0; i<5; i++ )); do
    echo "$i"
done
```

### While Loop

```bash
while (( count < 5 )); do
    echo "$count"
    (( count++ ))
done

while read line; do
    echo "$line"
done < file.txt
```

### Until Loop

```bash
until (( count >= 5 )); do
    echo "$count"
    (( count++ ))
done
```

### Loop Control

```bash
break                           # exit loop
continue                        # skip to next iteration
```

### Piping with Loops

```bash
# Pipe entire loop output once
for i in {1..5}; do
    echo "$i"
done | sort -r

# Pipe each iteration separately
for i in {1..5}; do
    echo "$i" | cmd
done
```

---

## Input/Output

```bash
read string                     # read from stdin
read -p "Prompt: " var          # with prompt
read -s password                # silent (for passwords)
read -t 5 var                   # with timeout
read -n 1 char                  # single character

# Read from file
while read line; do
    echo "$line"
done < file.txt

# Read with field separator
while IFS=: read user _ uid _; do
    echo "$user: $uid"
done < /etc/passwd

# Read file into array
mapfile -t lines < file.txt
readarray -t lines < file.txt
```

### Here Documents

```bash
cat << EOF
Line 1
Variable: $name
EOF

cat << 'EOF'                    # no variable expansion
Variable: $name (literal)
EOF

cat <<< "Here string"           # single line
```

---

## Redirection & Piping

```bash
echo "hello" > output.txt       # overwrite file
echo "world" >> output.txt      # append to file
command < input.txt             # input from file

command 2> errors.txt           # redirect stderr
command > out.txt 2>&1          # redirect both stdout and stderr
command &> file                 # shorthand for both
command &> /dev/null            # discard all output

cmd1 | cmd2                     # pipe stdout to next command
cmd1 |& cmd2                    # pipe stdout + stderr

command | tee output.txt        # output to file AND stdout
command | tee -a output.txt     # append

diff <(cmd1) <(cmd2)            # process substitution
```

---

## Text Processing

### AWK

```bash
awk 'NR==1' file.txt                    # first row
awk 'NR>=2 && NR<=5' file.txt           # rows 2 to 5
awk -F',' '{print $2}' file.csv         # second column (comma-separated)
awk '{print $1, $3}' file.txt           # multiple columns
awk '$3 > 100 {print $1, $3}' file.txt  # filter rows by condition
awk '{print $1 + $2}' file.txt          # arithmetic

awk '{sum += $2} END {print sum}' file.txt      # sum column
awk '{sum += $2} END {print sum/NR}' file.txt   # average column
```

### Grep

```bash
grep "pattern" file.txt                 # basic search
grep -i "pattern" file.txt              # case-insensitive
grep -v "pattern" file.txt              # lines NOT matching
grep -c "pattern" file.txt              # count matches
grep -n "pattern" file.txt              # with line numbers
grep -r "pattern" dir/                  # recursive
grep -E "regex" file.txt                # extended regex
```

### Sed

```bash
sed 's/old/new/' file.txt               # replace first per line
sed 's/old/new/g' file.txt              # replace all per line
sed -i 's/old/new/g' file.txt           # in-place edit
sed -n '5,10p' file.txt                 # print lines 5-10
sed '/pattern/d' file.txt               # delete matching lines
```

### Sort & Uniq

```bash
sort file.txt                           # alphabetical
sort -r file.txt                        # reverse
sort -n file.txt                        # numeric
sort -k2 file.txt                       # by column 2
sort file.txt | uniq                    # unique lines
sort file.txt | uniq -c                 # count occurrences
```

### Tr

```bash
echo "hello" | tr 'a-z' 'A-Z'           # HELLO (uppercase)
echo "hello 123" | tr -d '0-9'          # hello (delete digits)
echo "hello world" | tr ' ' '_'         # hello_world (replace)
echo "hellooo" | tr -s 'o'              # helo (squeeze repeated)
cat file.txt | tr -d '\n'               # remove newlines
```

### Wc

```bash
wc -l file.txt                          # line count
wc -w file.txt                          # word count
wc -c file.txt                          # byte count
```

### Cut

```bash
cut -d',' -f2 file.csv                  # field 2 (comma delim)
cut -d':' -f1,3 /etc/passwd             # fields 1 and 3
cut -c1-10 file.txt                     # characters 1-10
```

---

## Functions

```bash
myfunc() {
    local var="local variable"          # local scope
    echo "Hello $1"                     # access argument
    return 0                            # return status (0-255)
}

myfunc "world"                          # call function
echo $?                                 # check return status

# Return value via echo
get_value() {
    echo "result"
}
result=$(get_value)
```

---

## Exit Codes

```bash
exit 0                                  # success
exit 1                                  # failure

command
echo $?                                 # check last exit status

command && echo "success" || echo "failed"
```

| Code | Meaning |
|------|---------|
| `0` | Success |
| `1` | General error |
| `2` | Misuse of command |
| `126` | Not executable |
| `127` | Command not found |
| `130` | Ctrl+C |

---

## Miscellaneous

### Script Header

```bash
#!/bin/bash
set -euo pipefail                       # strict mode
# -e: exit on error
# -u: error on undefined variable  
# -o pipefail: fail if any pipe command fails
```

### Check if Root

```bash
if [[ "$EUID" -ne 0 ]]; then
    echo "Run as root"
    exit 1
fi
```

### Check Dependencies

```bash
command -v git &> /dev/null || { echo "git required"; exit 1; }
```

### Script Directory

```bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
```

### Debug Mode

```bash
set -x                                  # enable debug
set +x                                  # disable debug
bash -x script.sh                       # run in debug mode
```

### Trap Signals

```bash
cleanup() { rm -f /tmp/tempfile; }
trap cleanup EXIT                       # run on exit
trap "echo 'Interrupted'; exit 1" INT   # handle Ctrl+C
```

---

[↑ Back to Index](#index)
