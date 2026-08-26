### 

### **Annex C**

**Code Quality Assessment Worksheet**

**Section: 9 \- Magnesium	Score:\_\_\_\_\_\_\_\_\_\_\_\_**  
**C\# / Name :Azriel Jesse C. Ting, Kier Benedict Obaredes	Date: \_\_\_\_\_\_\_\_\_\_\_\_\_**

**Instructions:**

**The problem: Search for a Number in a Sorted List**

**For example: Both algorithms could search:**   
numbers \= \[5, 12, 18, 23, 31, 47, 56, 68, 74, 90\]  
target \= 47

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| def linear\_search(numbers, target):    *for* i *in* range(len(numbers)):        *if* numbers\[i\] \== target:            *return* i    *return* \-1   | def binary\_search(numbers, target):    low \= 0    high \= len(numbers) \- 1     *while* low \<= high:        middle \= (low \+ high) // 2         *if* numbers\[middle\] \== target:            *return* middle        *elif* numbers\[middle\] \< target:            low \= middle \+ 1        *else*:            high \= middle \- 1     *return* \-1   |

## 

## 

## 

## 

## **Questions with Checklists**

### **1\. Efficiency**

**Which algorithm is faster when the list of numbers is very large? Why?**

Algorithm 2 would be faster when the list of numbers is large because the input list is already sorted instead of going through and checking each element 1 by 1\.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list? | How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list? |

**2\. Readability**

**Which algorithm is easier to understand at first glance? What makes it clearer?**

At first glance, Algorithm 1 is easier to understand because it looks simpler, less lines of code, more practical and the use of less complicated loops and conditional statements make it clearer.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process? | How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process? |

### 

### 

### 

### **3\. Maintainability**

**If you had to modify the program, such as changing what happens when the target is found, which algorithm would be easier to update? Why?**

If we were to modify the program, Algorithm 1 would be easier to update because of how simple the structure is, it uses a single comparison inside one loop, which means we really only have 1 place to modify the code when the target is found. Meanwhile, algorithm 2 contains a more complex control flow and tracking of variables, making updates to the logic which can be more prone to errors.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating? | Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating? |

### 

### **4\. Testability**

**Which algorithm is easier to test with different inputs? Why?**

Algorithm 1 is easier to test for different output because it has one loop and basic logic. Meanwhile Algorithm 2 requires multiple conditional branches and complex logic, creating test cases that make sure of custom output behaviour requires checking more and more potential logic paths.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear? | Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear? |

### **5\. Reliability and Input Validation**

**What should the algorithm check to avoid errors when receiving input from a user?**

For Algorithm 1: Check that the variable *numbers* is a list, and target is a compatible data type ; Make sure that numbers and target is not None to prevent errors during executions.

For Algorithm 2: Check that the items inside *numbers* are sorted in ascending order, make sure that all items inside numbers are strictly orderable(ex. Numbers to strings are NOT possible.)

For both: Empty lists should be handled properly to avoid unnecessary processing or unexpected outputs.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Linear Search? | Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Binary Search? |

### 

### **6\. Final Answer**

Based on your answers from 1 to 5, Which algorithm would you choose for this problem, and under what conditions would the other algorithm be more suitable? Summarize your answer.

Based on our answers from 1 to 5, we choose algorithm 1 because it’s easier to write, test, and update because of its simple loop structure. It is the best choice when dealing with unsorted lists, small datasets, or one-time searches where sorting overhead isn’t worth it. However, it requires basic input checks for valid data types, null values, and empty lists to avoid runtime errors. 
