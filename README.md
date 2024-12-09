Markdown
# Test Project

**Description:**
Test ticket in python.

**Getting Started:**

1. **Clone the repository:**

```bash
   git clone git@github.com:Av007/ytest.git
```
or 
```
curl -L http://github.com/Av007/ytest/archive/main.zip
```

2. **Projects**

***Buildings Puzzle***
Was built without any custom library. Was covered by pytest by 95% (but it's not helped to get some edge cases). The solution is working, however the random matrix solving not always right way. The ideally need
another round of refactoring to:
 - include a union way to read/write the matrix by sequences (up, down, left, right)
 - find the way to add custom logic for read/write sequences (maybe lambda or ContextManager...)
 - add more test cases


***Undirected Word Graph***
Was built without any custom library. Was used a class 
to define a structure to represent a undirected graph 
method. Wasn't covered by tests.

3. **Installation (optional)**

a. Create Virtual Envirounment
```
python -m venv venv
source venv/bin/activate
```
b. Install dependencies:
```
pip install -r requirements.txt
```
4. **Run the project**

Both projects has run.py in root of projects which includes function to get results. 

5. **Test**

For puzzle project we can run tests
```
pytest -v -s
```
