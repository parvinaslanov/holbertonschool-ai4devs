# Prompt Testing Examples

## Example 1 - Refactoring Prompt
**Prompt**: Refactor the following Python function for readability and type hinting.
**Input**:
```python
def calc(a,b): return a+b*10
```

**AI Output**:
```python
def calculate_total(a: int, b: int) -> int:
    """Return a plus b times 10."""
    return a + (b * 10)
```

**Feedback**: Output is correct and clean; type hints and docstring were added successfully.


## Example 2 - Summarization Prompt
**Prompt**: Summarize the following technical paragraph into three concise bullet points for a project README.
**Input**:
Continuous integration (CI) is the practice of automating the integration of code changes from multiple contributors into a single software project. It allows developers to frequently merge code changes into a central repository where automated builds and tests are run. Automated tools are used to assert the new code's correctness before integration.

**AI Output**:
* Automates code integration from multiple contributors into a central repository.
* Encourages frequent code merging and automated builds.
* Runs automated tests to verify code correctness prior to integration.

**Feedback**: The summary is concise, accurate, and fits the target format well.


## Example 3 - Code Generation Prompt
**Prompt**: Write a JavaScript function that checks if a given string is a palindrome, ignoring spaces and capitalization.
**Input**:
```javascript
const text = "A man a plan a canal Panama";
```

**AI Output**:
```javascript
function isPalindrome(str) {
    const cleaned = str.toLowerCase().replace(/[^a-z0-9]/g, '');
    return cleaned === cleaned.split('').reverse().join('');
}
```

**Feedback**: The generated function handles spaces, punctuation, and case sensitivity accurately.


## Example 4 - Bug Fixing Prompt
**Prompt**: Identify and fix the bug in the following JavaScript function that calculates an array sum.
**Input**:
```javascript
function sumArray(arr) {
    let sum = 0;
    for (let i = 1; i <= arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}
```

**AI Output**:
```javascript
function sumArray(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}
```

**Feedback**: Correctly identified the off-by-one errors (starting index at 1 instead of 0, and using <= arr.length causing an undefined index).


## Example 5 - Documentation Prompt
**Prompt**: Write a JSDoc comment block for the following utility function.
**Input**:
```javascript
function formatCurrency(amount, currency = 'USD') {
    return new Intl.NumberFormat('en-US', { style: 'currency', currency }).format(amount);
}
```

**AI Output**:
```javascript
/**
 * Formats a numeric amount into a localized currency string.
 * @param {number} amount - The monetary value to format.
 * @param {string} [currency='USD'] - The ISO 4217 currency code.
 * @returns {string} The formatted currency string.
 */
function formatCurrency(amount, currency = 'USD') {
    return new Intl.NumberFormat('en-US', { style: 'currency', currency }).format(amount);
}
```

**Feedback**: The JSDoc documentation is comprehensive, accurately describes parameters, and includes default values.
```
