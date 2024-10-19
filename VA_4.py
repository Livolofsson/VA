"""
Solutions to module VA 4

Student:
Mail:
"""
#!/usr/bin/env python3

from person import Person

"""
Write a script that gives a plot for comparison of two approaches for Fibonacci numbers
"""
def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())

	f.setAge(51)
	print(f.getAge())
	print(f.getDecades())

if __name__ == '__main__':
	main()


"""What is the result for Fibonacci with n=47? Why?"""