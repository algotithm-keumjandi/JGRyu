'''
1. 힙은 최대힙(Max heap)과 최소힙(Min heap)으로 나뉘어진다. 최대힙은 자식 노드보다 부모 노드의 값이 크고, 최소힙은 자식 노드보다 부모 노드의 값이 작다.
2. 노드가 왼쪽부터 채워지는 완전 이진 트리 형태를 가진다.
3. 중복을 허용한다.
(부모 노드의 인덱스) = (자식 노드 인덱스) // 2
(왼쪽 자식 노드의 인덱스) = (부모 노드의 인덱스) * 2
(오른쪽 자식 노드의 인덱스) = (부모 노드의 인덱스) * 2 + 1
'''

class Heap():
    def __init__(self) -> None:
        self.heap = []
        self.heap.append(None) # 시작 index를 1로 하기 위해 None 삽입
    
    def check_swap_up(self, idx):
        if idx <= 1:
            return False
        parent_idx = idx // 2
        if self.heap[idx] > self.heap[parent_idx]:
            return True
        else:
            return False
    
    def insert(self, data):
        self.heap.append(data)
        idx = len(self.heap)

        while self.check_swap_up(idx):
            parent_idx  = idx // 2
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
        return True # ?
        
    def check_swap_down(self, idx):
        left_idx = idx * 2
        right_idx = idx * 2 + 1

        if left_idx >= len(self.heap):
            return False
        elif right_idx >= len(self.heap):
            if self.heap[left_idx] > self.heap[idx]:
                self.flag = 1
                return True
            else:
                return False
        else:
            if self.heap[left_idx] > self.heap[right_idx]:
                if self.heap[left_idx] > self.heap[idx]:
                    self.flag = 1
                    return True
                else:
                    return False
            else:
                if self.heap[right_idx] > self.heap[idx]:
                    self.flag = 2
                    return True
                else:
                    return False
    def pop(self):
        if len(self.heap) <= 1:
            return None
        
        max = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        idx = 1
        self.flag = 0

        while self.check_swap_down(idx):
            left_idx = idx * 2
            right_idx = idx * 2 + 1
            if self.flag == 1:
                self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                idx = left_idx
            elif self.flag == 2:
                self.heap[idx], self.heap[right_idx] = self.heap[right_idx], self.heap[idx]
                idx = right_idx
        return max
    

