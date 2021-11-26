class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> res;
        k = k% nums.size();
        for(int i = nums.size() - k; i< nums.size(); i++)
            res.push_back(nums[i]);
        for(int j = 0; j< nums.size() -k; j++)
            res.push_back(nums[j]);
        nums = res;
    }
};