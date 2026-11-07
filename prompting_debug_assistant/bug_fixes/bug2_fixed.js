function getFirstNItems(items, n) {
    /**
     * Intended Behavior: Return the first n items from an array.
     * Issue Type: Off-by-one loop logic issue
     */
    let result = [];
    
    for (let i = 0; i < n; i++) {
        if (i < items.length) {
            result.push(items[i]);
        }
    }
    return result;
}

// Test case
console.log(getFirstNItems([1, 2, 3, 4, 5], 3));
