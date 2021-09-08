# CRUD in Fast api

## Introduction

This is a crud operation on FASTAPI framework. Fastapi in useful for building the fast apis.
This project having a blog system which is like


This project currently runs on the local host. So every api should run from the local host.




## Run this project:-

For run this project you have to first clone this by using

```	 
	 	git remote add origin https://gitlab.com/Vicky_1999/crud_fastapi.git
```

Now you have to install dependencies by using:

In linux/Macos
```		
				pip3 install -r requirenment.txt  
```
In windows
```
				pip install -r requirenment.txt
```
				
To run this project go to this directory(Where you put this project) and run this command.

```
		uvicorn main:app
```


## Operations:


**Create a blog**:-   For creating a blog, you have to go to 
```
				127.0.0.1:8000/blog/create/
```

**Get an objects of a blog**:-  For getting a particular blog, you have to go to
```
				 127.0.0.1:8000/blog/get/title
				at the _**id**_ you have to put the title of the blog you want to see.
```			
		
**Get all blog**:-  For getting every blog, you just have to go to 
```				
				127.0.0.1:8000/blog/get
```

**Update a particular blog**:-  For this you have to give blog's id in this url
```				
__				127.0.0.1:8000/blog/update/ _**id**_
     			     and give what field you want to update
```

**Delete a particular blog**:- For this you have to give blog's id in this url
```
				127.0.0.1:8000/blog/delete/ _**id**_
```


**Thank you**
