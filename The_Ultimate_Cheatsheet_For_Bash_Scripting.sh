# Variables
name="Alice"				# declaring a variable
echo "$name"				# using the variable
printf "Hello %s\n" "world"		# using prints with format specifiers
readonly pi=3.14			# declaring a constant variable
unset name				# removing the variable

# Arithmetic
echo $(( 3 + 5 ))			# prints 8

# Advanced Arithmetic
echo "5 + 3" | bc			# prints 8
echo "5 + 50*3/20 + (19*2)/7" | bc -l	# prints 17.42857142857142857142

# Parameter Expansion
echo "${variable}"			# some string
echo "${variable/some_str/new_str}"	# string substitution
echo "${variable:start:end}"		# string slicing
echo "${#variable}"			# string length
echo "${!other_variable}"		# expands other variable
echo "${foo:-"default_value"}"		# set default value for a variable

# Array
array=(one two three four five six)
echo "${array[0]}"			# one
echo "${array[@]}"			# prints all elements from the array
echo "${#array[@]}"			# length of the array
echo "${#array[2]}"			# length of an element from the array
echo "${array[@]/one/seven}"		# array substitution
echo "${array[@]:3:2}"			# array slicing
array+=("seven")			# append an element to the array
unset array[1]				# remove/pop an element from the array

# Positional Arguments
$0					# name of the current script
$1					# first argument
$2					# second argument
$@					# contains all arguments passed when executing the script
$#					# number of arguments

# Command Substitution
date=$(date)
files=$(ls -l)
echo "Today is $date"

# Conditional Statements

#####numerical_comparison#####
if (( a > 5 )); then echo "yes"; fi

#####string_comparison#####
if [[ "$str" == "hello" ]]; then
	echo "world"
elif [[ "$str" == "dear" ]]; then 
	echo "friend"
else
	echo "bad string"
fi

#####empty_check(-z doesn’t care if the content is numeric or not)#####
if [[ -z "$str" ]]; then echo "empty"; fi

# File Checks
[[ -f file ]]				# exists and is a regular file
[[ -d file ]]				# exists and is a directory
[[ -r file ]]				# readable
[[ -w file ]]				# writable
[[ -x file ]]				# executable

# Logical Operators
[ -f file ] && echo "exists"		# if first command succeeds the next command is executed per command chain
[ -f file ] || echo "exists"		# if first command fails then the next command is executed per command chain

# Redirection and piping
echo "hello" > output.txt		# overwrites output.txt
echo "friend" >> output.txt		# appends to output.txt
cmd1 | cmd2				# cmd1 stdout is sent to stdin of cmd2
command &> file				# redirects both stdout and stderr
cmd |& other_cmd			# cmd1 stdout + stderr is sent to stdin of other_cmd

# Loops
for i in {1..5}; do echo "$i"; done	# loops through the sequence

#####C-Style_for_loop#####
for (( i=0; i<5; i++ )); do 
	echo "$i";
done

#####Looping_through_an_array#####
for x in "${array[@]}"; do
	echo "$x"
done

#####Pipe_entire_loop_output_once#####
for i in {1..5}; do
    echo "$i"
done | cmd

#####Pipe_each_iteration_separately#####
for i in {1..5}; do
    echo "$i" | cmd
done

#####loop_through_command_output#####
for file in $(ls *.txt); do
	echo $file
done

#####while_loop#####
while (( $count < 5 )); do
	echo "$count"
	(( count++ ))
done

# Input/Output
read string				# takes input from stdin

# Read from a file
while read line; do
	echo "$line"
done < file.txt

# Text Processing
awk 'NR==1' file.txt                    # first row
awk 'NR>=2 && NR<=5' file.txt           # rows 2 to 5
awk -F',' '{print $2}' file.csv         # second column (comma-separated)
awk '{print $1, $3}' file.txt           # multiple columns
awk '$3 > 100 {print $1, $3}' file.txt	# filter rows by condition
awk '{print $1 + $2}' file.txt		# prints sum of first and second column

#####Aggregate_(sum, avg, etc.)_using_AWK#####
awk '{sum += $2} END {print sum}' file.txt	# sum of second column
awk '{sum += $2} END {print sum/NR}' file.txt	# average of second column

grep -i "pattern" file.txt              # case-insensitive
grep -v "pattern" file.txt              # lines NOT matching
grep -c "pattern" file.txt              # count matches

sort file.txt                           # sort alphabetically
sort -r file.txt                        # reverse sort
sort file.txt | uniq                    # unique lines
sort -n file.txt                        # numeric sort

sed 's/old/new/' file.txt               # replace first occurrence per line
sed 's/old/new/g' file.txt              # replace ALL occurrences per line
sed -i 's/old/new/g' file.txt           # replace in-place

echo "hello world" | tr 'a-z' 'A-Z'	# prints HELLO WORLD (convert lowercase → uppercase and vice versa)
echo "hello 123" | tr -d '0-9'		# prints hello (delete specific characters)
echo "hello world" | tr ' ' '_'		# prints hello_world (replace a set of characters)
echo "hellooo     world" | tr -s ' o'	# prints helo world (squeeze (merge) repeated characters)
cat file.txt | tr -d '\n'		# remove newlines → make one line

wc -l file.txt                          # line count
wc -w file.txt                          # word count
wc -c file.txt                          # character count

# Functions
myfunc() {
	echo "hello $1"
	return 5
}
myfunc "world"				# prints hello world
echo "$?"				# prints 5

# Exit Codes
exit 0					# success
exit 1					# failure

# Miscellaneous

#####check_if_script_is_run_as_root#####
if [[ "$EUID" != 0 ]]; then
	echo "Run as root"
	exit 1;
fi
