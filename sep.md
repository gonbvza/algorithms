# Report for Assignment 1

## Project chosen

Name: algorithms

URL: https://github.com/keon/algorithms

Number of lines of code: 18023

Tool used to analyze: lizard

Programming language: Python

## Coverage measurement

### Existing tool

The tool we used was coverage, and to be more specific we used it as the pytest --cov flag. This library executed all test files that started with "test_". The method we followed to get the coverage was the following:
1. We forked the repository
2. We created a virtual environment and installed the required libraries
3. We changed any test files names that did not start with "test_" so they started with the correct prefix
4. We ran the command 

    ```
        pytest --cov --cov-report=html
    ```

This method produced both a report in the command line and a html that we used to find the functions that were not covered. 

The coverage percentage that we obtained after running this command was of 90% as shown in the following picture:



<Show the coverage results provided by the existing tool with a screenshot>

### Your own coverage tool

<The following is supposed to be repeated for each group member>

<Group member name>

<Function 1 name>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>

<Function 2 name>

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>

