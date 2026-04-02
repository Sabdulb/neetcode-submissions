class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            temp = Counter(nums)
            arr = [[] for i in range(len(nums) + 1)]

            for l,v in temp.items():
                arr[v].append(l)
            
            print(arr)

            count = 0
            ans = []
            for i in range(len(arr) - 1, -1, -1):
                print(count)
                print(k)
                if count >= k:
                    return ans
                if len(arr[i]) == 1:
                    ans.append(arr[i][0])
                    count += 1
                    print(ans)
                    print("elif")
                elif len(arr[i]) > 1:
                    for val in arr[i]:
                        if count >= k:
                            return ans
                        else:
                            ans.append(val)
                            print(ans)
                            print("else")
                            count += 1

            return ans