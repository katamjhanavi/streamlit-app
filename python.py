import streamlit as st

st.title("Python")

st.write("Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.")

st.subheader("Core features")
st.text("""1.Easy to Learn and Use: Python has a simple, clean syntax that reads almost like English, making it ideal for beginners and faster development.
2.Interpreted Language: It's executed line by line by an interpreter, which allows for quick prototyping and debugging. You don't need to compile it before running.
3.Dynamically Typed: You don't need to declare the variable type (like integer or string) before using it. The type is checked during execution.
4.High-Level Language: Developers don't need to manage low-level details like memory allocation; this is handled automatically.
5.Object-Oriented Programming (OOP): Supports OOP principles, allowing code to be organized using classes and objects for reusability and modularity.
6.Open Source and Free: Python is developed under an open-source license, meaning it's free to use and distribute, even for commercial purposes.""")


st.subheader("Key concepts")
st.text("""Readability: Code structure uses indentation (whitespace) to define code blocks (like loops and functions) instead of braces, strongly enforcing clean code.

Extensive Standard Library: Comes with a huge collection of pre-written modules and functions (e.g., for file I/O, networking, and math) that save development time.

Portability (Cross-Platform): Python code written on one operating system (like Windows) will run on others (like macOS or Linux) with little or no modification.

Automatic Memory Management: Uses a built-in garbage collector to automatically manage memory allocation and deallocation, freeing the programmer from manual memory handling.

Guido van Rossum: The creator of the Python language.""")


st.subheader("Common uses")
st.text("""1.Web Development (Backend): Building the server-side logic for websites and applications.
2.Data Science and Machine Learning: Analyzing data, creating predictive models, and training AI.
3.Scripting and Automation: Writing small programs to automate repetitive tasks (e.g., file processing, system maintenance).
4.Software Testing: Used for unit testing and creating test scripts.
5.System Administration: Managing operating systems and infrastructure.""")