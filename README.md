\# Quick-Calc



Quick-Calc is a simple calculator application developed as part of a Software Testing assignment.  

It supports basic arithmetic operations and demonstrates proper unit and integration testing practices.



---



\## Features



\- Addition

\- Subtraction

\- Multiplication

\- Division (handles division by zero gracefully)

\- Clear function



---



\## Setup



\### 1. Clone the repository



```bash

git clone https://github.com/melisaozctn/swe-testing-assignment.git

cd swe-testing-assignment

```



\### 2. Install dependencies



```bash

pip install pytest

```



---



\## Run Tests



```bash

python -m pytest

```



---



\## Testing Framework Research (pytest vs unittest)



This project uses \*\*pytest\*\* because it allows writing tests with less boilerplate code and very readable assertions.



Compared to Python’s built-in \*\*unittest\*\* framework, pytest provides:

\- Simpler syntax

\- No need for class-based test structure

\- Better error reporting

\- Powerful features like fixtures and parameterization



While \*\*unittest\*\* is included in the standard library and does not require installation, it typically requires more structured and verbose test classes.



For this project, pytest was chosen for better readability, simplicity, and faster development.



