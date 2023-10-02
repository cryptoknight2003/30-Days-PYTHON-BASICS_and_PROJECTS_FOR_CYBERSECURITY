#the simple print function () usuage is  to simply use the print fuction to print the string 


print("Hello world")




#not i  m mentioning some parameters that can be used with the print function *()



""" there are some parameters which are used with print functions  such as 

1<< end parameters
2<< format parameters
3<< separator parameters

key note:- We will use these parametersto beautifully print our functions it included end parameters << separator parameters << format parameters


1.... separator 
separator represents a delimiter based on which the given string or line is separated 
 example 
    ..............   
                  If i print a statement it would be like 
                  print("hello world")
                  

but what is i use a separator in between the string to do so we will use separator as 
                sep=" , "    --- This will use the separator , in between the strings


now the new program will look like 

                 print("hello" , " world ")

                 separator ends here 






2...... END parameter 
The end parameter is used with the print function to specify what should be printed at the end of a line of text or string  becuse by default 
print() uses \n  and print the result   ... this parameter is represented by     end=

example
    ..........  simple code :-----
                            .......     print("hello")
                            .......     print("world")

                and now using    " end= "    

                print("hello" , end="not really")
                print("world")

                and this will print the output as .........   hello not really world


one more example 

a = 10
b = 20
print(a , end= "is greater than")
print(b)

output will be  ... 10 is greater than 20




3...........  FORMAT parameter

format function in python ==  str.format () is technique of the string category permits you to try and do variable substitutions 
and data formatting


** it is represented as ( .format )

simple code ::--
....................   name = "Satyam"
..........             age = 20
..........             print(name + "is" +str(age)+ "years old" )

this is a code with out using format fxn. and it seems quite compled to write .....


new code   with  .formate function :-

name = "Satyam"
age = 20 
print("{} is {} years old " .format(name , age))

using .format makes  it simple and clearn and we don't even have to use str to get age 

another example


  animal = "cow"
  bird= "parrot"
  os = "kali"

  print("{} is loved by everyone and {} can talk {} and my favourite is {}"  .format(animal , bird , os))

  

we are printing the same thing but now in different ways """