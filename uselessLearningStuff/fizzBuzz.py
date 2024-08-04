##https://github.com/karan/Projects#:~:text=Fizz%20Buzz%20%2D%20Write%20a%20program%20that%20prints%20the%20numbers%20from%201%20to%20100.%20But%20for%20multiples%20of%20three%20print%20%E2%80%9CFizz%E2%80%9D%20instead%20of%20the%20number%20and%20for%20the%20multiples%20of%20five%20print%20%E2%80%9CBuzz%E2%80%9D.%20For%20numbers%20which%20are%20multiples%20of%20both%20three%20and%20five%20print%20%E2%80%9CFizzBuzz%E2%80%9D.
for i in range (1,101):
	if i % 3 == 0 and i % 5 == 0: print('Fizz Buzz')
	elif i % 3 == 0: print('Fizz')
	elif i % 5 == 0: print('Buzz')
	else: print(i)