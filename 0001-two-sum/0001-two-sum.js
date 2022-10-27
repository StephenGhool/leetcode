/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // create js object
    var hashmap = {}
    
    for (let i =0; i < nums.length; i++){
        let diff = target - nums[i]
        
        if (diff in hashmap) {
            return [hashmap[diff],i]
        } 
        hashmap[nums[i]] = i
    } 
};