class Solution:
    def maximumWealth(self,accounts):
        max_wealth=0
        for customer in accounts:
            wealth=sum(customer)
            max_wealth=max(max_wealth,wealth)
        return max_wealth
if __name__=="__main__":
    accounts=[[1,2,3],[2,3,1,]]
    solution = Solution()
    print(solution.maximumWealth(accounts))