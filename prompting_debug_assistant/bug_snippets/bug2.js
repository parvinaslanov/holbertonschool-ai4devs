function getFirstNItems(items, n) {
    /**
     * Intended Behavior: Return the first n items from an array.
     * Issue Type: Off-by-one loop logic issue
     */
    let result = [];
    
    // Bug: Uses '<=' instead of '<', causing an off-by-one or out-of-bounds issue
    for (let i = 0; i <= n; i++) {
        if (i < items.length) {
            result.push(items[i]);
        }
    }
    return result;
}

// Example usage:
// console.log(getFirstNItems([1, 2, 3], 2));
