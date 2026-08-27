class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if not accounts:
            return [[]]
        
        uf = UnionFind(len(accounts))
        email_to_index = {}
        index_to_name = {}
        pairs = []
        
        for i, account in enumerate(accounts):
            name = account[0]
            index_to_name[i] = name

            for email in account[1:]:
                if email not in email_to_index:
                    email_to_index[email] = i
                else:
                    uf.union(i, email_to_index[email])
        
        groups = defaultdict(list)
        for email in email_to_index:
            root = uf.find(email_to_index[email])
            groups[root].append(email)
        
        res = []
        for account_id in groups:
            name = index_to_name[account_id]
            res.append([name] + sorted(groups[account_id]))
        
        return res




class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size + 1))
        self.size = [1] * (size + 1)
      

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

        return True


            
