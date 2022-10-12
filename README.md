# Fizz Buzz Game

## User Story

- Substitute Multiple of 3 for fizz
- Substitute Multiple of 5 for buzz
- Substitute Multiple of 3 X 5 with fizzbuzz

- Range 1 To 100

```commandline
num = 1 # Initialize the counter

while num <= 100:
    if num % 15 == 0:
        print("FizzBuzz")  # Multiple of 15, displays "FizzBuzz"
    elif num % 3 == 0:
        print("Fizz")  # Multiple of 3, displays "Fizz"
    elif num % 5 == 0:
        print("Buzz")  # Multiple of 5, displays "Buzz"
    else:
        print(num)
    num += 1  # Incrementing the number, else infinite loop
    
Output:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
```