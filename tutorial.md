# Shell scripting/Bash scripting

In linux, process automation relies heavily on shell scripting. This is basically a file containing a series of commands that can be executed together.

1. Run ps to find the shell you are using
2. date to find the data
3. pwd shows the working dir
4. ls shows the contents of the current directory
5. echo prints a string of text or value to the terminal
6. Shebang -> #!/bin/bash -> this tells the shell to execute it via bash shell.
7. set variables like this `country=Australia`. To access this value put a `$` in front of it.


### Reading a file
`
while read line
do 
    echo $line
done < input.txt
`
### Command line arguments
`$1` denotes the initial argument passed
`$2` denotes the second arugment passed

### Write/append to a file
`echo "This is a text" > output.txt`

`echo "More text" >> output.txt` # append


### Conditions
`
if [[ condition ]];
then
    statement
elif [[ condition ]]; then
    statement
else
    do this by default
fi
`

We can use logical operators such as AND -a and OR -o to make comparisons 
`
if [ $a -gt 60 -a $b -lt 100 ]
`

### Important learning points

1. Use [[ ]] for regex matching with =~
2. Use [ ] for simple string/number comparisons with =, !=, -eq, etc.
3. Regex patterns need =~ operator, not =



# References
1. Free code camp bash scripting