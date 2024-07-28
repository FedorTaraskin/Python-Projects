##https://claude.ai/chat/736fbead-dbe1-4e09-a2cb-0df156105708

def longest_string(*args):
	a = ''
	for i in args:
		if len(i) > len(a): a = i

# Test cases
print(longest_string("apple", "banana", "cherry"))  # Should print: banana
print(longest_string("cat", "dog", "elephant", "fox"))  # Should print: elephant
print(longest_string("a", "ab", "abc", "abcd", "abcde"))  # Should print: abcde

##----------------------------------------------------------------------------##

def multiply_all(*args):
	a = 1
	for i in args: a *= i
	return a

# Test cases
print(multiply_all(2, 3, 4))  # Should print: 24
print(multiply_all(1, 2, 3, 4, 5))  # Should print: 120
print(multiply_all(10))  # Should print: 10

##----------------------------------------------------------------------------##

def merge_lists(*args):
	a = list()
	for i in args: 
		for b in i: a.append(b)
	return a

# Test cases
print(merge_lists([1, 2, 3], [4, 5, 6]))  # Should print: [1, 2, 3, 4, 5, 6]
print(merge_lists([1], [2], [3], [4, 5]))  # Should print: [1, 2, 3, 4, 5]
print(merge_lists(['a', 'b'], [1, 2], ['Python']))  # Should print: ['a', 'b', 1, 2, 'Python']

##----------------------------------------------------------------------------##

def repeat_string(string, *args):
	return string*sum(args)

# Test cases
print(repeat_string("hello", 3))  # Should print: hellohellohello
print(repeat_string("abc", 1, 2, 3))  # Should print: abcabcabcabcabcabc
print(repeat_string("hi", 0))  # Should print: (an empty string)

##----------------------------------------------------------------------------##

def grade_student(name, *args):
	# Your code here
	avg = sum(args)/len(args)
	##Must surpass the value to reach a grade letter
	gradeThresholds = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
	for a, b in gradeThresholds.items():
		if avg >= b: 
			grade = a
			break
	return tuple((name, avg, grade))

# Test cases
print(grade_student("Alice", 92, 85, 98))  # Should print: ('Alice', 91.67, 'A')
print(grade_student("Bob", 75, 80, 85, 90))  # Should print: ('Bob', 82.5, 'B')
print(grade_student("Charlie", 50, 55))  # Should print: ('Charlie', 52.5, 'F')