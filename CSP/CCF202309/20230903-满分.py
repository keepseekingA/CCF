def _add():     # +号求导
    pass


def _sub():     # -号求导
    pass


def _mcl():     # *号求导
    pass


class BiTNode:
    """二叉树节点类"""
    root = None     # 根节点

    def __init__(self, data):
        self.data = data    # 根
        self.left = None    # 左
        self.right = None   # 右

    def linsert(self, node):    # 插入左孩子
        self.left = node

    def rinsert(self, node):    # 插入右孩子
        self.right = node


def get_build():     # 对逆波兰式解析,并构建二叉树
    pass


def preOrder(root: BiTNode):   # 先序遍历
    if root:
        print(root.data)   # 在这里写求导操作
        preOrder(root.left)
        preOrder(root.right)


if __name__ == "__main__":
    pass
