# Awesome! AdventOfCode - Solutions in Python

These are my solutions for some of the puzzles provided by 
[Advent of Code](https://adventofcode.com/2023/about) (be sure to check it out!)
The primary reason for solving the puzzles is simply the pure joy of doing so.
The other reason is to challenge myself and get better at coding. 
After some time I realized there are reoccurring tasks like downloading the files etc. I automated that part in another mini project: [Setup Advent of Code DAYX](https://github.com/ce4os/setup_aoc)

<blockquote>
Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets 
and skill levels that can be solved in any programming language you like.
You don't need a computer science background to participate - just a little programming knowledge
and some problem solving skills will get you pretty far. Nor do you need a fancy computer; every problem has a solution that completes in at most 15 seconds on ten-year-old hardware.
</blockquote>

## Implementing Unit Tests

I solved a lot of those puzzles but the code quality was sometimes poor. This is because
I just solved the puzzles withouth thinking to much about readability, reausability and 
testing my code (those where the early days of my journy). Revisiting code I wrote half a 
year ago was more or less mind blowing and this beautiful sentence finally came true:
<blockquote>
You will look upon a file with a fond sense of remembrance. Then a sneaking feeling of foreboding, knowing that someone less experienced, less wise, had written it.
</blockquote>  
Taken from:[writethedocs](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/)

To learn from this experience, I decided to refactor my code from 2016/day4 on before publishing it and to implement Unit Tests to take the next step. The solutions for year 2015 are somewhat refactored but require a revisit nonetheless.
For comparison I upload the unrefactored code too. 

The basic structure is:
/BASE_DIR/
├── 2015
|   ├── day1.py
│   ├── day1_refactored.py
│   ├── day1_unit_tests.py
|   ├── utils.py
|   ├── ...
|   └── src/
|        ├── day1_input
|        ├── ...
|        └── dayX_input       
|
| ...
|
└── 2023
   ├── day1.py
   ├── day1_refactored.py
   ├── day1_unit_tests.py
   ├── utils.py
   ├── ...
   └── src/
        ├── day1_input
        ├── ...
        └── dayX_input


